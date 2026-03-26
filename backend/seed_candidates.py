"""
seed_candidates.py
------------------
One-time (re-runnable) script that populates two PostgreSQL tables:

  candidates_winner   — elected MLA per ward (from HARDCODED_DATA)
  candidates_aspiring — runner-up / aspiring candidates per ward

Safe to run multiple times: uses INSERT … ON CONFLICT DO UPDATE (upsert).
Tables are created if they don't already exist.

Usage:
    cd backend
    python seed_candidates.py
"""

from sqlalchemy import create_engine, text
from data.constituencies import HARDCODED_DATA
from data.aspiring_candidates import ASPIRING_CANDIDATES, DEFAULT_ASPIRING

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/cvdb")
engine = create_engine(DATABASE_URL)

# ---------------------------------------------------------------------------
# DDL
# ---------------------------------------------------------------------------
CREATE_WINNER_TABLE = text("""
CREATE TABLE IF NOT EXISTS candidates_winner (
    ward    TEXT PRIMARY KEY,
    name    TEXT,
    party   TEXT,
    cases   TEXT,
    assets  TEXT,
    image   TEXT,
    link    TEXT,
    status  TEXT
);
""")

CREATE_ASPIRING_TABLE = text("""
CREATE TABLE IF NOT EXISTS candidates_aspiring (
    id      SERIAL PRIMARY KEY,
    ward    TEXT NOT NULL,
    name    TEXT,
    party   TEXT,
    cases   TEXT,
    assets  TEXT
);
""")

# ---------------------------------------------------------------------------
# Upsert helpers
# ---------------------------------------------------------------------------
UPSERT_WINNER = text("""
INSERT INTO candidates_winner (ward, name, party, cases, assets, image, link, status)
VALUES (:ward, :name, :party, :cases, :assets, :image, :link, :status)
ON CONFLICT (ward) DO UPDATE SET
    name   = EXCLUDED.name,
    party  = EXCLUDED.party,
    cases  = EXCLUDED.cases,
    assets = EXCLUDED.assets,
    image  = EXCLUDED.image,
    link   = EXCLUDED.link,
    status = EXCLUDED.status;
""")

# For aspiring candidates we delete + re-insert per ward so the script is
# idempotent without needing a unique constraint on (ward, name).
DELETE_ASPIRING_FOR_WARD = text("""
DELETE FROM candidates_aspiring WHERE ward = :ward;
""")

INSERT_ASPIRING = text("""
INSERT INTO candidates_aspiring (ward, name, party, cases, assets)
VALUES (:ward, :name, :party, :cases, :assets);
""")

# Store the DEFAULT_ASPIRING set under the sentinel key "__default__"
# so the API can retrieve it when a ward has no specific aspirants.
DEFAULT_WARD_KEY = "__default__"


def seed():
    with engine.begin() as conn:
        # --- Create tables ---
        conn.execute(CREATE_WINNER_TABLE)
        conn.execute(CREATE_ASPIRING_TABLE)
        print("✅ Tables ensured.")

        # --- Seed winners ---
        winner_count = 0
        for ward, data in HARDCODED_DATA.items():
            conn.execute(UPSERT_WINNER, {
                "ward":   ward,
                "name":   data.get("name", ""),
                "party":  data.get("party", ""),
                "cases":  data.get("cases", "0"),
                "assets": data.get("assets", ""),
                "image":  data.get("image", ""),
                "link":   data.get("link", ""),
                "status": data.get("status", ""),
            })
            winner_count += 1
        print(f"✅ Seeded {winner_count} winner rows into candidates_winner.")

        # --- Seed aspiring candidates ---
        aspiring_count = 0

        # Seed the per-ward data
        for ward, candidates in ASPIRING_CANDIDATES.items():
            conn.execute(DELETE_ASPIRING_FOR_WARD, {"ward": ward})
            for c in candidates:
                conn.execute(INSERT_ASPIRING, {
                    "ward":   ward,
                    "name":   c.get("name", ""),
                    "party":  c.get("party", ""),
                    "cases":  c.get("cases", "0"),
                    "assets": c.get("assets", ""),
                })
                aspiring_count += 1

        # Seed the default fallback set under the sentinel key
        conn.execute(DELETE_ASPIRING_FOR_WARD, {"ward": DEFAULT_WARD_KEY})
        for c in DEFAULT_ASPIRING:
            conn.execute(INSERT_ASPIRING, {
                "ward":   DEFAULT_WARD_KEY,
                "name":   c.get("name", ""),
                "party":  c.get("party", ""),
                "cases":  c.get("cases", "0"),
                "assets": c.get("assets", ""),
            })
            aspiring_count += 1

        print(f"✅ Seeded {aspiring_count} aspiring rows into candidates_aspiring.")
        print(f"   (includes {len(DEFAULT_ASPIRING)} default fallback rows under key '{DEFAULT_WARD_KEY}')")

    print("\n🎉 Seed complete. All candidate data is now in the database.")


if __name__ == "__main__":
    seed()
