# CandidateValidate - Project Context & Architecture

This document is designed to provide complete context and implementation details for future LLM handovers. It outlines the project's vision, tech stack, architecture, and history.

## 1. Project Overview & Vision
CandidateValidate is a web application designed to empower voters by providing them with instant access to their political candidates' backgrounds, specifically focusing on criminal records and declared assets. The goal is to bring transparency and enable informed voting. The current demo is specifically built around the Maharashtra assembly constituencies.

## 2. Tech Stack Setup
- **Frontend**: Next.js 16 (App Router), React 19, TypeScript, Tailwind CSS v3, MapLibre GL JS (for fast vector mapping), Recharts (for data visualization), Lucide React (icons).
- **Backend**: Python 3, FastAPI, SQLAlchemy (Core).
- **Database**: PostgreSQL with PostGIS extension for geospatial queries.
- **AI Integration**: Google Generative AI (Gemini Pro) for intuitive candidate profile analysis of affidavits.
- **Data Pipeline**: Python scripts (`geopandas`, `requests`, `BeautifulSoup`) to load GeoJSON/Shapefiles and scrape/seed candidate data.

## 3. Project Structure
```text
candidatevalidate/
├── frontend/                     # Next.js Application
│   ├── app/
│   │   ├── layout.tsx            # Global layout (Inter font, globals.css)
│   │   ├── page.tsx              # Landing page with hero, features, and map preview
│   │   └── map/page.tsx          # Main map application route (guarded by BetaWarningDialog)
│   ├── components/               # React Components
│   │   ├── MapInterface.tsx      # Core map logic, searching, ward details (MapLibre)
│   │   ├── WardComparisonChart.tsx # Recharts-based bar chart comparing candidates
│   │   ├── AnalysisModal.tsx     # Displays AI verdict from Gemini
│   │   ├── BetaWarningDialog.tsx # Disclaimer shown before entering the map
│   │   └── partyLogos.ts         # Regex mapping of party names to local SVGs
│   └── public/                   # Static assets (logo.png, party-logos/)
└── backend/                      # FastAPI Application
    ├── main.py                   # Core API server (7 main endpoints)
    ├── load_maps.py              # Script to push GeoJSON/Shapefiles to PostGIS
    ├── seed_candidates.py        # Script to upsert winners/aspirants into DB
    ├── generate_mh_data.py       # Script to auto-generate missing constituency data
    ├── scraper.py                # Fallback web scraper for myneta.info
    ├── maps_data/                # Raw geospatial files (India_AC.shp, etc.)
    └── data/
        ├── constituencies.py     # Hardcoded mega-cache of winner MLAs
        └── aspiring_candidates.py# Hardcoded aspiring candidates per ward
```

## 4. Key Features Implemented
1. **Interactive Geospatial Map**: Renders Maharashtra constituencies using MapLibre GL. Users can click on the map to query the exact ward using PostGIS `ST_Contains`.
2. **Hybrid Search System**: Users can toggle between:
   - *Ward Search*: Fuzzy searches through GeoJSON features and flies to the ward.
   - *Candidate Search*: Hits the backend to search both winner and aspiring candidate tables, displaying matches in a dropdown with candidate/party summaries.
3. **Candidate Information Card**: Displays the MLA's name, party, criminal cases, declared assets, and photo. Includes a deep link to official myneta.info affidavits.
4. **Aspiring Candidates List**: Shows runner-ups/other candidates for the ward directly inside the info card.
5. **Data Visualization (Ward Comparison)**: A `Recharts` bar chart comparing the winner and aspiring candidates' cases and assets against the Mumbai-wide averages.
6. **AI Analysis**: Integrates Gemini Pro to read the chosen candidate's criminal and financial data, outputting a strict JSON verdict ("Safe", "Caution", "Risky") with red and green flags.
7. **Beta Warning Dialog**: A session-storaged gatekeeper that warns users the data is in beta and requires them to accept the disclaimer before accessing the interactive map.
8. **Dynamic Party Logos**: `partyLogos.ts` maps party strings to SVG logos using regex (e.g., Shiva Sena (UBT), BJP, NCP (SP), etc.), which are displayed in search results and candidate cards.

