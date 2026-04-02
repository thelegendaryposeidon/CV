import os
import sys

# Load env vars manually to avoid requiring python-dotenv
with open('.env') as f:
    for line in f:
        if line.startswith('GEMINI_API_KEY='):
            os.environ['GEMINI_API_KEY'] = line.strip().split('=', 1)[1]

from main import analyze_candidate, AnalysisRequest

req = AnalysisRequest(
    name="Test Politician",
    party="Test Party",
    cases="2 pending cases",
    assets="Rs 5 Crore"
)

try:
    result = analyze_candidate(req)
    print("----- SUCCESS -----")
    print("RESULT:", result)
except Exception as e:
    print("----- ERROR -----")
    print(e)
