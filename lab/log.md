# Log

| Date | Module | What clicked |
|------|--------|--------------|
| 2026-10-11 | 00 | Created the repo |
| 2026-10-12 | 01 | Pulled gpt-oss:20b (13 GB), qwen3:8b (5.2 GB), nomic-embed-text (274 MB); ran `chat.py` on 8b vs 20b and watched `ollama ps` — compared tokens/sec between the two |
| 2026-10-12 | 02 | Ran the LiteLLM proxy on :4000 with `cheap`/`local`/`smart` aliases; the provider prefix (`ollama_chat/`, `anthropic/`) picks the translator, and LiteLLM only forwards — Ollama loads/unloads models. Proxy now refuses to boot without `LITELLM_MASTER_KEY` |
| 2026-10-12 | 03 (partial) | Ported `server.py` to mcp 2.x (`FastMCP` → `MCPServer`); added read-only `list_files`/`read_file` tools sandboxed to `shared/` and a `shared://readme` resource; ran it in the Inspector. Resources are attachments the user/app includes, tools are what the model calls. Activation just puts `.venv/bin` on `PATH`, so MCP client configs need `uv run --directory` or absolute paths |
