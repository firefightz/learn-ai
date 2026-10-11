# 01 · Local LLM (Ollama)

- [ ] Install/update Ollama (want a recent version for the MLX path on Apple Silicon)
- [ ] `ollama pull gpt-oss:20b qwen3:8b nomic-embed-text`
- [ ] Check it's up: `curl http://localhost:11434`
- [ ] `ollama ps` while chatting — note memory use and % GPU
- [ ] Call the API from Python: `python chat.py "explain tokens in 2 lines"`
- [ ] Compare speed (tokens/s) of 8b vs 20b; log it in `notes.md`

**Done when:** you can explain what `/api/chat` takes and returns, and why 24GB caps model size.
