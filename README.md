# AI-Assisted Coding Interview — Foundation

A minimal FastAPI + React foundation for a 30-minute AI-assisted coding interview.
Candidates use Claude/Copilot to add a feature; the interviewer probes their
understanding of what the AI generated. See `docs/interviewer-guide.html` for
the full protocol and `docs/candidate-brief.html` for what to hand the candidate.

## Setup

### Backend (FastAPI)

```bash
cd backend
python3.12 -m venv .venv   # use 3.11/3.12/3.13 — pydantic-core has no 3.14 wheel yet
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest tests/ -q   # sanity check: 5 passed
.venv/bin/uvicorn app.main:app --reload --port 8010
```

API docs at http://localhost:8010/docs once running.

### Frontend (React + Vite)

```bash
cd frontend
npm install
npm run dev   # http://localhost:5180
```

## Structure

```
backend/app/
  main.py           FastAPI app, CORS, router registration
  models.py         User, Order pydantic models
  data.py           in-memory seed data
  routers/users.py  GET /users, GET /users/{id}
  routers/orders.py GET /orders, GET /orders/{id}, GET /orders/by-user/{id}

frontend/src/
  App.jsx                    top-level layout
  api.js                     fetch helpers
  components/OrdersList.jsx  fetches + renders orders (loading/error handled)
```

Both sides are intentionally small and already correct — the interview task
(in `docs/candidate-brief.html`) asks the candidate to extend this with AI
help, which is where realistic defects tend to appear.
