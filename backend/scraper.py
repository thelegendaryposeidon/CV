import requests
from bs4 import BeautifulSoup
import urllib.parse
from data.constituencies import HARDCODED_DATA  # Import the Mega-Cache

def search_candidate(constituency_name, state, level="assembly"):
    """
    Hybrid Scraper: Mega-Cache Lookup + Web Fallback
    """
    print(f"🕵️‍♀️ Scouting for leader of: {constituency_name} ({state})...")
    
    clean_name = constituency_name.strip()
    
    # --- CHECK 1: Mega Cache Lookup (Case Insensitive) ---
    # Try exact match
    if clean_name in HARDCODED_DATA:
        print(f"✅ Found in Mega Cache: {clean_name}")
        return HARDCODED_DATA[clean_name]

    # Try case-insensitive / partial match
    for key in HARDCODED_DATA:
        # Check if "Kalyan Rural" matches "Kalyan Rural (SC)" or "kalyan rural"
        if key.lower() == clean_name.lower() or key.lower() in clean_name.lower():
            print(f"✅ Fuzzy match: '{clean_name}' -> '{key}'")
            return HARDCODED_DATA[key]

    # --- CHECK 2: Live Scraping (Fallback) ---
    print("⚠️ Not in Cache, attempting Live Search...")
    try:
        query = f"site:myneta.info {constituency_name} Maharashtra 2024 winner"
        search_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
        headers = { "User-Agent": "Mozilla/5.0" }
        resp = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        target_link = None
        for link in soup.find_all('a', href=True):
            if "myneta.info" in link['href']:
                target_link = link['href']
                break
        
        if target_link:
            if "uddg=" in target_link:
                target_link = urllib.parse.unquote(target_link.split("uddg=")[1].split("&")[0])
                
            return {
                "name": "Click for Details", 
                "party": "Unknown", 
                "link": target_link,
                "status": "Success (Live)"
            }

    except Exception as e:
        print(f"❌ Scraping Error: {e}")

    return {"name": "Data Not Found", "party": "N/A", "link": "#"}

if __name__ == "__main__":
    # Test a few
    print(search_candidate("Dahanu", "Maharashtra"))
    print(search_candidate("Shahapur", "Maharashtra"))