## 5. Database Schema & Data Flow
The setup runs on a local PostgreSQL instance (`localhost:5432/cvdb`).

### Tables:
- `constituencies_ac`: Assembly constituencies (loaded via `load_maps.py` from Shapefile).
- `constituencies_pc`: Parliamentary constituencies.
- `candidates_winner`: Stores elected MLAs (PK: `ward`, cols: `name`, `party`, `cases`, `assets`, `image`, `link`, `status`).
- `candidates_aspiring`: Stores other candidates (PK: `id`, cols: `ward`, `name`, `party`, `cases`, `assets`). Contains a `__default__` ward for fallback options.

### Data Scripts:
1. `load_maps.py`: Uses `geopandas` to push `India_AC.shp` to PostGIS.
2. `generate_mh_data.py`: Identifies ACs in PostGIS missing from Python hardcoded files and generates realistic, region-aware mock data to fill gaps.
3. `seed_candidates.py`: Upserts data from Python dicts (`data/constituencies.py` and `data/aspiring_candidates.py`) into the `candidates_winner` and `candidates_aspiring` Postgres tables.

## 6. API Endpoints (`backend/main.py`)
- `GET /api/states`: Returns distinct states from `constituencies_ac`.
- `GET /api/shapes?state=...`: Returns GeoJSON features for the specified state.
- `POST /api/vicinity`: Accepts `{latitude, longitude}`. Uses `ST_Contains` to find the ward, then fetches the winner from `candidates_winner`. Returns MP, MLA, and candidate details.
- `POST /api/analyze`: Accepts candidate stats. Prompts Gemini Pro to return a JSON summary, flags, and verdict.
- `GET /api/search-candidates?q=...`: Searches both `candidates_winner` and `candidates_aspiring` using `ILIKE %q%` returning up to 10 unified results.
- `GET /api/ward-stats?ward=...`: Returns structured data for the comparison chart: the winner, aspirants list, and global averages (which are calculated via SQL and Python conversion functions `parse_assets_crore`).

## 7. Recent Refactors & Milestones (History)
Based on conversation history, the project was built iteratively with the following major milestones:
- **Project Reset**: Clean slate start to build the core architecture.
- **Database Migration**: Migrated hardcoded python data (`HARDCODED_DATA`, `ASPIRING_CANDIDATES`) into PostgreSQL (`candidates_winner`, `candidates_aspiring`). Refactored `main.py` to serve from the DB interface.
- **Candidate Data Expansion**: Generated realistic data for the rest of Maharashtra to cover coverage gaps, and increased aspirant limits. Added Mumbai-wide average calculations for cases/assets.
- **UI & UX Enhancements**:
  - Replaced generic candidate layout icons with specific political party logos.
  - Implemented the `BetaWarningDialog` to guard the map page.
  - Added the dual-mode ("Ward" vs "Candidate") inline search bar.
  - Extracted Recharts graph logic into `WardComparisonChart.tsx` for cleaner component hierarchy.
- **Cleanup**: Removed boilerplate Next.js assets, optimized unused imports, and streamlined package dependencies.

## 8. Current State & Known Edge Cases
- **Scraper Fallback**: If an MLA for a ward is missing in the DB, `main.py` falls back to `scraper.py` which attempts a DuckDuckGo search for myneta.info links. This is a fragile fallback and is largely bypassed now that `generate_mh_data.py` flushed out the database.
- **Asset Parsing**: Assets are currently stored as strings (e.g., "Rs 5 Crore+", "Rs 80 Lakh+"). The backend uses a regex parser (`parse_assets_crore`) to convert these to numeric Crore values dynamically for the charts.
- **API Keys**: Requires `GEMINI_API_KEY` in environment variables for the AI Analysis feature to function dynamically. If absent, it gracefully returns a hardcoded fallback analysis.
