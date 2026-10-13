# 03 · MCP server (local, Python)

- [ ] `uv add "mcp[cli]"`, run `server.py` in the Inspector: `uv run mcp dev server.py`
- [ ] Connect to Claude Code: `claude mcp add demo -- uv --directory $PWD run server.py`
- [ ] Add a file tool limited to `lab/03-mcp-local/shared/` (read-only)
- [ ] Add Gmail tools: search, read, draft — **no send**, bind `127.0.0.1` only
- [ ] Hook it to `gpt-oss:20b` and see if a local model calls tools reliably

Gotcha: never `print()` in a stdio server — stdout is the protocol channel. Log to stderr.

**Done when:** you can explain tools vs resources vs prompts, and why tool docstrings matter.
