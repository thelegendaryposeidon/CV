"""
generate_mh_data.py
-------------------
Queries PostgreSQL for all Maharashtra Assembly Constituency names,
identifies those NOT yet in data/constituencies.py, and generates
context-sensitive, realistic candidate entries for each.

The generated data uses:
 - Region-aware party distributions (Vidarbha, Marathwada, Western MH, etc.)
 - Common Maharashtrian surnames and first names
 - Realistic asset & criminal-case distributions
 - Parties from the actual 2024 MH legislative landscape

Usage:
    cd backend
    python generate_mh_data.py
"""

import random
import textwrap
from sqlalchemy import create_engine, text
from data.constituencies import HARDCODED_DATA
from data.aspiring_candidates import ASPIRING_CANDIDATES

import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost:5432/cvdb")
engine = create_engine(DATABASE_URL)

# ---------------------------------------------------------------------------
# Maharashtra political context
# ---------------------------------------------------------------------------

# Major parties in the 2024 MH Assembly elections
# Mahayuti (ruling): BJP, Shiv Sena (Eknath Shinde), NCP (Ajit Pawar)
# MVA (opposition):  Congress, Shiv Sena (UBT), NCP (Sharad Pawar)
# Others:            MNS, VBA, AIMIM, BSP, SP, PWP, CPI(M), Independent

PARTIES_RULING = ["BJP", "Shiv Sena", "NCP"]
PARTIES_OPPOSITION = ["Congress", "Shiv Sena (UBT)", "NCP (Sharad Pawar)"]
PARTIES_MINOR = ["MNS", "VBA", "AIMIM", "BSP", "SP", "PWP", "CPI(M)", "Independent",
                 "Bahujan Vikas Aghadi", "Peasants and Workers Party", "AAP",
                 "Republican Party of India (A)", "Swabhimani Paksha"]

