from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import create_engine, text
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

import re
from google import genai
import json


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "") 
gemini_client = None
if GEMINI_API_KEY:
    try:
        gemini_client = genai.Client(api_key=GEMINI_API_KEY)
    except Exception as e:
        print(f"Failed to init Gemini: {e}")

try:
    from scraper import search_candidate
except ImportError:
    def search_candidate(name, state, level):
        return {"name": "Error", "party": "Error", "link": "#"}

app = FastAPI(title="CandidateValidate API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/cvdb")
engine = create_engine(DATABASE_URL)

class LocationRequest(BaseModel):
    latitude: float
    longitude: float

class AnalysisRequest(BaseModel):
    name: str
    party: str
    cases: str
    assets: str

@app.get("/")
def home():
    return {"message": "Candidate Validator API is Running 🚀"}

# --- NEW: GET LIST OF STATES ---
@app.get("/api/states")
def get_states():
    """Returns a list of all available states/UTs in the database."""
    try:
        query = text("SELECT DISTINCT st_name FROM constituencies_ac ORDER BY st_name;")
        with engine.connect() as conn:
            result = conn.execute(query).fetchall()
            return [row[0] for row in result]
    except Exception as e:
        print(f"❌ State Fetch Error: {e}")
        return []

# --- UPDATED: FILTER SHAPES BY STATE ---
@app.get("/api/shapes")
def get_shapes(state: str = Query("MAHARASHTRA", description="State Name")):
    """
    Returns Assembly Constituencies for the requested State.
    """
    try:
        # Dynamic State Injection
        query = text("""
            SELECT json_build_object(
                'type', 'FeatureCollection',
                'features', json_agg(
                    json_build_object(
                        'type', 'Feature',
                        'geometry', ST_AsGeoJSON(geometry)::json,
                        'properties', json_build_object(
                            'name', ac_name,
                            'ac_no', ac_no
                        )
                    )
                )
            )
            FROM constituencies_ac
            WHERE st_name = :state;
        """)
        with engine.connect() as conn:
            result = conn.execute(query, {"state": state.upper()}).scalar()
            return result if result else {"type": "FeatureCollection", "features": []}
    except Exception as e:
        print(f"❌ Map Shape Error: {e}")
        return {"type": "FeatureCollection", "features": []}

