# CandidateValidate

**Democracy Needs Validation.** — Instantly verify criminal records, assets, and performance of your political candidates.

## Tech Stack

- **Frontend:** Next.js 16 · React 19 · Tailwind CSS · MapLibre GL · Recharts
- **Backend:** Python (FastAPI) · PostgreSQL

## Getting Started

```bash
# Install dependencies
cd frontend && npm install

# Run the dev server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the app.

## Project Structure

```
frontend/
├── app/           # Next.js App Router pages
│   ├── page.tsx   # Landing page
│   └── map/       # Constituency map page
├── components/    # React components (MapInterface, BetaWarningDialog, etc.)
└── public/        # Static assets (logo, party logos)

backend/
├── main.py        # FastAPI server
└── data/          # Constituency & candidate data
```

## License

Built for Mumbai Hacks 2026.