# Region-based party weight tuning
# In 2024, Mahayuti swept most regions, but opposition held pockets
def get_region(ac_name_upper):
    """Rough region mapping based on known AC names."""
    vidarbha = ["NAGPUR", "WARDHA", "AMRAVATI", "AKOLA", "YAVATMAL", "CHANDRAPUR",
                "BHANDARA", "GONDIA", "GADCHIROLI", "BULDHANA", "WASHIM", "HINGANGHAT",
                "ARVI", "KATOL", "SAONER", "UMRED", "RAMTEK", "KAMTHI", "HINGNA",
                "MORSHI", "ACHALPUR", "MELGHAT", "DARYAPUR", "BALAPUR", "RISOD",
                "PUSAD", "DIGRAS", "ARNI", "WANI", "RALEGAON", "CHIMUR", "BRAMHAPURI",
                "SAKOLI", "TIRORA", "TUMSAR", "DEOLI", "SINDKHED RAJA", "CHIKHLI",
                "MEHKAR", "KHAMGAON", "JALGAON JAMOD", "MALKAPUR", "NANDGAON KHANDESHWAR"]

    marathwada = ["AURANGABAD", "CHHATRAPATI SAMBHAJINAGAR", "JALNA", "PARBHANI",
                  "HINGOLI", "NANDED", "LATUR", "OSMANABAD", "BEED", "SILLOD",
                  "PHULAMBRI", "KANNAD", "VAIJAPUR", "GANGAPUR", "PAITHAN",
                  "GHANSAWANGI", "BHOKARDAN", "JINTUR", "PURNA", "GANGAKHED",
                  "PATHRI", "HADGAON", "KINWAT", "BHOKAR", "DEGLUR", "MUKHED",
                  "BASMATH", "KALAMNURI", "DHARASHIV", "PARANDA", "KALAMB", "TULJAPUR",
                  "UDGIR", "AHMEDPUR", "NILANGA", "AUSA", "SHIRUR KASAR",
                  "GEVRAI", "MAJALGAON", "PARLI", "AMBAJOGAI", "NAIGAON",
                  "LOHA", "MUDKHED"]

    western_mh = ["PUNE", "SATARA", "SANGLI", "KOLHAPUR", "SOLAPUR",
                  "BARAMATI", "INDAPUR", "DAUND", "PURANDAR", "BHOR", "MAVAL",
                  "PIMPRI", "CHINCHWAD", "BHOSARI", "KOTHRUD", "SHIVAJINAGAR",
                  "KASBA PETH", "PARVATI", "HADAPSAR", "WADGAON SHERI",
                  "KHADAKWASLA", "SHIRUR", "KARAD", "KOREGAON", "PATAN",
                  "WAIN", "MAN", "KHATAV", "SHAHUWADI", "CHANDGAD", "RADHANAGARI",
                  "KAGAL", "HATKANANGLE", "ICHALKARANJI", "SHIROL", "KARVIR",
                  "MIRAJ", "SANGLI", "ISLAMPUR", "SHIRALA", "PALUS KADEGAON",
                  "KHANAPUR", "TASGAON KAVATHE MAHANKAL", "JATH", "ATPADI",
                  "MOHOL", "MADHA", "BARSHI", "SOLAPUR NORTH", "SOLAPUR SOUTH",
                  "SOLAPUR CENTRAL", "AKKALKOT", "PANDHARPUR", "MALSHIRAS",
                  "SANGOLA", "MANGALVEDHA", "JUNNAR", "AMBEGAON", "MANCHAR"]

    north_mh = ["NASHIK", "DHULE", "JALGAON", "NANDURBAR", "AHMEDNAGAR",
                "NASHIK EAST", "NASHIK WEST", "NASHIK CENTRAL", "DEOLALI",
                "IGATPURI", "SINNAR", "NIPHAD", "DINDORI", "KALWAN",
                "MALEGAON OUTER", "MALEGAON CENTRAL", "BAGLAN",
                "CHALISGAON", "PACHORA", "JALGAON CITY", "JAMNER",
                "MUKTAINAGAR", "BODWAD", "AMALNER", "CHOPDA", "RAVER",
                "ERANDOL", "BHUSAWAL", "YAWAL",
                "DHULE CITY", "DHULE RURAL", "SINDKHEDA", "SHIRPUR",
                "NANDURBAR", "NAWAPUR", "SHAHADA", "TALODA", "AKKALKUWA",
                "SHRIRAMPUR", "NEVASA", "RAHURI", "PARNER", "AHMEDNAGAR CITY",
                "SHEVGAON", "PATHARDI", "KOPARGAON", "SANGAMNER", "AKOLE",
                "SHRIGONDA", "KARJAT JAMKHED", "RAHATA"]

    konkan = ["RATNAGIRI", "SINDHUDURG", "RAIGAD", "DAPOLI", "GUHAGAR",
              "CHIPLUN", "RAJAPUR", "KANKAVLI", "KUDAL", "SAWANTWADI",
              "PEN", "ALIBAUG", "SHRIVARDHAN", "MAHAD", "SUDHAGAD",
              "URAN", "KARJAT"]

    for name_part in vidarbha:
        if name_part in ac_name_upper:
            return "VIDARBHA"
    for name_part in marathwada:
        if name_part in ac_name_upper:
            return "MARATHWADA"
    for name_part in western_mh:
        if name_part in ac_name_upper:
            return "WESTERN_MH"
    for name_part in north_mh:
        if name_part in ac_name_upper:
            return "NORTH_MH"
    for name_part in konkan:
        if name_part in ac_name_upper:
            return "KONKAN"
    return "GENERAL"

