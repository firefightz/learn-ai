It's YAML, not TOML, but the syntax isn't doing the magic. Two separate things are going on.

**The prefix tells LiteLLM which API to speak.** In `ollama_chat/qwen3:8b`, the part before the slash is the provider, and the part after is the model name as that provider knows it.

- `ollama_chat/` means "send this to an Ollama server using its `/api/chat` endpoint," the same endpoint your `chat.py` uses. (Plain `ollama/` would use Ollama's older `/api/generate` endpoint instead.)
- `anthropic/` means "use Anthropic's Messages API," with the key from `api_key`.

Every provider has its own request format. Your curl sends OpenAI-style JSON to LiteLLM, and LiteLLM uses the prefix to pick the right translator, converts the request into that provider's format, then converts the reply back. That's the whole job of a router.

**LiteLLM doesn't start anything. Ollama does.** LiteLLM is just a forwarder: it sends an HTTP request to `api_base` (`localhost:11434`). The Ollama server you already have running in the background is what manages models:

1. A request arrives naming `qwen3:8b`.
2. If that model isn't in memory, Ollama loads its weights from disk. This is why the first call after a while is slow.
3. It generates the reply.
4. It keeps the model loaded for about 5 minutes of idle time, then unloads it to free memory.

You can watch this happen with `ollama ps`: models appear when called and disappear a few minutes later.

So the full path is: `model: "cheap"` → LiteLLM looks up the alias → `ollama_chat/qwen3:8b` at `localhost:11434` → Ollama loads the model if needed and answers → LiteLLM translates the reply back to you.

The flip side: if Ollama isn't running, LiteLLM can't start it. You'd get a "connection refused" error, and that's worth logging in `failures.md` if you hit it.

## Why a router at all?

Routing (cheap model for easy tasks, strong model for hard ones) and translating (one API for many providers) are two separate ideas.

**Claude doesn't pick the model; your code does.** Every API request names a model, so "Haiku for easy, Opus for hard" is logic you write, or that a tool like Claude Code applies when it runs subagents on cheaper models. With one provider, that's just changing one parameter. No router needed.

**Ollama and LiteLLM do different jobs:**
- **Ollama runs qwen.** It loads the model into memory and serves it, the way Anthropic's servers run Claude. Needed no matter what.
- **LiteLLM translates.** Claude's API and Ollama's API expect different request formats. LiteLLM gives one endpoint, one format, and one key, and converts each request for whichever provider the alias points to.

**LiteLLM is a convenience, not a requirement.** You could call Ollama directly (it has an OpenAI-compatible endpoint) alongside the Anthropic SDK, with two clients and an `if`. What LiteLLM adds:
- **Aliases:** swap `cheap` from qwen to Haiku in `config.yaml` without touching code.
- **Fallbacks:** if one model fails or is down, try another.
- **One place for spend and logs** across every provider.

Takeaway: routing exists because tasks differ in difficulty; LiteLLM exists because the models speak different APIs. With Claude only, the routing rules still apply. You just don't need the translator.
