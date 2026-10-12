"""Minimal call to Ollama's local chat API. Usage: python chat.py "your prompt" [model]"""

import json
import sys
import urllib.request

prompt = sys.argv[1] if len(sys.argv) > 1 else "Say hello in five words."
model = sys.argv[2] if len(sys.argv) > 2 else "gpt-oss:20b"

req = urllib.request.Request(
    "http://localhost:11434/api/chat",
    data=json.dumps(
        {
            "model": model,
            "think": "high",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
    ).encode(),
    headers={"Content-Type": "application/json"},
)
with urllib.request.urlopen(req) as r:
    out = json.load(r)
# print("THINKING:", out["message"].get("thinking", "(none)"), "\n")
print(out["message"]["content"])
tps = out["eval_count"] / (out["eval_duration"] / 1e9)
print(f"\n[{model}] {out['eval_count']} tokens at {tps:.1f} tok/s")