def pick_winner_party(region):
    """Region-aware party selection for winner (reflecting 2024 Mahayuti sweep)."""
    weights = {
        "VIDARBHA":    {"BJP": 40, "Shiv Sena": 15, "NCP": 10, "Congress": 20, "Shiv Sena (UBT)": 8, "NCP (Sharad Pawar)": 5, "Independent": 2},
        "MARATHWADA":  {"BJP": 30, "Shiv Sena": 20, "NCP": 15, "Congress": 15, "Shiv Sena (UBT)": 10, "NCP (Sharad Pawar)": 5, "AIMIM": 3, "Independent": 2},
        "WESTERN_MH":  {"BJP": 35, "Shiv Sena": 10, "NCP": 20, "Congress": 15, "Shiv Sena (UBT)": 5, "NCP (Sharad Pawar)": 10, "Independent": 5},
        "NORTH_MH":    {"BJP": 35, "Shiv Sena": 15, "NCP": 15, "Congress": 15, "Shiv Sena (UBT)": 8, "NCP (Sharad Pawar)": 7, "Independent": 5},
        "KONKAN":      {"BJP": 25, "Shiv Sena": 25, "NCP": 10, "Congress": 10, "Shiv Sena (UBT)": 15, "NCP (Sharad Pawar)": 5, "Independent": 5, "PWP": 5},
        "GENERAL":     {"BJP": 35, "Shiv Sena": 18, "NCP": 12, "Congress": 15, "Shiv Sena (UBT)": 10, "NCP (Sharad Pawar)": 5, "Independent": 5},
    }
    w = weights.get(region, weights["GENERAL"])
    parties = list(w.keys())
    wts = list(w.values())
    return random.choices(parties, weights=wts, k=1)[0]

# ---------------------------------------------------------------------------
# Realistic Maharashtrian names
# ---------------------------------------------------------------------------
MALE_FIRST = [
    "Rajesh", "Suresh", "Mahesh", "Ganesh", "Ramesh", "Dinesh", "Sanjay", "Vijay",
    "Anil", "Sunil", "Nitin", "Sachin", "Prakash", "Ashok", "Dilip", "Vinod",
    "Mohan", "Kishore", "Deepak", "Prashant", "Balasaheb", "Chandrakant", "Datta",
    "Eknath", "Govind", "Harish", "Jayant", "Kashinath", "Laxman", "Mahadev",
    "Narayan", "Pandurang", "Raghunath", "Shivaji", "Tanaji", "Uddhav", "Vasant",
    "Yashwant", "Bhimrao", "Shankar", "Dattatray", "Ravi", "Ajit", "Babanrao",
    "Vishwas", "Sambhaji", "Satyajit", "Abhijit", "Omprakash", "Dnyaneshwar",
    "Vitthal", "Baban", "Sandip", "Rohit", "Amol", "Nilesh", "Tushar",
    "Mangesh", "Yogesh", "Girish", "Kiran", "Pravin", "Vilas", "Shrihari",
    "Nana", "Ramdas", "Bharat", "Prabhakar", "Subhash", "Madhukar", "Sadashiv",
]

FEMALE_FIRST = [
    "Sushma", "Sunita", "Anita", "Rekha", "Savita", "Kavita", "Shobha", "Mangala",
    "Lata", "Sneha", "Pooja", "Priya", "Neha", "Swati", "Jyoti", "Asha", "Bharati",
    "Vandana", "Supriya", "Rohini", "Archana", "Nirmala", "Varsha", "Pushpa",
    "Suvarna", "Meena", "Radha", "Shubhangi", "Indira", "Ujwala", "Manisha",
    "Deepali", "Smita", "Pramila", "Leela", "Vaishali", "Chitra", "Durga",
]

SURNAMES = [
    "Patil", "Deshmukh", "Jadhav", "More", "Shinde", "Pawar", "Chavan", "Bhosale",
    "Gaikwad", "Kamble", "Sawant", "Kadam", "Mane", "Salvi", "Kokate", "Thorat",
    "Nikam", "Londhe", "Kale", "Khedkar", "Kshirsagar", "Joshi", "Kulkarni",
    "Deshpande", "Phadke", "Gokhale", "Kelkar", "Wagh", "Thakur", "Mhatre",
    "Kolhe", "Bhoir", "Ghule", "Tupe", "Suryawanshi", "Rathod", "Bhalerao",
    "Yadav", "Pardeshi", "Gavhane", "Borse", "Shelar", "Dahake", "Autade",
    "Phad", "Ingale", "Pachpute", "Khandare", "Takle", "Udawant", "Gore",
    "Waghmare", "Sonawane", "Dhole", "Gawande", "Borkar", "Meshram", "Raut",
    "Dhawale", "Nandanwar", "Bankar", "Gharat", "Gavit", "Naik", "Dalvi",
]

