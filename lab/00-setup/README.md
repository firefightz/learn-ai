# 00 · Setup

- [ ] Install Homebrew, `git`, `gh`, `uv` (`brew install git gh uv`)
- [ ] `gh auth login`, clone this repo: `gh repo clone firefightz/learn-ai ~/learn-ai`
- [ ] Python env: `uv venv && source .venv/bin/activate && uv pip install -r lab/requirements.txt`
- [ ] Copy `.env.example` → `.env`, add `ANTHROPIC_API_KEY` (console.anthropic.com, billed separately from Claude.ai)
- [ ] Confirm `.env` is ignored: `git check-ignore .env`

**Done when:** `uv run python -c "import anthropic"` works and `.env` never shows in `git status`.
