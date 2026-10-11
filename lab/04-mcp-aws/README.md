# 04 · MCP server on AWS (cloud notes)

- [ ] AWS account, root MFA, **$15 budget alarm**, admin IAM user, `aws configure` (us-east-1)
- [ ] Create DynamoDB table `mcp-notes` (key: `topic` + `created`, on-demand)
- [ ] Notes MCP server (Streamable HTTP) with `add_note`, `latest_notes(topic)`
- [ ] Deploy with an IAM role scoped to that one table — never your own keys
- [ ] Add auth before exposing it; connect from Claude Code and from a local model

**Done when:** a local agent saves and recalls notes through the cloud server.
