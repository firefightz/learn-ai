# Routing rules

Which LiteLLM alias a task goes to, and why. The aliases live in `lab/02-litellm-router/config.yaml`; callers only ever name the alias, so models can be swapped there without code changes.

| Alias | Model | Runs on | Cost |
|-------|-------|---------|------|
| `cheap` | `qwen3:8b` | Ollama, local | free (RAM + time) |
| `local` | `gpt-oss:20b` | Ollama, local | free (more RAM, ~13 GB) |
| `smart` | `claude-opus-5-5` | Anthropic API | paid per token |

## Default rule

Start at the cheapest alias that can do the job, then escalate only when output quality fails a check you can name. Never default to `smart` "just in case".

## By task type

| Task | Alias | Why |
|------|-------|-----|
| Classify / route a request (pick a label, yes/no) | `cheap` | Short output, easy to verify; errors are cheap to catch |
| Extract fields into JSON | `cheap` | Schema-shaped output; validate it, escalate on parse failure |
| Summarize a doc or log | `cheap` | Lossy is acceptable; turn thinking off (`"think": false`) to cut hidden tokens |
| Multi-step reasoning, math, debugging | `local` | Reasoning model; MoE (~3.6B active params) so it ran *faster* than the 8b in lab 01 |
| Tool / function calling in an agent loop | `local` | Many calls per task; keep the loop free and local |
| Planning a multi-file change or a design | `smart` | Mistakes here cost far more than tokens |
| Final answer a human will act on | `smart` | Quality matters more than cost on the last step |
| Anything with private data you won't send off-box | `cheap` / `local` | Never leaves the machine |

## Escalation triggers

Move up one tier (`cheap` → `local` → `smart`) when:

- Output fails validation (bad JSON, missing fields) twice
- The answer contradicts the input or invents facts
- The task needs more than ~3 reasoning steps or a plan
- A local model is too slow for an interactive loop (check `ollama ps`: the first call after idle includes model load time)

## Gotchas

- **Hidden thinking tokens:** both local models think before answering, and that counts toward latency. qwen3 is verbose; use `"think": false` for simple tasks. gpt-oss only takes `low`/`medium`/`high`.
- **Token counts aren't comparable across models:** they use different tokenizers.
- **LiteLLM doesn't start Ollama:** if Ollama is down, `cheap`/`local` return connection refused. That's not a reason to fall back to `smart` silently.
- **Auth:** every call needs `Authorization: Bearer $LITELLM_MASTER_KEY`.

## Evidence (fill in from the lab 02 comparison)

Same prompt sent to each alias:

| Prompt | Alias | Latency | Tokens out | Quality (1–5) | Notes |
|--------|-------|---------|-----------|---------------|-------|
| | `cheap` | | | | |
| | `local` | | | | |
| | `smart` | | | | |

Revise the rules above when the numbers disagree with them.
