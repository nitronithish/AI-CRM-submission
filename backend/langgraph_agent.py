import os
from typing import TypedDict

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, END

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

class AgentState(TypedDict):
    message: str
    response: str

def analyze_meeting(state: AgentState):
    prompt = f"""
You are an AI CRM Assistant for a pharmaceutical sales representative.

Analyze the meeting notes and return the result in this exact format.

📋 Doctor Information

Doctor Name:
Hospital:
Specialization:

📝 Meeting Summary

(2-3 lines)

💊 Products Discussed

- Product 1
- Product 2

📈 Interest Level

High / Medium / Low

📦 Samples Requested

(number)

📅 Follow-up Action

(action)

⭐ Next Visit Recommendation

(1-2 lines)

Meeting Notes:
{state["message"]}
"""

    result = llm.invoke(prompt)

    return {
        "message": state["message"],
        "response": result.content
    }

builder = StateGraph(AgentState)

builder.add_node("analyze_meeting", analyze_meeting)

builder.set_entry_point("analyze_meeting")

builder.add_edge("analyze_meeting", END)

graph = builder.compile()

def ask_ai(message: str):
    result = graph.invoke({"message": message})
    return result["response"]