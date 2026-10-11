# 07 · RAG on AWS (DIY)

Same pipeline as 06, moved to the cloud — still by hand, not Bedrock Knowledge Bases.

- [ ] Docs in S3
- [ ] Embeddings via Bedrock's embeddings API
- [ ] Vectors in pgvector (RDS) or OpenSearch — note the monthly cost before creating
- [ ] Small retrieval service (Lambda) that returns top-k chunks
- [ ] Answer with a local model on the Mac, or Claude via API
- [ ] Tear down anything billing hourly when done

**Done when:** you can map each AWS piece to its local equivalent in 06.
