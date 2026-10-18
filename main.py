import re
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="OpenAI-Compatible Tiny Mock")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    model: str = "tiny-mock"
    messages: list[dict[str, Any]]
    stream: bool = False

@app.get("/")
def root():
    return {"status": "ok", "model": "tiny-mock"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/chat/completions")
def chat_completions(body: ChatRequest):
    prompt = "\n".join(
        str(message.get("content", ""))
        for message in body.messages
        if message.get("role") == "user"
    )
    token_match = re.search(r"TK[0-9A-Fa-f-]+", prompt)
    if token_match:
        answer = f"The token is {token_match.group(0)}"
    else:
        numbers = re.findall(r"(?<!\w)-?\d+", prompt)
        if "+" in prompt and len(numbers) >= 2:
            answer = str(int(numbers[0]) + int(numbers[1]))
        else:
            answer = "I received your message."

    return {
        "id": "chatcmpl-tiny-mock",
        "object": "chat.completion",
        "created": 0,
        "model": body.model or "tiny-mock",
        "choices": [{
            "index": 0,
            "message": {"role": "assistant", "content": answer},
            "finish_reason": "stop"
        }]
    }