def random_name():
    """Generate a realistic Maharashtrian name."""
    if random.random() < 0.25:
        first = random.choice(FEMALE_FIRST)
    else:
        first = random.choice(MALE_FIRST)
    return f"{first} {random.choice(SURNAMES)}"

def random_cases(is_winner=False):
    """Generate realistic criminal case count. Winners tend to have more cases (sad reality)."""
    if is_winner:
        r = random.random()
        if r < 0.35: return "0"
        if r < 0.55: return str(random.randint(1, 2))
        if r < 0.80: return str(random.randint(3, 6))
        return str(random.randint(7, 15))
    else:
        r = random.random()
        if r < 0.45: return "0"
        if r < 0.70: return str(random.randint(1, 2))
        if r < 0.90: return str(random.randint(3, 5))
        return str(random.randint(6, 10))

def random_assets(is_winner=False):
    """Generate realistic declared assets string."""
    if is_winner:
        r = random.random()
        if r < 0.05:
            val = random.choice([3, 5, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80])
            return f"Rs {val} Lakh+"
        elif r < 0.60:
            val = random.randint(1, 20)
            return f"Rs {val} Crore+"
        elif r < 0.85:
            val = random.randint(20, 80)
            return f"Rs {val} Crore+"
        else:
            val = random.randint(80, 300)
            return f"Rs {val} Crore+"
    else:
        r = random.random()
        if r < 0.20:
            val = random.choice([25, 35, 45, 50, 60, 70, 80, 90])
            return f"Rs {val} Lakh+"
        elif r < 0.70:
            val = random.randint(1, 10)
            return f"Rs {val} Crore+"
        elif r < 0.90:
            val = random.randint(10, 40)
            return f"Rs {val} Crore+"
        else:
            val = random.randint(40, 120)
            return f"Rs {val} Crore+"

def pick_aspirant_parties(winner_party, region):
    """Pick 6 varied aspirant parties, ensuring the winner's party isn't dominant."""
    all_parties = (PARTIES_RULING + PARTIES_OPPOSITION + PARTIES_MINOR)
    # Remove the winner's party so we don't duplicate it too much
    pool = [p for p in all_parties if p != winner_party]
    # Add one candidate from the winner's party (a rebel or factional candidate)
    chosen = [winner_party] if random.random() < 0.3 else []
    # Fill the rest
    while len(chosen) < 6:
        p = random.choice(pool)
        if chosen.count(p) < 2:  # max 2 from same party
            chosen.append(p)
    random.shuffle(chosen)
    return chosen[:6]


def generate_winner_entry(ac_name, region):
    """Generate a winner dict for a constituency."""
    party = pick_winner_party(region)
    name = random_name()
    cases = random_cases(is_winner=True)
    assets = random_assets(is_winner=True)
    # Use ui-avatars for placeholder images
    party_color = {
        "BJP": "ff9933", "Shiv Sena": "ff9933", "NCP": "008000",
        "Congress": "0066cc", "Shiv Sena (UBT)": "ff6600",
        "NCP (Sharad Pawar)": "004d00", "Independent": "808080",
        "AIMIM": "006400", "PWP": "cc0000", "MNS": "ff4500",
    }.get(party, "808080")

    encoded_name = name.replace(" ", "+")
    return {
        "name": name,
        "party": party,
        "cases": cases,
        "assets": assets,
        "image": f"https://ui-avatars.com/api/?name={encoded_name}&background={party_color}&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success",
    }


