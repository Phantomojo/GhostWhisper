from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import asyncio
import json
import os
from datetime import datetime
from core.message import Message

app = FastAPI()

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'ghostwhisper-devlog.txt')
RECEIVED_MESSAGES_LOG = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'received_messages.log')

def log_devlog(entry: str):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_PATH, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] {entry}\\n")

def log_received_message(message: Message):
    with open(RECEIVED_MESSAGES_LOG, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.utcnow().isoformat()} - From: {message.sender} To: {message.receiver} Content: {message.content}\\n")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/receive")
async def receive_message(request: Request):
    try:
        data = await request.json()
    except Exception:
        log_devlog("[ERROR] Failed to parse JSON payload")
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    try:
        message = Message.deserialize(json.dumps(data))
    except Exception as e:
        log_devlog(f"[ERROR] Failed to deserialize message: {e}")
        raise HTTPException(status_code=400, detail="Invalid message format")

    log_devlog(f"[RECEIVE] Message received from {message.sender} to {message.receiver}")
    log_received_message(message)

    return {"status": "success", "detail": "Message received"}

# Graceful shutdown handling can be added if needed later
