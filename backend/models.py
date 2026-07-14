from sqlalchemy import Column, Integer, String, Text
from database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    doctor_name = Column(String)
    hospital = Column(String)
    specialization = Column(String)
    products = Column(Text)
    notes = Column(Text)
    ai_reply = Column(Text)