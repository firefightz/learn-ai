import json
import urllib.request

import chromadb

OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "gpt-oss:20b"


def _post(path: str, body: dict) -> dict:
    req = urllib.request.Request(
        OLLAMA + path, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def embed(texts: list[str]) -> list[list[float]]:
    return _post("/api/embed", {"model": EMBED_MODEL, "input": texts})["embeddings"]


def chat(prompt: str) -> str:
    out = _post("/api/chat", {"model": CHAT_MODEL, "stream": False,
                              "messages": [{"role": "user", "content": prompt}]})
    return out["message"]["content"]


def collection():
    return chromadb.PersistentClient(path="chroma").get_or_create_collection("docs")
