## Activation is about finding commands

Installing a package that comes with a command-line tool puts the executable in `.venv/bin/`: `litellm[proxy]` creates `.venv/bin/litellm`, `mcp[cli]` creates `.venv/bin/mcp`. Your shell only searches the folders on `PATH`, and `source .venv/bin/activate` adds `.venv/bin` to that list. Without it, `mcp` gives `command not found` even though it's installed.

Three ways to run it without activating:

```bash
uv run mcp ...        # uv finds the project's .venv
.venv/bin/mcp ...     # call the file by its path
source .venv/bin/activate && mcp ...
```

| You type | Activated | Not activated |
|---|---|---|
| `mcp dev server.py` | project's mcp | `command not found`, or some global install |
| `python server.py` | project's Python and packages | system Python, so `ModuleNotFoundError` |
| `uv run mcp ...` | project's mcp | project's mcp |
| `uv pip install x` | into `.venv` | into `.venv` (found by searching) |

- The plain `mcp` package has no command. The `mcp` executable only comes with `mcp[cli]`.
- Imports follow the same rule: `import mcp` works only under the venv's Python.
- If a *different* venv is activated, `uv pip` installs into it; `uv run` warns and sticks with the project's `.venv`.

**Why it matters here:** Claude Code (or any MCP client) starts the server in a fresh process, not your activated terminal. In the client config, never use a bare `mcp` or `python`. Use `uv run --directory /Users/warren/development/github/learn-ai python server.py`, or an absolute path such as `/Users/warren/development/github/learn-ai/.venv/bin/python`. Otherwise the server runs fine in your terminal but fails in the client.

## mcp 2.x renamed FastMCP

`from mcp.server.fastmcp import FastMCP` fails on mcp 2.x with `ModuleNotFoundError`. It's now:

```python
from mcp.server.mcpserver import MCPServer
mcp = MCPServer("demo")
```

The `@mcp.tool()` decorator and `mcp.run()` are unchanged. Most tutorials still show the v1 name; either translate as above or pin `mcp<2`. Migration guide: https://py.sdk.modelcontextprotocol.io/v2/migration/#fastmcp-renamed-to-mcpserver

## Resources: how they get into a prompt

A resource goes into your message, but through the app's interface rather than as plain text. Each app has its own UI for it.

**In Claude Code**, @-mention it while typing:

```
> @demo:shared://readme summarize this and tell me what's in the folder
```

The format is `@<server-name>:<resource-uri>`. Typing `@` opens an autocomplete menu listing files and the resources from connected MCP servers. On send, Claude Code reads the resource from the server and swaps its content into the message. The model sees roughly:

```
[contents of shared://readme: "# Shared folder"]
summarize this and tell me what's in the folder
```

**In Claude Desktop**, connected servers' resources show up under the attach (+) button, like attaching a file.

**In the Inspector**, clicking `shared://readme` in the Resources tab is doing it by hand: *you* play the app, ask the server for the resource, and see what would get pasted in. There's just no model on the other end.

So a resource is an @-mentionable attachment that your server supplies. The user (or app) chooses to include it; the model doesn't call it the way it calls a tool.
