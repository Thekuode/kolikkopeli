from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import roll

app = FastAPI(title="Kolikkopeli API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular-dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(roll.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Kolikkopeli API"}