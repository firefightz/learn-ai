"""Ingest every .txt/.pdf in docs/ into Chroma. Skips files already ingested (by hash)."""
import hashlib
from pathlib import Path

from pypdf import PdfReader

from rag_common import collection, embed

CHUNK, OVERLAP = 2000, 300  # characters (~500 / ~75 tokens)


def load(path: Path) -> str:
    if path.suffix == ".pdf":
        return "\n".join(p.extract_text() or "" for p in PdfReader(path).pages)
    return path.read_text(errors="ignore")


def chunks(text: str):
    step = CHUNK - OVERLAP
    for i in range(0, max(len(text), 1), step):
        piece = text[i:i + CHUNK].strip()
        if piece:
            yield piece


col = collection()
for path in sorted(Path("docs").glob("*")):
    if path.suffix not in {".txt", ".md", ".pdf"}:
        continue
    digest = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
    if col.get(where={"hash": digest}, limit=1)["ids"]:
        print(f"skip  {path.name} (unchanged)")
        continue
    col.delete(where={"source": path.name})  # drop old version if file changed
    parts = list(chunks(load(path)))
    col.add(
        ids=[f"{path.name}:{digest}:{i}" for i in range(len(parts))],
        documents=parts,
        embeddings=embed(parts),
        metadatas=[{"source": path.name, "hash": digest, "chunk": i} for i in range(len(parts))],
    )
    print(f"added {path.name}: {len(parts)} chunks")
