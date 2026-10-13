# 02 · LiteLLM router

Goal: one endpoint for every model; cheap steps go local, hard reasoning goes to Opus.

- [ ] `uv pip install 'litellm[proxy]'`
- [ ] Generate a proxy master key (LiteLLM refuses to start without one):
      `echo "LITELLM_MASTER_KEY=sk-$(openssl rand -hex 32)" >> .env` (repo root; `.env` is gitignored)
- [ ] Review `config.yaml` (aliases `cheap`, `local`, `smart`; `master_key` reads `LITELLM_MASTER_KEY`)
- [ ] From the repo root, start the proxy and leave it running:
      `litellm --config lab/02-litellm-router/config.yaml` → serves on `localhost:4000`
- [ ] In a second terminal, load the key into your shell (LiteLLM reads `.env` itself; your shell doesn't):
      `set -a; . ./.env; set +a`
- [ ] Call `cheap` and `smart` with the same prompt; compare quality, speed, cost:
      ```bash
      curl localhost:4000/v1/chat/completions \
        -H "Authorization: Bearer $LITELLM_MASTER_KEY" -H "Content-Type: application/json" \
        -d '{"model":"cheap","messages":[{"role":"user","content":"hi"}]}'
      ```
- [ ] Write `playbooks/routing-rules.md`: which task types go where, and why

**Done when:** an agent can switch models by alias without code changes.

**Troubleshooting**
- `UnsafeMasterKeyError` on startup → `LITELLM_MASTER_KEY` missing from `.env`, or you started `litellm` outside the repo root.
- `curl: (7) Failed to connect` → the proxy isn't running (terminal 1).
- 401/500 auth error → `$LITELLM_MASTER_KEY` is empty in your shell; re-run the `set -a` line.
