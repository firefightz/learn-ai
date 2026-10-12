what does /api/chat take and return:
it takes in 2 arugments: prompt and model
With stream: true (the default), Ollama sends the reply back in many small pieces, roughly a token or a few at a time, as it generates them. Each piece is its own line of JSON. Only the last one has "done": true and the stats like eval_count. That’s what makes chat apps feel fast: text starts appearing immediately instead of after the whole answer is finished.

With stream: false, Ollama waits until generation is completely done and returns one JSON object. The script can then just do json.load(r), read out["message"]["content"], and grab the stats, all in one go. For a learning script, that’s much easier to read.

Both answers you see are about the same length, roughly 50 tokens each. The difference is in what you don’t see.

Both are reasoning models. Before writing the answer, each one “thinks” through the problem first, and those thinking tokens count toward eval_count. Your script only prints message.content, so the thinking is generated but never shown. Roughly speaking, gpt-oss thought for about 75 tokens and qwen3 for about 250. Qwen3 thinks by default and tends to be fairly verbose about it, even on an easy prompt.

You can see it by adding one line to chat.py before the content print:

python
print("THINKING:", out["message"].get("thinking", "(none)"), "\n")

You can also turn qwen3’s thinking off by adding "think": False to the request body. gpt-oss can’t fully switch it off, but it accepts "think": "low", "medium", or "high". Rerun both with thinking off or set to low, and the token counts should come much closer together.

The speed is the more surprising result: the 20b model ran faster than the 8b. That’s because gpt-oss:20b is a mixture-of-experts model. It has about 21B parameters in total but only activates about 3.6B of them for each token, so per token it does less work than qwen3:8b, which uses all 8B every time. It still needs memory for all 21B, which is why it takes up more of your RAM.

Two caveats for your notes: the two models use different tokenizers, so “300 tokens” doesn’t mean exactly the same amount of text in each. And the content itself differed: qwen led with programming-language tokens, which is a less relevant reading of your question.

These three things together (hidden thinking tokens, MoE speed, and tokenizer differences) are exactly the kind of observations your notes.md is for.