@app.post("/api/vicinity")
def get_vicinity(location: LocationRequest):
    # (Same as before - keeping your demo overrides and logic)
    if 19.25 < location.latitude < 19.35 and 73.25 < location.longitude < 73.35:
        return {
            "coordinates": {"lat": location.latitude, "lon": location.longitude},
            "mp_constituency": "Kalyan",
            "mp_state": "Maharashtra",
            "mla_constituency": "Kalyan Rural",
            "mla_number": "144",
            "mla_candidate": "Rajesh Govardhan More",
            "mla_party": "Shiv Sena",
            "mla_cases": "2",
            "mla_assets": "Rs 5 Crore+",
            "mla_link": "https://myneta.info/Maharashtra2024/candidate.php?candidate_id=3062",
            "mla_image": "https://myneta.info/Maharashtra2024/images/candidate_photos/3062.jpg"
        }

    try:
        with engine.connect() as connection:
            pc_query = text("SELECT * FROM constituencies_pc WHERE ST_Contains(geometry, ST_SetSRID(ST_MakePoint(:lon, :lat), 4326));")
            pc_result = connection.execute(pc_query, {"lon": location.longitude, "lat": location.latitude}).mappings().fetchone()
            
            ac_query = text("SELECT * FROM constituencies_ac WHERE ST_Contains(geometry, ST_SetSRID(ST_MakePoint(:lon, :lat), 4326));")
            ac_result = connection.execute(ac_query, {"lon": location.longitude, "lat": location.latitude}).mappings().fetchone()

            mla_data = {}
            if ac_result:
                name = ac_result.get('ac_name', ac_result.get('name'))
                state = ac_result.get('st_name', ac_result.get('state'))
                if name:
                    # --- Primary: look up from candidates_winner DB table ---
                    db_winner = connection.execute(
                        text("""
                            SELECT name, party, cases, assets, image, link
                            FROM candidates_winner
                            WHERE LOWER(ward) = LOWER(:ward)
                               OR LOWER(ward) LIKE LOWER(:partial)
                               OR LOWER(:ward) LIKE LOWER(CONCAT('%', ward, '%'))
                            LIMIT 1
                        """),
                        {"ward": name, "partial": f"%{name}%"}
                    ).mappings().fetchone()

                    if db_winner:
                        mla_data = {
                            "name":   db_winner["name"],
                            "party":  db_winner["party"],
                            "cases":  db_winner["cases"],
                            "assets": db_winner["assets"],
                            "image":  db_winner["image"],
                            "link":   db_winner["link"],
                        }
                    else:
                        # --- Fallback: scraper (unreliable, used only if ward not in DB) ---
                        print(f"⚠️  Ward '{name}' not in candidates_winner, trying scraper...")
                        mla_data = search_candidate(name, state, "assembly")

            return {
                "coordinates": {"lat": location.latitude, "lon": location.longitude},
                "mp_constituency": pc_result.get('pc_name', 'Unknown') if pc_result else "Not Found",
                "mp_state": pc_result.get('st_name', 'N/A') if pc_result else "N/A",
                "mla_constituency": ac_result.get('ac_name', 'Unknown') if ac_result else "Not Found",
                "mla_number": ac_result.get('ac_no', 'N/A') if ac_result else "N/A",
                "mla_candidate": mla_data.get('name', 'Unknown'),
                "mla_party": mla_data.get('party', 'N/A'),
                "mla_cases": mla_data.get('cases', '?'),
                "mla_assets": mla_data.get('assets', '?'),
                "mla_link": mla_data.get('link', '#'),
                "mla_image": mla_data.get('image', None)
            }

    except Exception as e:
        print(f"❌ Error: {e}")
        return {"error": "Backend Error", "details": str(e)}

@app.post("/api/analyze")
def analyze_candidate(data: AnalysisRequest):
    # Determine the numerical baseline averages for the state.
    state_avg_cases = 0.0
    state_avg_assets = 0.0
    candidate_cases = 0
    candidate_assets_crore = 0.0
    
    try:
        try:
            cases_str = ''.join(filter(str.isdigit, str(data.cases)))
            candidate_cases = int(cases_str) if cases_str else 0
        except:
            candidate_cases = 0
        candidate_assets_crore = parse_assets_crore(data.assets)
        
        with engine.connect() as conn:
            avg_row = conn.execute(text("SELECT AVG(CAST(NULLIF(cases, '') AS NUMERIC)) AS avg_cases FROM candidates_winner")).mappings().fetchone()
            state_avg_cases = round(float(avg_row["avg_cases"] or 0), 2)
            
            all_asset_rows = conn.execute(text("SELECT assets FROM candidates_winner")).scalars().fetchall()
            all_assets_crore = [parse_assets_crore(a or "") for a in all_asset_rows]
            state_avg_assets = round(sum(all_assets_crore) / len(all_assets_crore), 2) if all_assets_crore else 0
    except Exception as e:
        print(f"Stats Error inside analyze: {e}")

    result_payload = None

    if gemini_client:
        try:
            prompt = f"""
            Act as a strict, neutral political analyst. 
            Analyze this Indian Politician based on their affidavit data:
            Name: {data.name}
            Party: {data.party}
            Criminal Cases: {data.cases}
            Assets: {data.assets}

            Output a JSON object ONLY (no markdown or additional text) with these keys:
            - summary: A 2-sentence summary of their profile.
            - red_flags: List of 2 potential concerns (if any).
            - green_flags: List of 2 positive indicators.
            - verdict: One word ("Safe", "Caution", "Risky").
            """
            response = gemini_client.models.generate_content(
                model='gemini-2.5-flash',
                contents=prompt
            )
            clean_text = response.text.strip()
            if clean_text.startswith("```json"):
                clean_text = clean_text[7:]
            elif clean_text.startswith("```"):
                clean_text = clean_text[3:]
            if clean_text.endswith("```"):
                clean_text = clean_text[:-3]
            clean_text = clean_text.strip()
            
            result_payload = json.loads(clean_text)
        except Exception as e:
            print(f"Gemini AI Error: {e}")
    
    if not result_payload:
        verdict = "Safe"
        cases_str = str(data.cases).lower()
        if "0" not in cases_str and "no" not in cases_str: 
            verdict = "Caution"
            try:
                if int(data.cases) > 5: verdict = "Risky"
            except: pass

        result_payload = {
            "summary": f"{data.name} is a prominent leader from {data.party} with declared assets of {data.assets}. Their legal record is a primary factor in this analysis.",
            "red_flags": [f"{data.cases} Criminal Cases declared in affidavit", "High asset disparity compared to average"],
            "green_flags": ["Active political engagement", "Publicly available affidavit data"],
            "verdict": verdict
        }

    # Inject the exact stats required for the comparative chart
    result_payload["candidate_stats"] = {
        "cases": candidate_cases,
        "assets_crore": candidate_assets_crore
    }
    result_payload["state_avg"] = {
        "cases": state_avg_cases,
        "assets_crore": state_avg_assets
    }
    
    return result_payload

