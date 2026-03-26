import geopandas as gpd
from sqlalchemy import create_engine
import os

# Database Connection
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/cvdb")
engine = create_engine(DATABASE_URL)

def load_data():
    print("🚀 Starting Data Load...")

    # --- PART 1: LOAD MPs (GeoJSON) ---
    # UPDATED FILENAME based on your screenshot
    pc_file = "maps_data/india_pc_2019_simplified.geojson" 
    
    if os.path.exists(pc_file):
        print(f"Reading {pc_file} (GeoJSON)...")
        gdf_pc = gpd.read_file(pc_file)
        
        # Standardize columns to lowercase
        gdf_pc.columns = [c.lower() for c in gdf_pc.columns]
        
        print("Pushing MPs to DB... (Fast)")
        gdf_pc.to_postgis('constituencies_pc', engine, if_exists='replace', index=False)
        print("✅ MPs Loaded Successfully!")
    else:
        print(f"❌ File not found: {pc_file}")


    # --- PART 2: LOAD MLAs (Shapefile) ---
    # This points to the main .shp file. Python will auto-detect the others (.shx, .dbf)
    ac_file = "maps_data/India_AC.shp" 
    
    if os.path.exists(ac_file):
        print(f"Reading {ac_file} (Shapefile)...")
        gdf_ac = gpd.read_file(ac_file)
        
        # Standardize columns to lowercase
        gdf_ac.columns = [c.lower() for c in gdf_ac.columns]
        
        print("Pushing MLAs to DB... (This will take 1-2 mins)")
        gdf_ac.to_postgis('constituencies_ac', engine, if_exists='replace', index=False)
        print("✅ MLAs Loaded Successfully!")
    else:
        print(f"❌ File not found: {ac_file}")

if __name__ == "__main__":
    load_data()