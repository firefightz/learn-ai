# 08 · AI pipelines in GitHub Actions

- [ ] Add repo secret `ANTHROPIC_API_KEY` (Settings → Secrets and variables → Actions)
- [ ] Move the "AI article of the day" workflow into `.github/workflows/` and its script here
- [ ] Run it manually (Actions → Run workflow), then let the cron take over
- [ ] Add a second provider and compare picks (multi-provider pipeline)
- [ ] Turn it into an eval: save both answers, grade them, track a score over time

Note: GitHub runners can't reach your Mac's Ollama — use API models in Actions.

**Done when:** a scheduled job produces something you actually read.