# ---------------------------------------------------------------------------
# GET /api/search-candidates?q=<name>
# Searches candidates by name across both winner and aspiring tables.
# ---------------------------------------------------------------------------
@app.get("/api/search-candidates")
def search_candidates_by_name(q: str = Query(..., min_length=2, description="Candidate name to search")):
    """
    Returns up to 10 candidates whose name matches the query string.
    Searches both candidates_winner and candidates_aspiring tables.
    """
    try:
        pattern = f"%{q}%"
        with engine.connect() as conn:
            # Search winners
            winner_rows = conn.execute(
                text("""
                    SELECT name, party, ward, cases, assets, image, TRUE AS is_winner
                    FROM candidates_winner
                    WHERE name ILIKE :pattern
                    LIMIT 10
                """),
                {"pattern": pattern}
            ).mappings().fetchall()

            # Search aspiring candidates
            aspiring_rows = conn.execute(
                text("""
                    SELECT name, party, ward, cases, assets, FALSE AS is_winner
                    FROM candidates_aspiring
                    WHERE name ILIKE :pattern
                      AND ward != '__default__'
                    LIMIT 10
                """),
                {"pattern": pattern}
            ).mappings().fetchall()

            # Merge, de-duplicate by name+ward, cap at 10 total
            seen = set()
            results = []
            for row in list(winner_rows) + list(aspiring_rows):
                key = (row["name"], row["ward"])
                if key not in seen:
                    seen.add(key)
                    results.append({
                        "name": row["name"],
                        "party": row["party"],
                        "ward": row["ward"],
                        "cases": row["cases"],
                        "assets": row["assets"],
                        "is_winner": bool(row["is_winner"]),
                    })
                if len(results) >= 10:
                    break

            return results
    except Exception as e:
        print(f"❌ Candidate Search Error: {e}")
        return []

# ---------------------------------------------------------------------------
# Helper: Parse asset string → float (₹ Crore)
# Handles: "Rs 38 Crore+", "Rs 5 Lakhs", "Rs 5 Lakh+", "Rs 80 Lakh+", etc.
# ---------------------------------------------------------------------------
def parse_assets_crore(asset_str: str) -> float:
    if not asset_str:
        return 0.0
    s = asset_str.lower().replace(",", "").replace("+", "").strip()
    m = re.search(r"[\d]+(?:\.\d+)?", s)
    if not m:
        return 0.0
    val = float(m.group())
    if "lakh" in s:
        return round(val / 100.0, 2)  # convert lakhs → crore
    return val  # already crore

