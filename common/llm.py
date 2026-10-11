"""One place for provider code. Swap Claude <-> Ollama with one argument.

    from common.llm import ask, embed
    ask("Summarize this...", provider="ollama")
    ask("Plan this research task...", provider="claude", model="claude-opus-5-5")
"""
import json
import os
import urllib.request

from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
DEFAULTS = {
    "claude": os.getenv("CLAUDE_MODEL", "claude-sonnet-5-5"),
    "ollama": os.getenv("OLLAMA_MODEL", "gpt-oss:20b"),
}
EMBED_MODEL = os.getenv("EMBED_MODEL", "nomic-embed-text")


def _ollama(path: str, body: dict) -> dict:
    req = urllib.request.Request(
        OLLAMA_URL + path, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def ask(prompt: str, provider: str = "claude", model: str | None = None,
        system: str | None = None, max_tokens: int = 1024) -> str:
    """Send one prompt and return the text reply."""
    model = model or DEFAULTS[provider]
    if provider == "claude":
        import anthropic  # imported here so Ollama-only labs don't need it
        kwargs = {"system": system} if system else {}
        msg = anthropic.Anthropic().messages.create(
            model=model, max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}], **kwargs,
        )
        return "".join(b.text for b in msg.content if b.type == "text")
    if provider == "ollama":
        messages = ([{"role": "system", "content": system}] if system else []) + [
            {"role": "user", "content": prompt}]
        return _ollama("/api/chat", {"model": model, "messages": messages, "stream": False})["message"]["content"]
    raise ValueError(f"Unknown provider: {provider!r} (use 'claude' or 'ollama')")


def embed(texts: list[str], model: str = EMBED_MODEL) -> list[list[float]]:
    """Local embeddings via Ollama (Anthropic has no embeddings endpoint)."""
    return _ollama("/api/embed", {"model": model, "input": texts})["embeddings"]
