# Level 4: Querying with BTQL

## Query 1: Finding All Failed Spans

```sql
SELECT *
FROM spans
WHERE scores.overall < 0.7
ORDER BY scores.overall ASC
```

### Explanation
This query finds all spans where the overall score is below 0.7, which I've defined as the threshold for "failed" spans. The results are ordered by the overall score in ascending order, so the lowest-scoring spans appear first. This helps identify the most problematic responses that need attention.

## Query 2: Counting Spans Per Prompt Type

```sql
SELECT metadata.query AS prompt_type, COUNT(*) AS count
FROM spans
GROUP BY metadata.query
ORDER BY count DESC
```

### Explanation
This query counts the number of spans for each prompt type, using the `metadata.query` field to identify different types of prompts. The results are grouped by prompt type and ordered by count in descending order, showing the most common prompt types first. This helps understand the distribution of different query types in the dataset.

## Alternative Query 2 (Using Tags)

```sql
SELECT tags.prompt_type, COUNT(*) AS count
FROM spans
GROUP BY tags.prompt_type
ORDER BY count DESC
```

### Explanation
This alternative version of Query 2 uses tags instead of metadata to group spans by prompt type. If your spans have been tagged with prompt types (e.g., "summarization", "qa", etc.), this query will count spans for each type and order them by frequency.
