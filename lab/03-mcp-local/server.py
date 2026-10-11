from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@mcp.tool()
def word_count(text: str) -> dict:
    """Count words, characters, and lines in a block of text."""
    return {"words": len(text.split()), "chars": len(text), "lines": len(text.splitlines())}


if __name__ == "__main__":
    mcp.run()  # stdio
