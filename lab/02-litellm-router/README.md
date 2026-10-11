# 02 · LiteLLM router

Goal: one OpenAI-style endpoint; cheap steps go local, hard reasoning goes to Opus.

- [ ] `uv pip install 'litellm[proxy]'`
- [ ] Review `config.yaml` (aliases `cheap`, `local`, `smart`)
- [ ] `litellm --config config.yaml` → serves on `localhost:4000`
- [ ] Call `cheap` and `smart` with the same prompt; compare quality, speed, cost
- [ ] Write `playbooks/routing-rules.md`: which task types go where, and why

**Done when:** an agent can switch models by alias without code changes.
