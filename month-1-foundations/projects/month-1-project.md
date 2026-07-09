# Month 1 Project — LLM-Powered CLI Tool

Build a small but real command-line tool powered by the OpenAI API.

## Pick one
1. **Smart summarizer** — paste/point at text, get a tight summary + 3 key points.
2. **Terminal chatbot** — multi-turn conversation that remembers the session.
3. **Structured extractor** — feed it messy text, get clean JSON (e.g. pull
   name/date/amount from an email-style blob — no real personal data).

## Requirements
- Reads input from CLI args, stdin, or an interactive loop.
- Loads the API key from `.env` (never hard-coded, never committed).
- Uses a system prompt that shapes behavior.
- Handles an API error gracefully (try/except + a friendly message).
- A short `README.md` in the project folder: what it does, how to run it.

## Stretch goals
- Add `--model` to switch between a capable and a fast model.
- Stream the response token-by-token.
- For the extractor: validate the JSON against a schema before printing.

## Done when
You can run it from a fresh terminal, it does something genuinely useful, and a
friend could run it from your README alone.
