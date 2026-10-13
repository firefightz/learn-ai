from mcp.server.mcpserver import MCPServer

mcp = MCPServer("demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Does Math."""
    return a + b


@mcp.tool()
def word_count(text: str) -> dict:
    """Count words, characters, and lines in a block of text."""
    return {
        "words": len(text.split()),
        "chars": len(text),
        "lines": len(text.splitlines()),
    }


from pathlib import Path

SHARED = (Path(__file__).parent / "shared").resolve()
SHARED.mkdir(parents=True, exist_ok=True)


def _safe(rel: str) -> Path:
    """Resolve a path and refuse anything outside SHARED."""
    p = (SHARED / rel).resolve()
    if not p.is_relative_to(SHARED):
        raise ValueError(f"{rel!r} is outside the shared folder")
    return p


@mcp.tool()
def list_files(subdir: str = "") -> list[str]:
    """List files in the shared folder (lab/03-mcp-local/shared) or a subfolder of it.
    Returns paths relative to the shared folder. Call this first to find what exists."""
    base = _safe(subdir)
    return sorted(str(p.relative_to(SHARED)) for p in base.rglob("*") if p.is_file())


@mcp.tool()
def read_file(path: str, max_chars: int = 20000) -> str:
    """Read a text file from the shared folder. `path` is relative to the shared folder,
    e.g. 'notes/todo.md'. Read-only; cannot reach anything outside that folder."""
    p = _safe(path)
    if not p.is_file():
        raise FileNotFoundError(f"No file at {path!r}")
    return p.read_text(errors="replace")[:max_chars]


@mcp.resource("shared://readme")
def shared_readme() -> str:
    """The README.md in the shared folder."""
    p = SHARED / "README.md"
    return p.read_text() if p.exists() else "(no README.md yet)"


if __name__ == "__main__":
    mcp.run()  # stdio
