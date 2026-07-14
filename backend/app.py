from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langgraph_agent import ask_ai
from database import engine, Base, SessionLocal
from models import Interaction
import models

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Request Models
# -----------------------------

class ChatRequest(BaseModel):
    message: str

class InteractionRequest(BaseModel):
    doctor_name: str
    hospital: str
    specialization: str
    products: str
    notes: str
    ai_reply: str

# -----------------------------
# Home API
# -----------------------------

@app.get("/")
def home():
    return {"message": "AI CRM Backend Running"}

# -----------------------------
# AI Chat API
# -----------------------------

@app.post("/chat")
def chat(data: ChatRequest):
    try:
        ai_reply = ask_ai(data.message)
        return {"reply": ai_reply}
    except Exception as e:
        return {"reply": str(e)}

# -----------------------------
# Save Interaction API
# -----------------------------

@app.post("/save")
def save_interaction(data: InteractionRequest):
    db = SessionLocal()

    interaction = Interaction(
        doctor_name=data.doctor_name,
        hospital=data.hospital,
        specialization=data.specialization,
        products=data.products,
        notes=data.notes,
        ai_reply=data.ai_reply
    )

    db.add(interaction)
    db.commit()
    db.refresh(interaction)
    db.close()

    return {
        "message": "Interaction saved successfully!"
    }

# -----------------------------
# View All Interactions API
# -----------------------------

@app.get("/interactions")
def get_interactions():
    db = SessionLocal()

    interactions = db.query(Interaction).all()

    data = []

    for item in interactions:
        data.append({
            "id": item.id,
            "doctor_name": item.doctor_name,
            "hospital": item.hospital,
            "specialization": item.specialization,
            "products": item.products,
            "notes": item.notes,
            "ai_reply": item.ai_reply
        })

    db.close()

    return data

