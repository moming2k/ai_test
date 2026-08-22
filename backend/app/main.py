from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import orders, users

app = FastAPI(title="AI Test API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(orders.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