def generate_aspirants(ac_name, winner_party, region):
    """Generate 6 aspirant candidates for a constituency."""
    parties = pick_aspirant_parties(winner_party, region)
    aspirants = []
    for party in parties:
        aspirants.append({
            "name": random_name(),
            "party": party,
            "cases": random_cases(is_winner=False),
            "assets": random_assets(is_winner=False),
        })
    return aspirants


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------
def main():
    random.seed(42)  # Reproducible output

    # 1. Query all Maharashtra AC names from PostGIS
    with engine.connect() as conn:
        rows = conn.execute(
            text("SELECT DISTINCT ac_name FROM constituencies_ac WHERE st_name = 'MAHARASHTRA' ORDER BY ac_name;")
        ).fetchall()

    db_ac_names = [row[0] for row in rows if row[0]]
    print(f"📊 Found {len(db_ac_names)} ACs in PostGIS for MAHARASHTRA")

    # 2. Identify which ones are NOT in the current data
    existing_keys_lower = {k.lower() for k in HARDCODED_DATA.keys()}
    missing = [name for name in db_ac_names if name.lower() not in existing_keys_lower]
    print(f"🔍 {len(missing)} ACs missing from constituencies.py")

    if not missing:
        print("✅ All ACs already covered! Nothing to generate.")
        return

    # 3. Generate data
    new_winners = {}
    new_aspirants = {}

    for ac_name in missing:
        region = get_region(ac_name.upper())
        winner = generate_winner_entry(ac_name, region)
        new_winners[ac_name] = winner
        new_aspirants[ac_name] = generate_aspirants(ac_name, winner["party"], region)

    # 4. Append to constituencies.py
    print(f"\n📝 Appending {len(new_winners)} new winner entries to data/constituencies.py ...")

    with open("data/constituencies.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Find the closing brace of HARDCODED_DATA
    # We'll insert before the last "}" that closes the dict
    last_brace = content.rfind("}")
    if last_brace == -1:
        print("❌ Could not find closing brace in constituencies.py")
        return

    new_entries_str = "\n    # --- AUTO-GENERATED: REST OF MAHARASHTRA ---\n"
    for ward, data in new_winners.items():
        new_entries_str += f'    "{ward}": {{\n'
        new_entries_str += f'        "name": "{data["name"]}", "party": "{data["party"]}", "cases": "{data["cases"]}", "assets": "{data["assets"]}",\n'
        new_entries_str += f'        "image": "{data["image"]}",\n'
        new_entries_str += f'        "link": "{data["link"]}",\n'
        new_entries_str += f'        "status": "{data["status"]}"\n'
        new_entries_str += '    },\n'

    new_content = content[:last_brace] + new_entries_str + content[last_brace:]

    with open("data/constituencies.py", "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ constituencies.py updated ({len(HARDCODED_DATA) + len(new_winners)} total entries)")

    # 5. Append to aspiring_candidates.py
    print(f"📝 Appending {len(new_aspirants)} new aspirant ward entries to data/aspiring_candidates.py ...")

    with open("data/aspiring_candidates.py", "r", encoding="utf-8") as f:
        asp_content = f.read()

    # Find the closing brace of ASPIRING_CANDIDATES dict
    # Look for the closing "}" of the ASPIRING_CANDIDATES dict (before DEFAULT_ASPIRING)
    marker = "}\n\n# Default aspiring"
    marker_pos = asp_content.find(marker)
    if marker_pos == -1:
        # Try alternative
        marker = "}\n\n# Default"
        marker_pos = asp_content.find(marker)

    if marker_pos == -1:
        print("❌ Could not find ASPIRING_CANDIDATES closing point in aspiring_candidates.py")
        return

    new_asp_str = "\n    # --- AUTO-GENERATED: REST OF MAHARASHTRA ---\n"
    for ward, candidates in new_aspirants.items():
        new_asp_str += f'    "{ward}": [\n'
        for c in candidates:
            new_asp_str += f'        {{"name": "{c["name"]}", "party": "{c["party"]}", "cases": "{c["cases"]}", "assets": "{c["assets"]}"}},\n'
        new_asp_str += '    ],\n'

    new_asp_content = asp_content[:marker_pos] + new_asp_str + asp_content[marker_pos:]

    with open("data/aspiring_candidates.py", "w", encoding="utf-8") as f:
        f.write(new_asp_content)

    print(f"✅ aspiring_candidates.py updated ({len(ASPIRING_CANDIDATES) + len(new_aspirants)} total ward entries)")
    print(f"\n🎉 Generation complete! Now run: python seed_candidates.py")


if __name__ == "__main__":
    main()
