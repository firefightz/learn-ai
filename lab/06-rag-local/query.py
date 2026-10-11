"""Ask a question over ingested docs. Usage: python query.py "question" """
import sys

from rag_common import chat, collection, embed

question = " ".join(sys.argv[1:]) or "What are these documents about?"
hits = collection().query(query_embeddings=embed([question]), n_results=4)

context = "\n\n".join(
    f"[{m['source']} #{m['chunk']}]\n{d}" for d, m in zip(hits["documents"][0], hits["metadatas"][0])
)
prompt = (
    "Answer using only the context. Cite sources like [file #chunk]. "
    "If the answer isn't in the context, say so.\n\n"
    f"Context:\n{context}\n\nQuestion: {question}"
)
print(chat(prompt))
print("\nRetrieved:", [f"{m['source']}#{m['chunk']}" for m in hits["metadatas"][0]])
