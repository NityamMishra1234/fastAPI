from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import process

app = FastAPI(title="Voice Assistant API")

# ✅ Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["*"] for all origins (less secure)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(process.router)