# ---------------------------------------------------------------------------
# GET /api/all-candidates
# Returns all wards and their candidates (winners and aspirants).
# ---------------------------------------------------------------------------
@app.get("/api/all-candidates")
def get_all_candidates():
    """
    Returns all candidates grouped by ward, with global and local averages for charting.
    """
    try:
        with engine.connect() as conn:
            # 1. Fetch all winners
            winners = conn.execute(
                text("SELECT ward, name, party, cases, assets, image FROM candidates_winner ORDER BY ward")
            ).mappings().fetchall()

            # 2. Fetch all aspirants
            aspirants = conn.execute(
                text("SELECT ward, name, party, cases, assets FROM candidates_aspiring WHERE ward != '__default__'")
            ).mappings().fetchall()

            # --- Global Averages ---
            avg_row = conn.execute(
                text("""
                    SELECT
                        COUNT(*) AS total,
                        AVG(CAST(NULLIF(cases, '') AS NUMERIC)) AS avg_cases
                    FROM candidates_winner
                """)
            ).mappings().fetchone()
            total_wards = int(avg_row["total"] or 0)
            avg_cases = round(float(avg_row["avg_cases"] or 0), 2)
            all_assets_crore = [parse_assets_crore(w["assets"] or "") for w in winners]
            avg_assets = round(sum(all_assets_crore) / len(all_assets_crore), 2) if all_assets_crore else 0

            # Group aspirants by ward
            aspirants_by_ward = {}
            for row in aspirants:
                w = row["ward"]
                if w not in aspirants_by_ward:
                    aspirants_by_ward[w] = []
                aspirants_by_ward[w].append({
                    "name": row["name"],
                    "party": row["party"],
                    "cases": int(row["cases"] or 0),
                    "assets": row["assets"] or "",
                    "assets_crore": parse_assets_crore(row["assets"] or ""),
                    "is_winner": False
                })

            # Format the output
            results = []
            for w in winners:
                ward_name = w["ward"]
                ward_aspirants = aspirants_by_ward.get(ward_name, [])
                
                winner_cases = int(w["cases"] or 0)
                winner_assets_crore = parse_assets_crore(w["assets"] or "")
                
                winner_data = {
                    "name": w["name"],
                    "party": w["party"],
                    "cases": winner_cases,
                    "assets": w["assets"] or "",
                    "assets_crore": winner_assets_crore,
                    "image": w["image"],
                    "is_winner": True
                }

                all_local_cases = [winner_cases] + [c["cases"] for c in ward_aspirants]
                all_local_assets = [winner_assets_crore] + [c["assets_crore"] for c in ward_aspirants]
                local_avg_cases = round(sum(all_local_cases) / len(all_local_cases), 2) if all_local_cases else 0
                local_avg_assets = round(sum(all_local_assets) / len(all_local_assets), 2) if all_local_assets else 0

                results.append({
                    "ward": ward_name,
                    "winner": winner_data,
                    "candidates": ward_aspirants,
                    "ward_avg": {
                        "cases": avg_cases,
                        "assets_crore": avg_assets,
                    },
                    "local_ward_avg": {
                        "cases": local_avg_cases,
                        "assets_crore": local_avg_assets,
                    },
                    "all_wards_count": total_wards,
                })

            return results
    except Exception as e:
        print(f"❌ All Candidates Fetch Error: {e}")
        return []

