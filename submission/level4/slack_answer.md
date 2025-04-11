# Slack-style Answer to Customer Question

## Question
"I want to see how many of my model outputs scored below 0.7, and what their prompts were. How do I write that in BTQL?"

## Answer
👋 Great question about using BTQL to analyze your low-scoring outputs!

Here's a query that will show you exactly what you're looking for:

```sql
SELECT input AS prompt, output, scores.overall
FROM spans
WHERE scores.overall < 0.7
ORDER BY scores.overall ASC
```

This query will:
1️⃣ Find all spans where the overall score is below 0.7
2️⃣ Show you the prompt (input), the model's output, and the overall score
3️⃣ Sort results from lowest to highest score, so you see the worst performers first

If you also want to count how many outputs scored below 0.7, you can run:

```sql
SELECT COUNT(*) AS low_score_count
FROM spans
WHERE scores.overall < 0.7
```

💡 **Pro tip**: If you want to group by prompt type to see which types of prompts are struggling the most, you could use:

```sql
SELECT metadata.prompt_type, COUNT(*) AS count
FROM spans
WHERE scores.overall < 0.7
GROUP BY metadata.prompt_type
ORDER BY count DESC
```

(Just replace `metadata.prompt_type` with whatever field you use to categorize your prompts)

Hope that helps! Let me know if you need any clarification or have other BTQL questions. 🚀
