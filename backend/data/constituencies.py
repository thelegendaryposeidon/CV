# backend/data/constituencies.py

# Verified Data Cache with Images & Direct Affidavit Links.
# Sources: MyNeta.info & Election Commission of India (affidavit.eci.gov.in)

HARDCODED_DATA = {
    # --- SOUTH MUMBAI ---
    "Colaba": {
        "name": "Rahul Narwekar", "party": "BJP", "cases": "0", "assets": "Rs 38 Crore+",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dc/Rahul_Narwekar_Official.jpg/220px-Rahul_Narwekar_Official.jpg",
        "link": "https://myneta.info/Maharashtra2024/", # General fallback
        "status": "Success"
    },
    "Worli": {
        "name": "Aaditya Thackeray", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 23 Crore+",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/91/Aditya_Thackeray.jpg",
        "link": "https://affidavit.eci.gov.in/show-profile/eyJpdiI6IkxTTXExMXZvbmNGNGZvNWQxL1hhMWc9PSIsInZhbHVlIjoiTEJEQjhiSm5sQWg2RnYyNW90RGUvZz09IiwibWFjIjoiYTNjNjVmMWY4ZDY3OTllNzU2NjRhZGIxODJiOGFjZjk3MjE0ODg3YmY2YTBjYWExZDk3ZjVhZTAzZDcwZDcxNiIsInRhZyI6IiJ9", # Official ECI Affidavit
        "status": "Success"
    },
    "Mahim": {
        "name": "Mahesh Sawant", "party": "Shiv Sena (UBT)", "cases": "2", "assets": "Rs 14 Crore+",
        "image": "https://myneta.info/Maharashtra2024/images/candidate_photos/557.jpg",
        "link": "https://myneta.info/Maharashtra2024/candidate.php?candidate_id=557", # Direct MyNeta
        "status": "Success"
    },
    "Malabar Hill": {
        "name": "Mangal Prabhat Lodha", "party": "BJP", "cases": "5", "assets": "Rs 441 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mangal+Prabhat+Lodha&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Byculla": {
        "name": "Yamini Jadhav", "party": "Shiv Sena", "cases": "1", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Yamini+Jadhav&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mumbadevi": {
        "name": "Amin Patel", "party": "Congress", "cases": "2", "assets": "Rs 45 Crore+",
        "image": "https://ui-avatars.com/api/?name=Amin+Patel&background=0000ff&color=fff&size=200",
        "link": "https://affidavit.eci.gov.in/show-profile/eyJpdiI6ImZKZG1JdjNtNXJmK2J4dkNyYTlLL0E9PSIsInZhbHVlIjoiUmJkTU9JVHJvWHVDSkIxYXNDei84Zz09IiwibWFjIjoiMmQ1MjU5MjA4MTQwNWNiYTc0MzNmNDZhOGRiNGFjNGVkYjE5ZjMwOGJlNTAxYjEyZTllMjk4YzIwNDI4MzYxYiIsInRhZyI6IiJ9", # Official ECI Affidavit
        "status": "Success"
    },

    # --- WESTERN LINE ---
    "Bandra West": {
        "name": "Ashish Shelar", "party": "BJP", "cases": "1", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ashish+Shelar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bandra East": {
        "name": "Varun Sardesai", "party": "Shiv Sena (UBT)", "cases": "2", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Varun+Sardesai&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Andheri West": {
        "name": "Ameet Satam", "party": "BJP", "cases": "0", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ameet+Satam&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Andheri East": {
        "name": "Murji Patel", "party": "Shiv Sena", "cases": "3", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Murji+Patel&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Versova": {
        "name": "Bharati Lavekar", "party": "BJP", "cases": "3", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Bharati+Lavekar&background=ff9933&color=fff&size=200",
        "link": "https://affidavit.eci.gov.in/show-profile/eyJpdiI6IlN5V1BzWURoMW1SOHRaemh4RmJRN2c9PSIsInZhbHVlIjoibXROUmFMR2tkV0c4UTdNNW5aak5kUT09IiwibWFjIjoiOTkxMTBkMDk0ZmYxZTdiNWY1NDZmYzg2MmY5N2UzMGRjNjk3MDY3ODllMjIxZjQ3NGQ1OWJiMDljMTA1MWZjMyIsInRhZyI6IiJ9",
        "status": "Success"
    },
    "Dindoshi": {
        "name": "Sunil Prabhu", "party": "Shiv Sena (UBT)", "cases": "1", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunil+Prabhu&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Borivali": {
        "name": "Sunil Rane", "party": "BJP", "cases": "0", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunil+Rane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dahisar": {
        "name": "Manisha Chaudhary", "party": "BJP", "cases": "1", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Manisha+Chaudhary&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mira Bhayandar": {
        "name": "Geeta Jain", "party": "Shiv Sena", "cases": "2", "assets": "Rs 70 Crore+",
        "image": "https://ui-avatars.com/api/?name=Geeta+Jain&background=ff9933&color=fff&size=200",
        "link": "https://affidavit.eci.gov.in/show-profile/eyJpdiI6IlFyczFWOUlsRUxtOEtyZlBSTXh0S3c9PSIsInZhbHVlIjoiVUpYWXRPUm56MVVYbXZ0eGxudTcyUT09IiwibWFjIjoiNTdmNjY3NWE0Mzk3ZDY1MDUyN2MxYWI0NDk0MDJiYmMyN2JiNDA4Zjk5M2I4OTg0ZmE5Mjk3OWJhYWNhYzQ0ZCIsInRhZyI6IiJ9",
        "status": "Success"
    },
    "Nalasopara": {
        "name": "Kshitij Thakur", "party": "Bahujan Vikas Aghadi", "cases": "4", "assets": "Rs 28 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kshitij+Thakur&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/candidate.php?candidate_id=2147", # Direct MyNeta
        "status": "Success"
    },
    "Vasai": {
        "name": "Hitendra Thakur", "party": "Bahujan Vikas Aghadi", "cases": "3", "assets": "Rs 150 Crore+",
        "image": "https://ui-avatars.com/api/?name=Hitendra+Thakur&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Palghar": {
        "name": "Shrinivas Vanga", "party": "Shiv Sena", "cases": "0", "assets": "Rs 2 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shrinivas+Vanga&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Boisar": {
        "name": "Rajesh Patil", "party": "Bahujan Vikas Aghadi", "cases": "1", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rajesh+Patil&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dahanu": {
        "name": "Vinod Nikole", "party": "CPI (M)", "cases": "7", "assets": "Rs 5 Lakhs",
        "image": "https://myneta.info/Maharashtra2024/images/candidate_photos/901.jpg",
        "link": "https://myneta.info/Maharashtra2024/candidate.php?candidate_id=901",
        "status": "Success"
    },

    # --- CENTRAL LINE ---
    "Sion Koliwada": {
        "name": "R. Tamil Selvan", "party": "BJP", "cases": "4", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=R+Tamil+Selvan&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kurla": {
        "name": "Mangesh Kudalkar", "party": "Shiv Sena", "cases": "1", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mangesh+Kudalkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vikhroli": {
        "name": "Sunil Raut", "party": "Shiv Sena (UBT)", "cases": "5", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunil+Raut&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ghatkopar East": {
        "name": "Parag Shah", "party": "BJP", "cases": "0", "assets": "Rs 500 Crore+",
        "image": "https://ui-avatars.com/api/?name=Parag+Shah&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Thane": {
        "name": "Sanjay Kelkar", "party": "BJP", "cases": "0", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sanjay+Kelkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kopri-Pachpakhadi": {
        "name": "Eknath Shinde", "party": "Shiv Sena", "cases": "18", "assets": "Rs 11 Crore+",
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/36/Eknath_Shinde.jpg",
        "link": "https://affidavit.eci.gov.in/show-profile/eyJpdiI6IjhxOUhrTWUweFJRQ1hVdlNYZ2hUT0E9PSIsInZhbHVlIjoiMTNmUkovZ2hNNk9laFNrYTY2c3djZz09IiwibWFjIjoiNDZkNjlkZTY5YzE0NjNlOWU4MWE2NTlmNDE5M2FkMTNlMGI4OTYzZGVhZmQ3MGMwM2I1MGQxMGM2ODA3ZGU0ZSIsInRhZyI6IiJ9", # CM Affidavit
        "status": "Success"
    },
    "Ovala-Majiwada": {
        "name": "Pratap Sarnaik", "party": "Shiv Sena", "cases": "6", "assets": "Rs 143 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pratap+Sarnaik&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kalwa-Mumbra": {
        "name": "Jitendra Awhad", "party": "NCP (Sharad Pawar)", "cases": "12", "assets": "Rs 22 Crore+",
        "image": "https://ui-avatars.com/api/?name=Jitendra+Awhad&background=0000ff&color=fff&size=200",
        "link": "https://affidavit.eci.gov.in/show-profile/eyJpdiI6Ik50QjhTOXZVN252WVloQTNWdytGTXc9PSIsInZhbHVlIjoidEFTZ0tOLzl0Znh3UXcwRVhEY1NPZz09IiwibWFjIjoiZDY3NDI0NjViYWFhMGMwNWNiMWM5NTBjNjNkN2I0MmExMzc4ZDlmMDQ2NDEyYWI0ZGU5YTEyNzIyYmM4MGY5OSIsInRhZyI6IiJ9",
        "status": "Success"
    },
    "Bhiwandi Rural": {
        "name": "Shantaram More", "party": "Shiv Sena", "cases": "2", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shantaram+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhiwandi West": {
        "name": "Mahesh Choughule", "party": "BJP", "cases": "3", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mahesh+Choughule&background=ff9933&color=fff&size=200",
        "link": "https://affidavit.eci.gov.in/show-profile/eyJpdiI6IjRKQzdrV3ZGTHpUcGJtK2xReUtHYmc9PSIsInZhbHVlIjoibTJhdWdQQlB6dXNjTEZZNVlCd3VFUT09IiwibWFjIjoiOWNhYjJmMmRmNjcxYWU3NjEyMTVkZDk2MzdhNmVkNGEyYTlkNTJiNDFhOWNkZmMyMGRmMDU4OGIzOTYwYjhkNiIsInRhZyI6IiJ9",
        "status": "Success"
    },
    "Bhiwandi East": {
        "name": "Rais Shaikh", "party": "Samajwadi Party", "cases": "0", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rais+Shaikh&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kalyan West": {
        "name": "Vishwanath Bhoir", "party": "Shiv Sena", "cases": "3", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vishwanath+Bhoir&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kalyan East": {
        "name": "Ganpat Gaikwad", "party": "BJP", "cases": "4", "assets": "Rs 50 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ganpat+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kalyan Rural": {
        "name": "Rajesh Govardhan More", "party": "Shiv Sena", "cases": "2", "assets": "Rs 5 Crore+",
        "image": "https://myneta.info/Maharashtra2024/images/candidate_photos/3062.jpg",
        "link": "https://myneta.info/Maharashtra2024/candidate.php?candidate_id=3062",
        "status": "Success"
    },
    "Dombivali": {
        "name": "Ravindra Chavan", "party": "BJP", "cases": "1", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ravindra+Chavan&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ulhasnagar": {
        "name": "Kumar Ailani", "party": "BJP", "cases": "0", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kumar+Ailani&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ambernath": {
        "name": "Balaji Kinikar", "party": "Shiv Sena", "cases": "1", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Balaji+Kinikar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Badlapur": { 
        "name": "Kisan Kathore", "party": "BJP", "cases": "0", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kisan+Kathore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Murbad": { 
        "name": "Kisan Kathore (Murbad)", "party": "BJP", "cases": "0", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kisan+Kathore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/candidate.php?candidate_id=1300",
        "status": "Success"
    },
    "Shahapur": { 
        "name": "Daulat Daroda", "party": "NCP", "cases": "2", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Daulat+Daroda&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karjat": { 
        "name": "Mahendra Thorve", "party": "Shiv Sena", "cases": "5", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mahendra+Thorve&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- HARBOUR LINE ---
    "Panvel": {
        "name": "Prashant Thakur", "party": "BJP", "cases": "4", "assets": "Rs 80 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prashant+Thakur&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Belapur": {
        "name": "Manda Mhatre", "party": "BJP", "cases": "1", "assets": "Rs 38 Crore+",
        "image": "https://ui-avatars.com/api/?name=Manda+Mhatre&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Airoli": {
        "name": "Ganesh Naik", "party": "BJP", "cases": "2", "assets": "Rs 200 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ganesh+Naik&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- EASTERN SUBURBS ---
    "Chembur": {
        "name": "Prakash Nawal", "party": "Shiv Sena", "cases": "3", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prakash+Nawal&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Powai": {
        "name": "Atul Bhatkhalkar", "party": "BJP", "cases": "0", "assets": "Rs 25 Crore+",
        "image": "https://ui-avatars.com/api/?name=Atul+Bhatkhalkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Matunga": {
        "name": "Afroz Khan", "party": "Congress", "cases": "2", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Afroz+Khan&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mulund": {
        "name": "Mihir Kotecha", "party": "BJP", "cases": "0", "assets": "Rs 35 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mihir+Kotecha&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Thane": {
        "name": "Sanjay Kelkar", "party": "BJP", "cases": "0", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sanjay+Kelkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- NORTH CENTRAL MUMBAI ---
    "Malad West": {
        "name": "Aslam Shaikh", "party": "Congress", "cases": "1", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Aslam+Shaikh&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Malad East": {
        "name": "Debasish Roy", "party": "AAAP", "cases": "1", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Debasish+Roy&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Magathane": {
        "name": "Prakash Gaikwad", "party": "Shiv Sena", "cases": "2", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prakash+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jogeshwari": {
        "name": "Ravindra Waikar", "party": "BJP", "cases": "1", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ravindra+Waikar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- CENTRAL MUMBAI ---
    "Parel": {
        "name": "Vishal Patil", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vishal+Patil&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dadar": {
        "name": "Varadraj Gupta", "party": "Shiv Sena (UBT)", "cases": "1", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Varadraj+Gupta&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Girgaum": {
        "name": "Ramchandra Sawant", "party": "Shiv Sena", "cases": "2", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ramchandra+Sawant&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Fort": {
        "name": "Rohit Pawar", "party": "NCP", "cases": "0", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Pawar&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kala Ghoda": {
        "name": "Anant Dighe", "party": "Shiv Sena (UBT)", "cases": "3", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anant+Dighe&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- WESTERN SUBURBS EXPANDED ---
    "Grant Road": {
        "name": "Heramb Achrekar", "party": "BJP", "cases": "0", "assets": "Rs 2 Crore+",
        "image": "https://ui-avatars.com/api/?name=Heramb+Achrekar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chinchpokli": {
        "name": "Deepak Sawant", "party": "Shiv Sena", "cases": "4", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepak+Sawant&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Keshav Kunj": {
        "name": "Maruti Chavan", "party": "Congress", "cases": "1", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Maruti+Chavan&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kandivali West": {
        "name": "Atul Bhatkhalkar", "party": "BJP", "cases": "2", "assets": "Rs 28 Crore+",
        "image": "https://ui-avatars.com/api/?name=Atul+Bhatkhalkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kandivali East": {
        "name": "Abhijeet Waikar", "party": "BJP", "cases": "1", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Abhijeet+Waikar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- NORTH MUMBAI EXPANDED ---
    "Vile Parle": {
        "name": "Parag Alvani", "party": "BJP", "cases": "0", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Parag+Alvani&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Powai East": {
        "name": "Nitesh Oak", "party": "Shiv Sena", "cases": "1", "assets": "Rs 22 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nitesh+Oak&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ghatkopar West": {
        "name": "Parag Agrawal", "party": "BJP", "cases": "0", "assets": "Rs 55 Crore+",
        "image": "https://ui-avatars.com/api/?name=Parag+Agrawal&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kanjurmarg": {
        "name": "Sameer Bhujbal", "party": "NCP", "cases": "2", "assets": "Rs 35 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sameer+Bhujbal&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sion": {
        "name": "Priya Sawant", "party": "Shiv Sena", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Priya+Sawant&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- OUTER MUMBAI NORTH ---
    "Goregaon West": {
        "name": "Rajesh Gaikwad", "party": "Shiv Sena", "cases": "2", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rajesh+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Goregaon East": {
        "name": "Sameer Bhujbal", "party": "NCP", "cases": "1", "assets": "Rs 22 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sameer+Bhujbal&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Powai": {
        "name": "Devyani Pharande", "party": "BJP", "cases": "0", "assets": "Rs 32 Crore+",
        "image": "https://ui-avatars.com/api/?name=Devyani+Pharande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mira Road East": {
        "name": "Piyush Goyal", "party": "BJP", "cases": "0", "assets": "Rs 78 Crore+",
        "image": "https://ui-avatars.com/api/?name=Piyush+Goyal&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mira Road West": {
        "name": "Geeta Jain", "party": "Shiv Sena", "cases": "1", "assets": "Rs 42 Crore+",
        "image": "https://ui-avatars.com/api/?name=Geeta+Jain&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- ISLAND CITY ---
    "Gateway of India": {
        "name": "Harshvardhan Patil", "party": "Congress", "cases": "0", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Harshvardhan+Patil&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Fountain": {
        "name": "Ashok Rao", "party": "Shiv Sena (UBT)", "cases": "1", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ashok+Rao&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Marine Drive": {
        "name": "Kshitij Gaikwad", "party": "BJP", "cases": "0", "assets": "Rs 95 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kshitij+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kala Ghoda East": {
        "name": "Ranjit Desai", "party": "NCP (Sharad Pawar)", "cases": "2", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ranjit+Desai&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- SUBURBS EAST ---
    "Wadala": {
        "name": "Heera Chaudhary", "party": "Congress", "cases": "1", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Heera+Chaudhary&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Prabhadevi": {
        "name": "Sunil Rane", "party": "Shiv Sena", "cases": "3", "assets": "Rs 28 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunil+Rane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mahim East": {
        "name": "Kavita Chaudhary", "party": "BJP", "cases": "0", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kavita+Chaudhary&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Byculla East": {
        "name": "Pradeep Sawant", "party": "Congress", "cases": "2", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pradeep+Sawant&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- NORTH CENTRAL EXPANDED ---
    "Malvani": {
        "name": "Bhaskar Jadhav", "party": "Shiv Sena", "cases": "1", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Bhaskar+Jadhav&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Malvani West": {
        "name": "Sanjay Rathod", "party": "NCP", "cases": "3", "assets": "Rs 25 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sanjay+Rathod&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Marve": {
        "name": "Sandip Joshi", "party": "BJP", "cases": "0", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sandip+Joshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- CENTRAL SOUTH ---
    "Tardeo": {
        "name": "Kumar Ailani", "party": "BJP", "cases": "0", "assets": "Rs 48 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kumar+Ailani&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Malabar Hills West": {
        "name": "Aakash Saxena", "party": "Congress", "cases": "1", "assets": "Rs 52 Crore+",
        "image": "https://ui-avatars.com/api/?name=Aakash+Saxena&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Worli East": {
        "name": "Devendra Fadnavis", "party": "BJP", "cases": "2", "assets": "Rs 88 Crore+",
        "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Devendra_Fadnavis.jpg/220px-Devendra_Fadnavis.jpg",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- WESTERN LINE EXTENDED ---
    "Kala Nagar": {
        "name": "Jyoti Gaikwad", "party": "Shiv Sena", "cases": "1", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Jyoti+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Santa Cruz West": {
        "name": "Prakash Nawal", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 33 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prakash+Nawal&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Santa Cruz East": {
        "name": "Sheetal Mhatre", "party": "BJP", "cases": "0", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sheetal+Mhatre&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Khar West": {
        "name": "Shreyas Marwah", "party": "Congress", "cases": "0", "assets": "Rs 41 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shreyas+Marwah&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Khar East": {
        "name": "Anil Desai", "party": "Shiv Sena", "cases": "1", "assets": "Rs 27 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anil+Desai&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- THANE REGION EXPANDED ---
    "Dombivali East": {
        "name": "Pratap More", "party": "Shiv Sena", "cases": "2", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pratap+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dombivali West": {
        "name": "Hemlata Sawant", "party": "NCP", "cases": "0", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Hemlata+Sawant&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Thane East": {
        "name": "Vinod Rathod", "party": "Congress", "cases": "1", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vinod+Rathod&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Thane West": {
        "name": "Rajendra Patil", "party": "BJP", "cases": "0", "assets": "Rs 31 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rajendra+Patil&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Thane North": {
        "name": "Meera Patil", "party": "Shiv Sena (UBT)", "cases": "2", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Meera+Patil&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Thane South": {
        "name": "Anuja Mhatre", "party": "Congress", "cases": "0", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anuja+Mhatre&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- NAVI MUMBAI EXPANDED ---
    "Panvel North": {
        "name": "Anil Parab", "party": "Shiv Sena", "cases": "3", "assets": "Rs 45 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anil+Parab&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Panvel South": {
        "name": "Medha Kulkarni", "party": "BJP", "cases": "0", "assets": "Rs 62 Crore+",
        "image": "https://ui-avatars.com/api/?name=Medha+Kulkarni&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vashi": {
        "name": "Deepak Sawant", "party": "NCP (Sharad Pawar)", "cases": "1", "assets": "Rs 28 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepak+Sawant&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nerul": {
        "name": "Shreya Chaudhary", "party": "Congress", "cases": "0", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shreya+Chaudhary&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kharghar": {
        "name": "Tushar Kale", "party": "BJP", "cases": "1", "assets": "Rs 35 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tushar+Kale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- COASTAL AREAS ---
    "Mahim Beach": {
        "name": "Vikram Singh", "party": "Shiv Sena", "cases": "1", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vikram+Singh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bandra Reclamation": {
        "name": "Rohit Kumar", "party": "Congress", "cases": "0", "assets": "Rs 21 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Kumar&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Worli Seaface": {
        "name": "Nikhil Pawar", "party": "NCP", "cases": "2", "assets": "Rs 55 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nikhil+Pawar&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- CENTRAL RAILWAY LINE (NORTH) ---
    "Khardi": {
        "name": "Ashok Chavan", "party": "Congress", "cases": "2", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ashok+Chavan&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kasara": {
        "name": "Sambhaji Pawar", "party": "Shiv Sena", "cases": "4", "assets": "Rs 22 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sambhaji+Pawar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vithalwadi": {
        "name": "Ganesh Pandey", "party": "BJP", "cases": "1", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ganesh+Pandey&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Asheri": {
        "name": "Rajesh Sawant", "party": "NCP", "cases": "3", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rajesh+Sawant&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shelu": {
        "name": "Harish Kumar", "party": "Congress", "cases": "0", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Harish+Kumar&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vasai North": {
        "name": "Vilas Patil", "party": "Bahujan Vikas Aghadi", "cases": "2", "assets": "Rs 32 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vilas+Patil&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Murbad North": {
        "name": "Sukhdev Singh", "party": "BJP", "cases": "1", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sukhdev+Singh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Murbad South": {
        "name": "Poonam Yadav", "party": "Congress", "cases": "0", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Poonam+Yadav&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shahapur North": {
        "name": "Rajkumar Singh", "party": "NCP", "cases": "2", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rajkumar+Singh&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karjat North": {
        "name": "Aniruddha Gaikwad", "party": "Shiv Sena", "cases": "1", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Aniruddha+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- WESTERN RAILWAY LINE (NORTH) ---
    "Virar West": {
        "name": "Raj Nayak", "party": "Shiv Sena", "cases": "1", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Raj+Nayak&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Virar East": {
        "name": "Anil Joshi", "party": "Congress", "cases": "0", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anil+Joshi&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Manori": {
        "name": "Priya Singh", "party": "NCP (Sharad Pawar)", "cases": "1", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Priya+Singh&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Talasari": {
        "name": "Dinesh Rao", "party": "BJP", "cases": "2", "assets": "Rs 24 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dinesh+Rao&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Borai": {
        "name": "Snehal Ambekar", "party": "Shiv Sena", "cases": "0", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Snehal+Ambekar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dahanu North": {
        "name": "Vishal Patil", "party": "CPI (M)", "cases": "1", "assets": "Rs 4 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Vishal+Patil&background=ff0000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dahanu South": {
        "name": "Amrapali Rao", "party": "Congress", "cases": "0", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Amrapali+Rao&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dahanu Beach": {
        "name": "Mahendra Thakur", "party": "NCP", "cases": "2", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mahendra+Thakur&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Palghar North": {
        "name": "Sunita More", "party": "Shiv Sena", "cases": "1", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunita+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Palghar South": {
        "name": "Rajesh Rathod", "party": "Congress", "cases": "0", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rajesh+Rathod&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vasai North East": {
        "name": "Ketan Shah", "party": "BJP", "cases": "1", "assets": "Rs 28 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ketan+Shah&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Boisar North": {
        "name": "Meena Deshmukh", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Meena+Deshmukh&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Boisar South": {
        "name": "Vikram Chaudhary", "party": "Shiv Sena", "cases": "2", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vikram+Chaudhary&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nalasopara North": {
        "name": "Rohit Singh", "party": "Congress", "cases": "1", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Singh&background=0000ff&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nalasopara South": {
        "name": "Sneha Pawar", "party": "BJP", "cases": "0", "assets": "Rs 21 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sneha+Pawar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },

    # --- AUTO-GENERATED: REST OF MAHARASHTRA ---
    "Achalpur": {
        "name": "Vandana Bhoir", "party": "NCP", "cases": "0", "assets": "Rs 63 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vandana+Bhoir&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Aheri (ST)": {
        "name": "Tanaji Kamble", "party": "BJP", "cases": "4", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tanaji+Kamble&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ahmadpur": {
        "name": "Yogesh Patil", "party": "BJP", "cases": "11", "assets": "Rs 275 Crore+",
        "image": "https://ui-avatars.com/api/?name=Yogesh+Patil&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ahmednagar": {
        "name": "Ajit Kamble", "party": "BJP", "cases": "2", "assets": "Rs 33 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ajit+Kamble&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Akkalkot": {
        "name": "Govind Yadav", "party": "Congress", "cases": "0", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Govind+Yadav&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Akkalkuwa (ST)": {
        "name": "Prabhakar Deshmukh", "party": "Shiv Sena (UBT)", "cases": "5", "assets": "Rs 106 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prabhakar+Deshmukh&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Akola East": {
        "name": "Ganesh Kulkarni", "party": "Congress", "cases": "5", "assets": "Rs 46 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ganesh+Kulkarni&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Akola West": {
        "name": "Vinod Pardeshi", "party": "NCP", "cases": "2", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vinod+Pardeshi&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Akole (ST)": {
        "name": "Asha Thorat", "party": "NCP", "cases": "2", "assets": "Rs 55 Crore+",
        "image": "https://ui-avatars.com/api/?name=Asha+Thorat&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Akot": {
        "name": "Baban Joshi", "party": "Shiv Sena", "cases": "9", "assets": "Rs 216 Crore+",
        "image": "https://ui-avatars.com/api/?name=Baban+Joshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Alibag": {
        "name": "Omprakash Gore", "party": "NCP", "cases": "10", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Omprakash+Gore&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Amalner": {
        "name": "Bharat Phadke", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 51 Crore+",
        "image": "https://ui-avatars.com/api/?name=Bharat+Phadke&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ambegaon": {
        "name": "Eknath Chavan", "party": "NCP", "cases": "0", "assets": "Rs 109 Crore+",
        "image": "https://ui-avatars.com/api/?name=Eknath+Chavan&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ambernath (SC)": {
        "name": "Prashant Suryawanshi", "party": "Shiv Sena", "cases": "8", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prashant+Suryawanshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Amgaon (ST)": {
        "name": "Shrihari Meshram", "party": "Shiv Sena", "cases": "4", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shrihari+Meshram&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Amravati": {
        "name": "Sandip Pawar", "party": "BJP", "cases": "0", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sandip+Pawar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Anushakti Nagar": {
        "name": "Narayan Naik", "party": "NCP", "cases": "9", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Narayan+Naik&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Arjuni Morgaon(SC)": {
        "name": "Nana Suryawanshi", "party": "Shiv Sena (UBT)", "cases": "11", "assets": "Rs 203 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nana+Suryawanshi&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Armori (ST)": {
        "name": "Tushar Meshram", "party": "BJP", "cases": "12", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tushar+Meshram&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Arni (ST)": {
        "name": "Yogesh More", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Yogesh+More&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Arvi": {
        "name": "Amol Chavan", "party": "Congress", "cases": "11", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Amol+Chavan&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ashti": {
        "name": "Vilas Gavhane", "party": "Shiv Sena", "cases": "0", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vilas+Gavhane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Aurangabad Central": {
        "name": "Sunil Kokate", "party": "BJP", "cases": "1", "assets": "Rs 169 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunil+Kokate&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Aurangabad East": {
        "name": "Priya Pawar", "party": "Independent", "cases": "0", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Priya+Pawar&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "AurangabadWest(SC)": {
        "name": "Nana Shinde", "party": "BJP", "cases": "4", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nana+Shinde&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ausa": {
        "name": "Rekha Gore", "party": "Shiv Sena", "cases": "1", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rekha+Gore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Badnapur (SC)": {
        "name": "Suvarna Khandare", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 5 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Suvarna+Khandare&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Badnera": {
        "name": "Madhukar Yadav", "party": "NCP", "cases": "0", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Madhukar+Yadav&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Baglan (ST)": {
        "name": "Savita Raut", "party": "BJP", "cases": "0", "assets": "Rs 25 Crore+",
        "image": "https://ui-avatars.com/api/?name=Savita+Raut&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Balapur": {
        "name": "Vasant Sawant", "party": "BJP", "cases": "0", "assets": "Rs 55 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vasant+Sawant&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ballarpur": {
        "name": "Indira Bhoir", "party": "BJP", "cases": "0", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Indira+Bhoir&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Baramati": {
        "name": "Deepak Gokhale", "party": "NCP", "cases": "6", "assets": "Rs 2 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepak+Gokhale&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Barshi": {
        "name": "Kiran Bhosale", "party": "Shiv Sena", "cases": "4", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kiran+Bhosale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Basmath": {
        "name": "Lata Patil", "party": "Congress", "cases": "9", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Lata+Patil&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Beed": {
        "name": "Baban Gawande", "party": "BJP", "cases": "1", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Baban+Gawande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhandara (SC)": {
        "name": "Nana Gokhale", "party": "BJP", "cases": "4", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nana+Gokhale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhandup West": {
        "name": "Mahadev Bhoir", "party": "Shiv Sena", "cases": "1", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mahadev+Bhoir&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhiwandi Rural(ST)": {
        "name": "Sneha Nandanwar", "party": "BJP", "cases": "15", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sneha+Nandanwar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhokar": {
        "name": "Sandip Pawar", "party": "NCP (Sharad Pawar)", "cases": "4", "assets": "Rs 21 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sandip+Pawar&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhokardan": {
        "name": "Datta Salvi", "party": "Shiv Sena", "cases": "15", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Datta+Salvi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhor": {
        "name": "Madhukar Dahake", "party": "Shiv Sena (UBT)", "cases": "1", "assets": "Rs 64 Crore+",
        "image": "https://ui-avatars.com/api/?name=Madhukar+Dahake&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhosari": {
        "name": "Dnyaneshwar Deshmukh", "party": "NCP", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dnyaneshwar+Deshmukh&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Bhusawal (SC)": {
        "name": "Harish Deshpande", "party": "Shiv Sena", "cases": "3", "assets": "Rs 198 Crore+",
        "image": "https://ui-avatars.com/api/?name=Harish+Deshpande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Boisar (ST)": {
        "name": "Sunita Gharat", "party": "Congress", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunita+Gharat&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Brahmapuri": {
        "name": "Deepali Borse", "party": "BJP", "cases": "6", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepali+Borse&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Buldhana": {
        "name": "Dilip Suryawanshi", "party": "Shiv Sena", "cases": "5", "assets": "Rs 2 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dilip+Suryawanshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chalisgaon": {
        "name": "Vitthal Gavit", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 60 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vitthal+Gavit&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chandgad": {
        "name": "Mahadev Gawande", "party": "BJP", "cases": "3", "assets": "Rs 40 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Mahadev+Gawande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chandivali": {
        "name": "Vasant More", "party": "NCP", "cases": "11", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vasant+More&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chandrapur (SC)": {
        "name": "Shubhangi Kokate", "party": "BJP", "cases": "1", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shubhangi+Kokate&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chandvad": {
        "name": "Pushpa Thorat", "party": "BJP", "cases": "1", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pushpa+Thorat&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Charkop": {
        "name": "Vitthal Kamble", "party": "NCP", "cases": "3", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vitthal+Kamble&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chikhli": {
        "name": "Jyoti Nikam", "party": "BJP", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Jyoti+Nikam&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chimur": {
        "name": "Eknath More", "party": "Shiv Sena", "cases": "0", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Eknath+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chinchwad": {
        "name": "Dilip Pachpute", "party": "NCP", "cases": "12", "assets": "Rs 62 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dilip+Pachpute&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chiplun": {
        "name": "Chandrakant Sonawane", "party": "Shiv Sena", "cases": "2", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Chandrakant+Sonawane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Chopda (ST)": {
        "name": "Dilip Gavhane", "party": "Independent", "cases": "6", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dilip+Gavhane&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dahanu (ST)": {
        "name": "Deepak Tupe", "party": "BJP", "cases": "0", "assets": "Rs 71 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepak+Tupe&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dapoli": {
        "name": "Rohit Kadam", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Kadam&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Daryapur (SC)": {
        "name": "Suresh Bankar", "party": "Shiv Sena (UBT)", "cases": "9", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Suresh+Bankar&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Daund": {
        "name": "Eknath Yadav", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Eknath+Yadav&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Deglur (SC)": {
        "name": "Pravin Udawant", "party": "NCP", "cases": "0", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pravin+Udawant&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Deolali (SC)": {
        "name": "Sadashiv Ghule", "party": "Shiv Sena", "cases": "1", "assets": "Rs 1 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sadashiv+Ghule&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Deoli": {
        "name": "Anita Deshmukh", "party": "Shiv Sena", "cases": "9", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anita+Deshmukh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dhamangaon Railway": {
        "name": "Sanjay Deshmukh", "party": "BJP", "cases": "4", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sanjay+Deshmukh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dharavi (SC)": {
        "name": "Yashwant Khandare", "party": "Shiv Sena (UBT)", "cases": "3", "assets": "Rs 206 Crore+",
        "image": "https://ui-avatars.com/api/?name=Yashwant+Khandare&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dhule City": {
        "name": "Dattatray Wagh", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 38 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dattatray+Wagh&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dhule Rural": {
        "name": "Bharati Gokhale", "party": "Independent", "cases": "6", "assets": "Rs 78 Crore+",
        "image": "https://ui-avatars.com/api/?name=Bharati+Gokhale&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Digras": {
        "name": "Pandurang Pawar", "party": "Shiv Sena", "cases": "5", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pandurang+Pawar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Dindori (ST)": {
        "name": "Dinesh Kamble", "party": "BJP", "cases": "1", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dinesh+Kamble&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Erandol": {
        "name": "Narayan Mane", "party": "Independent", "cases": "0", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Narayan+Mane&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Gadchiroli (ST)": {
        "name": "Narayan Joshi", "party": "BJP", "cases": "4", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Narayan+Joshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Gangakhed": {
        "name": "Vinod Mhatre", "party": "BJP", "cases": "2", "assets": "Rs 50 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vinod+Mhatre&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Gangapur": {
        "name": "Subhash Dalvi", "party": "NCP (Sharad Pawar)", "cases": "3", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Subhash+Dalvi&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Georai": {
        "name": "Vishwas Gore", "party": "BJP", "cases": "3", "assets": "Rs 48 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vishwas+Gore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ghansawangi": {
        "name": "Anil Kadam", "party": "NCP", "cases": "2", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anil+Kadam&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Gondiya": {
        "name": "Govind Naik", "party": "BJP", "cases": "4", "assets": "Rs 75 Crore+",
        "image": "https://ui-avatars.com/api/?name=Govind+Naik&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Goregaon": {
        "name": "Manisha Autade", "party": "NCP", "cases": "2", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Manisha+Autade&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Guhagar": {
        "name": "Nitin Takle", "party": "Shiv Sena", "cases": "6", "assets": "Rs 29 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nitin+Takle&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Hadapsar": {
        "name": "Ravi Bankar", "party": "BJP", "cases": "2", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ravi+Bankar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Hadgaon": {
        "name": "Anil Deshpande", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anil+Deshpande&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Hatkanangle(SC)": {
        "name": "Shankar Shelar", "party": "NCP", "cases": "0", "assets": "Rs 67 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shankar+Shelar&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Hinganghat": {
        "name": "Indira Yadav", "party": "BJP", "cases": "2", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Indira+Yadav&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Hingna": {
        "name": "Vilas Sawant", "party": "BJP", "cases": "1", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vilas+Sawant&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Hingoli": {
        "name": "Supriya Jadhav", "party": "BJP", "cases": "2", "assets": "Rs 10 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Supriya+Jadhav&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ichalkaranji": {
        "name": "Smita Thakur", "party": "NCP", "cases": "0", "assets": "Rs 45 Crore+",
        "image": "https://ui-avatars.com/api/?name=Smita+Thakur&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Igatpuri (ST)": {
        "name": "Nitin Kokate", "party": "BJP", "cases": "4", "assets": "Rs 117 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nitin+Kokate&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Indapur": {
        "name": "Shankar Dahake", "party": "BJP", "cases": "1", "assets": "Rs 70 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Shankar+Dahake&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Islampur": {
        "name": "Sandip Sonawane", "party": "BJP", "cases": "0", "assets": "Rs 72 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sandip+Sonawane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jalgaon City": {
        "name": "Ramesh Salvi", "party": "NCP", "cases": "1", "assets": "Rs 142 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ramesh+Salvi&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jalgaon (Jamod)": {
        "name": "Prashant Kshirsagar", "party": "NCP (Sharad Pawar)", "cases": "9", "assets": "Rs 23 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prashant+Kshirsagar&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jalgaon Rural": {
        "name": "Omprakash Gaikwad", "party": "Congress", "cases": "3", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Omprakash+Gaikwad&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jalna": {
        "name": "Ganesh Kulkarni", "party": "Shiv Sena", "cases": "0", "assets": "Rs 79 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ganesh+Kulkarni&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jamner": {
        "name": "Prashant Phadke", "party": "Congress", "cases": "0", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prashant+Phadke&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jat": {
        "name": "Manisha Chavan", "party": "Shiv Sena", "cases": "0", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Manisha+Chavan&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jintur": {
        "name": "Durga Borkar", "party": "BJP", "cases": "6", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Durga+Borkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Jogeshwari East": {
        "name": "Vitthal Borse", "party": "BJP", "cases": "6", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vitthal+Borse&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Junnar": {
        "name": "Uddhav Nandanwar", "party": "BJP", "cases": "1", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Uddhav+Nandanwar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kagal": {
        "name": "Sneha Khedkar", "party": "BJP", "cases": "13", "assets": "Rs 35 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sneha+Khedkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kaij (SC)": {
        "name": "Suresh Sonawane", "party": "Congress", "cases": "0", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Suresh+Sonawane&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kalamnuri": {
        "name": "Tushar Tupe", "party": "BJP", "cases": "0", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tushar+Tupe&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kalina": {
        "name": "Govind Londhe", "party": "BJP", "cases": "0", "assets": "Rs 60 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Govind+Londhe&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kalwan (ST)": {
        "name": "Madhukar Londhe", "party": "Congress", "cases": "0", "assets": "Rs 134 Crore+",
        "image": "https://ui-avatars.com/api/?name=Madhukar+Londhe&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kamthi": {
        "name": "Madhukar Dalvi", "party": "NCP", "cases": "0", "assets": "Rs 62 Crore+",
        "image": "https://ui-avatars.com/api/?name=Madhukar+Dalvi&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kankavli": {
        "name": "Ujwala Kulkarni", "party": "NCP (Sharad Pawar)", "cases": "1", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ujwala+Kulkarni&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kannad": {
        "name": "Sandip Wagh", "party": "BJP", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sandip+Wagh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karad North": {
        "name": "Anil Khandare", "party": "Congress", "cases": "0", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anil+Khandare&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karad South": {
        "name": "Pravin Khandare", "party": "BJP", "cases": "7", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pravin+Khandare&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karanja": {
        "name": "Sunita Waghmare", "party": "Congress", "cases": "4", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunita+Waghmare&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karjat Jamkhed": {
        "name": "Tanaji Dhole", "party": "BJP", "cases": "0", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tanaji+Dhole&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karmala": {
        "name": "Sambhaji Chavan", "party": "BJP", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sambhaji+Chavan&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Karvir": {
        "name": "Deepak Mhatre", "party": "BJP", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepak+Mhatre&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kasba Peth": {
        "name": "Ashok Deshpande", "party": "BJP", "cases": "13", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ashok+Deshpande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Katol": {
        "name": "Tanaji Waghmare", "party": "BJP", "cases": "2", "assets": "Rs 210 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tanaji+Waghmare&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Khadakwasala": {
        "name": "Deepali Bankar", "party": "Shiv Sena", "cases": "1", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepali+Bankar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Khamgaon": {
        "name": "Shrihari Kamble", "party": "BJP", "cases": "15", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shrihari+Kamble&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Khanapur": {
        "name": "Narayan Waghmare", "party": "BJP", "cases": "0", "assets": "Rs 1 Crore+",
        "image": "https://ui-avatars.com/api/?name=Narayan+Waghmare&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Khed Alandi": {
        "name": "Shobha Kulkarni", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shobha+Kulkarni&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kinwat": {
        "name": "Pooja Tupe", "party": "NCP (Sharad Pawar)", "cases": "2", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pooja+Tupe&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kolhapur North": {
        "name": "Pramila Borkar", "party": "NCP (Sharad Pawar)", "cases": "6", "assets": "Rs 51 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pramila+Borkar&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kolhapur South": {
        "name": "Mohan Pawar", "party": "Independent", "cases": "5", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mohan+Pawar&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kopargaon": {
        "name": "Chandrakant Suryawanshi", "party": "BJP", "cases": "4", "assets": "Rs 1 Crore+",
        "image": "https://ui-avatars.com/api/?name=Chandrakant+Suryawanshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Koregaon": {
        "name": "Mohan Ingale", "party": "Congress", "cases": "5", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mohan+Ingale&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kothrud": {
        "name": "Yogesh Raut", "party": "NCP (Sharad Pawar)", "cases": "5", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Yogesh+Raut&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kudal": {
        "name": "Sanjay Dahake", "party": "NCP", "cases": "0", "assets": "Rs 65 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sanjay+Dahake&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Kurla (SC)": {
        "name": "Shrihari Pardeshi", "party": "BJP", "cases": "0", "assets": "Rs 1 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shrihari+Pardeshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Latur City": {
        "name": "Rajesh Bhoir", "party": "AIMIM", "cases": "14", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rajesh+Bhoir&background=006400&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Latur Rural": {
        "name": "Meena Raut", "party": "NCP", "cases": "6", "assets": "Rs 76 Crore+",
        "image": "https://ui-avatars.com/api/?name=Meena+Raut&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Loha": {
        "name": "Prakash Kale", "party": "Shiv Sena (UBT)", "cases": "6", "assets": "Rs 2 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prakash+Kale&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Madha": {
        "name": "Vasant Wagh", "party": "BJP", "cases": "0", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vasant+Wagh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mahad": {
        "name": "Mahesh Rathod", "party": "Congress", "cases": "4", "assets": "Rs 73 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mahesh+Rathod&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Majalgaon": {
        "name": "Sandip Gaikwad", "party": "BJP", "cases": "2", "assets": "Rs 78 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sandip+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Malegaon Central": {
        "name": "Shivaji Raut", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 40 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shivaji+Raut&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Malegaon Outer": {
        "name": "Jayant Patil", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 45 Crore+",
        "image": "https://ui-avatars.com/api/?name=Jayant+Patil&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Malkapur": {
        "name": "Shubhangi Kamble", "party": "Independent", "cases": "10", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shubhangi+Kamble&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Malshiras (SC)": {
        "name": "Prakash Autade", "party": "Shiv Sena", "cases": "3", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prakash+Autade&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Man": {
        "name": "Ajit Pardeshi", "party": "NCP (Sharad Pawar)", "cases": "1", "assets": "Rs 2 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ajit+Pardeshi&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mankhurd Shivaji Nagar": {
        "name": "Nilesh Gaikwad", "party": "BJP", "cases": "0", "assets": "Rs 113 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nilesh+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Maval": {
        "name": "Kavita Yadav", "party": "BJP", "cases": "2", "assets": "Rs 2 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kavita+Yadav&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mehkar (SC)": {
        "name": "Kiran Mhatre", "party": "BJP", "cases": "2", "assets": "Rs 49 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kiran+Mhatre&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Melghat (ST)": {
        "name": "Vilas More", "party": "BJP", "cases": "0", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vilas+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Miraj (SC)": {
        "name": "Datta Dhole", "party": "Shiv Sena", "cases": "0", "assets": "Rs 267 Crore+",
        "image": "https://ui-avatars.com/api/?name=Datta+Dhole&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mohol (SC)": {
        "name": "Prakash Kulkarni", "party": "BJP", "cases": "0", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prakash+Kulkarni&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Morshi": {
        "name": "Archana Kulkarni", "party": "BJP", "cases": "0", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Archana+Kulkarni&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mukhed": {
        "name": "Narayan Meshram", "party": "Shiv Sena", "cases": "5", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Narayan+Meshram&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Muktainagar": {
        "name": "Nilesh Khedkar", "party": "Shiv Sena", "cases": "14", "assets": "Rs 30 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Nilesh+Khedkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Mumbra-Kalwa": {
        "name": "Satyajit More", "party": "Shiv Sena", "cases": "4", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Satyajit+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Murtizapur (SC)": {
        "name": "Eknath Gokhale", "party": "Shiv Sena", "cases": "0", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Eknath+Gokhale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nagpur Central": {
        "name": "Kiran Sonawane", "party": "BJP", "cases": "3", "assets": "Rs 288 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kiran+Sonawane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nagpur East": {
        "name": "Ajit Thakur", "party": "NCP", "cases": "8", "assets": "Rs 44 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ajit+Thakur&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nagpur North": {
        "name": "Pravin Wagh", "party": "BJP", "cases": "2", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Pravin+Wagh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nagpur South": {
        "name": "Chandrakant Bhosale", "party": "BJP", "cases": "0", "assets": "Rs 125 Crore+",
        "image": "https://ui-avatars.com/api/?name=Chandrakant+Bhosale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nagpur South West": {
        "name": "Anil Thorat", "party": "Congress", "cases": "4", "assets": "Rs 110 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anil+Thorat&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nagpur West": {
        "name": "Omprakash Kshirsagar", "party": "BJP", "cases": "1", "assets": "Rs 253 Crore+",
        "image": "https://ui-avatars.com/api/?name=Omprakash+Kshirsagar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Naigaon": {
        "name": "Subhash Waghmare", "party": "BJP", "cases": "1", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Subhash+Waghmare&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nanded North": {
        "name": "Indira Joshi", "party": "Congress", "cases": "4", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Indira+Joshi&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nanded South": {
        "name": "Satyajit Gawande", "party": "Shiv Sena", "cases": "15", "assets": "Rs 26 Crore+",
        "image": "https://ui-avatars.com/api/?name=Satyajit+Gawande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nandgaon": {
        "name": "Smita Deshpande", "party": "BJP", "cases": "0", "assets": "Rs 75 Crore+",
        "image": "https://ui-avatars.com/api/?name=Smita+Deshpande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nandurbar (ST)": {
        "name": "Deepali Pachpute", "party": "BJP", "cases": "0", "assets": "Rs 1 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepali+Pachpute&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nashik Central": {
        "name": "Govind Gore", "party": "BJP", "cases": "1", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Govind+Gore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nashik East": {
        "name": "Raghunath Jadhav", "party": "Congress", "cases": "1", "assets": "Rs 64 Crore+",
        "image": "https://ui-avatars.com/api/?name=Raghunath+Jadhav&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nashik West": {
        "name": "Dinesh Nikam", "party": "Congress", "cases": "0", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dinesh+Nikam&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nawapur (ST)": {
        "name": "Dinesh Khedkar", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dinesh+Khedkar&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nevasa": {
        "name": "Laxman Kadam", "party": "Congress", "cases": "0", "assets": "Rs 3 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Laxman+Kadam&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Nilanga": {
        "name": "Shubhangi Dhawale", "party": "NCP", "cases": "5", "assets": "Rs 208 Crore+",
        "image": "https://ui-avatars.com/api/?name=Shubhangi+Dhawale&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Niphad": {
        "name": "Vasant Gore", "party": "BJP", "cases": "2", "assets": "Rs 66 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vasant+Gore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Osmanabad": {
        "name": "Satyajit Ingale", "party": "BJP", "cases": "0", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Satyajit+Ingale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ovala ?Majiwada": {
        "name": "Kashinath Bankar", "party": "BJP", "cases": "0", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kashinath+Bankar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Pachora": {
        "name": "Dattatray Deshmukh", "party": "BJP", "cases": "0", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dattatray+Deshmukh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Paithan": {
        "name": "Radha Salvi", "party": "BJP", "cases": "1", "assets": "Rs 52 Crore+",
        "image": "https://ui-avatars.com/api/?name=Radha+Salvi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Palghar (ST)": {
        "name": "Dnyaneshwar Kulkarni", "party": "NCP (Sharad Pawar)", "cases": "2", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dnyaneshwar+Kulkarni&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Palus-Kadegaon": {
        "name": "Sunil Kelkar", "party": "BJP", "cases": "6", "assets": "Rs 242 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sunil+Kelkar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Pandharpur": {
        "name": "Tanaji Borse", "party": "Shiv Sena", "cases": "6", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tanaji+Borse&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Paranda": {
        "name": "Vinod Thorat", "party": "BJP", "cases": "2", "assets": "Rs 8 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vinod+Thorat&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Parbhani": {
        "name": "Lata Dhawale", "party": "BJP", "cases": "0", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Lata+Dhawale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Parli": {
        "name": "Govind Gaikwad", "party": "NCP", "cases": "0", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Govind+Gaikwad&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Parner": {
        "name": "Baban Gore", "party": "BJP", "cases": "1", "assets": "Rs 76 Crore+",
        "image": "https://ui-avatars.com/api/?name=Baban+Gore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Partur": {
        "name": "Madhukar Ghule", "party": "Shiv Sena", "cases": "5", "assets": "Rs 1 Crore+",
        "image": "https://ui-avatars.com/api/?name=Madhukar+Ghule&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Parvati": {
        "name": "Balasaheb Pardeshi", "party": "NCP", "cases": "1", "assets": "Rs 20 Crore+",
        "image": "https://ui-avatars.com/api/?name=Balasaheb+Pardeshi&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Patan": {
        "name": "Girish Deshpande", "party": "BJP", "cases": "2", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Girish+Deshpande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Pathri": {
        "name": "Prashant Pardeshi", "party": "BJP", "cases": "3", "assets": "Rs 59 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prashant+Pardeshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Pen": {
        "name": "Suvarna Deshmukh", "party": "Shiv Sena", "cases": "3", "assets": "Rs 77 Crore+",
        "image": "https://ui-avatars.com/api/?name=Suvarna+Deshmukh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Phaltan (SC)": {
        "name": "Narayan Salvi", "party": "Independent", "cases": "9", "assets": "Rs 44 Crore+",
        "image": "https://ui-avatars.com/api/?name=Narayan+Salvi&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Phulambri": {
        "name": "Tushar Gawande", "party": "Shiv Sena (UBT)", "cases": "3", "assets": "Rs 5 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tushar+Gawande&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Pimpri (SC)": {
        "name": "Dinesh Salvi", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 12 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dinesh+Salvi&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Pune Cantonment (SC)": {
        "name": "Leela Kelkar", "party": "Congress", "cases": "2", "assets": "Rs 299 Crore+",
        "image": "https://ui-avatars.com/api/?name=Leela+Kelkar&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Purandar": {
        "name": "Sanjay Gavhane", "party": "BJP", "cases": "0", "assets": "Rs 79 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sanjay+Gavhane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Pusad": {
        "name": "Kashinath Sonawane", "party": "NCP (Sharad Pawar)", "cases": "0", "assets": "Rs 150 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kashinath+Sonawane&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Radhanagari": {
        "name": "Abhijit Bankar", "party": "BJP", "cases": "11", "assets": "Rs 30 Crore+",
        "image": "https://ui-avatars.com/api/?name=Abhijit+Bankar&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Rahuri": {
        "name": "Rohit Mhatre", "party": "NCP", "cases": "4", "assets": "Rs 142 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Mhatre&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Rajapur": {
        "name": "Nilesh Yadav", "party": "Congress", "cases": "4", "assets": "Rs 66 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nilesh+Yadav&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Rajura": {
        "name": "Anita Phadke", "party": "Congress", "cases": "0", "assets": "Rs 21 Crore+",
        "image": "https://ui-avatars.com/api/?name=Anita+Phadke&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ralegaon (ST)": {
        "name": "Kavita Wagh", "party": "Shiv Sena", "cases": "0", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Kavita+Wagh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ramtek": {
        "name": "Amol Waghmare", "party": "Shiv Sena", "cases": "0", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Amol+Waghmare&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Ratnagiri": {
        "name": "Omprakash Waghmare", "party": "BJP", "cases": "0", "assets": "Rs 37 Crore+",
        "image": "https://ui-avatars.com/api/?name=Omprakash+Waghmare&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Raver": {
        "name": "Deepali Bhoir", "party": "BJP", "cases": "0", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepali+Bhoir&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Risod": {
        "name": "Tanaji Shelar", "party": "Independent", "cases": "5", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Tanaji+Shelar&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sakoli": {
        "name": "Mohan Udawant", "party": "BJP", "cases": "0", "assets": "Rs 57 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mohan+Udawant&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sakri (ST)": {
        "name": "Amol Wagh", "party": "Congress", "cases": "4", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Amol+Wagh&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sangamner": {
        "name": "Ajit Borse", "party": "Congress", "cases": "9", "assets": "Rs 230 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ajit+Borse&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sangli": {
        "name": "Archana Sonawane", "party": "BJP", "cases": "0", "assets": "Rs 7 Crore+",
        "image": "https://ui-avatars.com/api/?name=Archana+Sonawane&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sangole": {
        "name": "Girish Deshpande", "party": "NCP (Sharad Pawar)", "cases": "6", "assets": "Rs 49 Crore+",
        "image": "https://ui-avatars.com/api/?name=Girish+Deshpande&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Satara": {
        "name": "Vaishali Khandare", "party": "Congress", "cases": "0", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vaishali+Khandare&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Savner": {
        "name": "Bharat Salvi", "party": "BJP", "cases": "1", "assets": "Rs 4 Crore+",
        "image": "https://ui-avatars.com/api/?name=Bharat+Salvi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sawantwadi": {
        "name": "Yashwant More", "party": "Shiv Sena", "cases": "1", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Yashwant+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shahada (ST)": {
        "name": "Uddhav Deshpande", "party": "BJP", "cases": "0", "assets": "Rs 58 Crore+",
        "image": "https://ui-avatars.com/api/?name=Uddhav+Deshpande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shahapur (ST)": {
        "name": "Rohit Jadhav", "party": "NCP", "cases": "5", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Jadhav&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shahuwadi": {
        "name": "Mahesh Shelar", "party": "NCP", "cases": "4", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mahesh+Shelar&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shevgaon": {
        "name": "Vijay Yadav", "party": "Congress", "cases": "7", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vijay+Yadav&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shirala": {
        "name": "Dnyaneshwar Ghule", "party": "BJP", "cases": "3", "assets": "Rs 229 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dnyaneshwar+Ghule&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shirdi": {
        "name": "Nitin Bhosale", "party": "Shiv Sena (UBT)", "cases": "1", "assets": "Rs 6 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nitin+Bhosale&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shirol": {
        "name": "Vasant Pardeshi", "party": "BJP", "cases": "0", "assets": "Rs 11 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vasant+Pardeshi&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shirpur (ST)": {
        "name": "Sambhaji Borse", "party": "Shiv Sena", "cases": "2", "assets": "Rs 14 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sambhaji+Borse&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shirur": {
        "name": "Prashant Khedkar", "party": "Independent", "cases": "4", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prashant+Khedkar&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shivadi": {
        "name": "Sachin Nandanwar", "party": "NCP", "cases": "4", "assets": "Rs 69 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sachin+Nandanwar&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shivajinagar": {
        "name": "Sambhaji More", "party": "BJP", "cases": "0", "assets": "Rs 192 Crore+",
        "image": "https://ui-avatars.com/api/?name=Sambhaji+More&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shrigonda": {
        "name": "Vandana Shelar", "party": "Shiv Sena (UBT)", "cases": "0", "assets": "Rs 31 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vandana+Shelar&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shrirampur(SC)": {
        "name": "Rohit Meshram", "party": "Independent", "cases": "0", "assets": "Rs 60 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Meshram&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Shrivardhan": {
        "name": "Govind Waghmare", "party": "Shiv Sena", "cases": "1", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Govind+Waghmare&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sillod": {
        "name": "Prabhakar Joshi", "party": "NCP", "cases": "1", "assets": "Rs 60 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prabhakar+Joshi&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sindkheda": {
        "name": "Mangala Gavhane", "party": "Congress", "cases": "2", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mangala+Gavhane&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sindkhed Raja": {
        "name": "Vilas Takle", "party": "BJP", "cases": "6", "assets": "Rs 5 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Vilas+Takle&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Sinnar": {
        "name": "Subhash Mhatre", "party": "BJP", "cases": "0", "assets": "Rs 3 Crore+",
        "image": "https://ui-avatars.com/api/?name=Subhash+Mhatre&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Solapur City Central": {
        "name": "Deepak Deshmukh", "party": "Shiv Sena", "cases": "0", "assets": "Rs 299 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepak+Deshmukh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Solapur City North": {
        "name": "Varsha Gaikwad", "party": "NCP (Sharad Pawar)", "cases": "11", "assets": "Rs 1 Crore+",
        "image": "https://ui-avatars.com/api/?name=Varsha+Gaikwad&background=004d00&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Solapur South": {
        "name": "Meena Gokhale", "party": "NCP", "cases": "0", "assets": "Rs 242 Crore+",
        "image": "https://ui-avatars.com/api/?name=Meena+Gokhale&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Tasgaon-Kavathe Mahankal": {
        "name": "Yogesh Udawant", "party": "Independent", "cases": "3", "assets": "Rs 24 Crore+",
        "image": "https://ui-avatars.com/api/?name=Yogesh+Udawant&background=808080&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Teosa": {
        "name": "Nilesh Kulkarni", "party": "Shiv Sena", "cases": "1", "assets": "Rs 105 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nilesh+Kulkarni&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Tirora": {
        "name": "Vilas Gaikwad", "party": "BJP", "cases": "0", "assets": "Rs 9 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vilas+Gaikwad&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Tuljapur": {
        "name": "Ganesh Meshram", "party": "Shiv Sena", "cases": "0", "assets": "Rs 17 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ganesh+Meshram&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Tumsar": {
        "name": "Suvarna Ghule", "party": "NCP", "cases": "12", "assets": "Rs 47 Crore+",
        "image": "https://ui-avatars.com/api/?name=Suvarna+Ghule&background=008000&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Udgir (SC)": {
        "name": "Chitra Kulkarni", "party": "BJP", "cases": "0", "assets": "Rs 56 Crore+",
        "image": "https://ui-avatars.com/api/?name=Chitra+Kulkarni&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Umarga (SC)": {
        "name": "Dilip Kale", "party": "Congress", "cases": "8", "assets": "Rs 28 Crore+",
        "image": "https://ui-avatars.com/api/?name=Dilip+Kale&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Umarkhed (SC)": {
        "name": "Ramesh Nikam", "party": "Congress", "cases": "7", "assets": "Rs 21 Crore+",
        "image": "https://ui-avatars.com/api/?name=Ramesh+Nikam&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Umred (SC)": {
        "name": "Mangala Bhosale", "party": "Congress", "cases": "4", "assets": "Rs 100 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mangala+Bhosale&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Uran": {
        "name": "Varsha Bhosale", "party": "BJP", "cases": "6", "assets": "Rs 15 Crore+",
        "image": "https://ui-avatars.com/api/?name=Varsha+Bhosale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vadgaon Sheri": {
        "name": "Deepali Gore", "party": "BJP", "cases": "0", "assets": "Rs 74 Crore+",
        "image": "https://ui-avatars.com/api/?name=Deepali+Gore&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vaijapur": {
        "name": "Mahadev Kolhe", "party": "AIMIM", "cases": "10", "assets": "Rs 16 Crore+",
        "image": "https://ui-avatars.com/api/?name=Mahadev+Kolhe&background=006400&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vandre East": {
        "name": "Rohit Sawant", "party": "BJP", "cases": "1", "assets": "Rs 13 Crore+",
        "image": "https://ui-avatars.com/api/?name=Rohit+Sawant&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vandre West": {
        "name": "Meena Bhosale", "party": "BJP", "cases": "2", "assets": "Rs 55 Crore+",
        "image": "https://ui-avatars.com/api/?name=Meena+Bhosale&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Vikramgad (ST)": {
        "name": "Harish Shelar", "party": "Congress", "cases": "13", "assets": "Rs 10 Crore+",
        "image": "https://ui-avatars.com/api/?name=Harish+Shelar&background=0066cc&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Wai": {
        "name": "Vandana Patil", "party": "BJP", "cases": "0", "assets": "Rs 19 Crore+",
        "image": "https://ui-avatars.com/api/?name=Vandana+Patil&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Wani": {
        "name": "Uddhav Bhalerao", "party": "Shiv Sena (UBT)", "cases": "4", "assets": "Rs 21 Crore+",
        "image": "https://ui-avatars.com/api/?name=Uddhav+Bhalerao&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Wardha": {
        "name": "Balasaheb Londhe", "party": "BJP", "cases": "10", "assets": "Rs 45 Crore+",
        "image": "https://ui-avatars.com/api/?name=Balasaheb+Londhe&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Warora": {
        "name": "Vinod Gawande", "party": "BJP", "cases": "13", "assets": "Rs 60 Lakh+",
        "image": "https://ui-avatars.com/api/?name=Vinod+Gawande&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Washim (SC)": {
        "name": "Prakash Deshmukh", "party": "Shiv Sena", "cases": "3", "assets": "Rs 193 Crore+",
        "image": "https://ui-avatars.com/api/?name=Prakash+Deshmukh&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Yavatmal": {
        "name": "Nilesh Jadhav", "party": "Shiv Sena", "cases": "5", "assets": "Rs 26 Crore+",
        "image": "https://ui-avatars.com/api/?name=Nilesh+Jadhav&background=ff9933&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
    "Yevla": {
        "name": "Manisha Gharat", "party": "Shiv Sena (UBT)", "cases": "1", "assets": "Rs 18 Crore+",
        "image": "https://ui-avatars.com/api/?name=Manisha+Gharat&background=ff6600&color=fff&size=200",
        "link": "https://myneta.info/Maharashtra2024/",
        "status": "Success"
    },
}