# ---------------------------------------------------------------------------
# GET /api/ward-stats?ward=<name>
# Returns winner, aspiring candidates, and Mumbai-wide averages for bar chart.
# All data is read from candidates_winner and candidates_aspiring DB tables.
# ---------------------------------------------------------------------------
@app.get("/api/ward-stats")
def get_ward_stats(ward: str = Query(..., description="Assembly constituency name")):
    """
    Returns structured data for the ward comparison bar chart.
    Data is served from the candidates_winner / candidates_aspiring DB tables.
    """
    try:
        with engine.connect() as conn:
            # --- 1. Resolve winner (case-insensitive fuzzy match) ---
            winner_row = conn.execute(
                text("""
                    SELECT ward, name, party, cases, assets, image
                    FROM candidates_winner
                    WHERE LOWER(ward) = LOWER(:ward)
                       OR LOWER(ward) LIKE LOWER(:partial)
                       OR LOWER(:ward) LIKE LOWER(CONCAT('%', ward, '%'))
                    LIMIT 1
                """),
                {"ward": ward, "partial": f"%{ward}%"}
            ).mappings().fetchone()

            if not winner_row:
                return {
                    "ward": ward,
                    "available": False,
                    "winner": None,
                    "candidates": [],
                    "ward_avg": {"cases": 0, "assets_crore": 0},
                    "all_wards_count": 0,
                }

            winner_key = winner_row["ward"]
            winner_cases = int(winner_row["cases"] or 0)
            winner_assets_crore = parse_assets_crore(winner_row["assets"] or "")

            winner_data = {
                "name": winner_row["name"],
                "party": winner_row["party"],
                "cases": winner_cases,
                "assets_crore": winner_assets_crore,
                "image": winner_row["image"],
                "is_winner": True,
            }

            # --- 2. Aspiring candidates for this ward ---
            aspirant_rows = conn.execute(
                text("""
                    SELECT name, party, cases, assets
                    FROM candidates_aspiring
                    WHERE ward = :ward
                """),
                {"ward": winner_key}
            ).mappings().fetchall()

            # Fall back to the default set stored under '__default__'
            if not aspirant_rows:
                aspirant_rows = conn.execute(
                    text("""
                        SELECT name, party, cases, assets
                        FROM candidates_aspiring
                        WHERE ward = '__default__'
                    """)
                ).mappings().fetchall()

            aspirants = [
                {
                    "name": r["name"],
                    "party": r["party"],
                    "cases": int(r["cases"] or 0),
                    "assets_crore": parse_assets_crore(r["assets"] or ""),
                    "is_winner": False,
                }
                for r in aspirant_rows
            ]

            # --- 3. Mumbai-wide averages via SQL aggregation ---
            avg_row = conn.execute(
                text("""
                    SELECT
                        COUNT(*) AS total,
                        AVG(CAST(NULLIF(cases, '') AS NUMERIC)) AS avg_cases
                    FROM candidates_winner
                """)
            ).mappings().fetchone()

            total_wards = int(avg_row["total"] or 0)
            avg_cases = round(float(avg_row["avg_cases"] or 0), 2)

            # Compute average assets in Python (parsing the human-readable string)
            all_asset_rows = conn.execute(
                text("SELECT assets FROM candidates_winner")
            ).scalars().fetchall()
            all_assets_crore = [parse_assets_crore(a or "") for a in all_asset_rows]
            avg_assets = round(
                sum(all_assets_crore) / len(all_assets_crore), 2
            ) if all_assets_crore else 0

        # Compute local ward averages (winner + aspirants)
        all_local_cases = [winner_data["cases"]] + [c["cases"] for c in aspirants]
        all_local_assets = [winner_data["assets_crore"]] + [c["assets_crore"] for c in aspirants]
        
        local_avg_cases = round(sum(all_local_cases) / len(all_local_cases), 2) if all_local_cases else 0
        local_avg_assets = round(sum(all_local_assets) / len(all_local_assets), 2) if all_local_assets else 0

        return {
            "ward": winner_key,
            "available": True,
            "winner": winner_data,
            "candidates": aspirants,
            "ward_avg": {
                "cases": avg_cases,
                "assets_crore": avg_assets,
            },
            "local_ward_avg": {
                "cases": local_avg_cases,
                "assets_crore": local_avg_assets,
            },
            "all_wards_count": total_wards,
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"❌ Ward Stats Error: {e}")
        raise HTTPException(status_code=500, detail="Error fetching ward stats from database.")