from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import RedirectResponse
from chatbot import chatbot
import json

app = FastAPI()

@app.get("/")
async def root():
    return {
        "Hello": "mundo"
    }

@app.get("/api/v1/chatbot/{query}")
def ask_question(query: str):
    return chatbot(q=query)
