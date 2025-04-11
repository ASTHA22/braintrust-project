# Braintrust Level 4 Submission: Querying with BTQL

This directory contains the submission files for Level 4 of the Braintrust task: Querying with BTQL.

## Files Included

1. `btql_queries.md` - Contains the two BTQL queries with explanations:
   - Query 1: Finding all failed spans (overall score < 0.7)
   - Query 2: Counting spans per prompt type

2. `slack_answer.md` - Slack-style answer to the customer question about writing a BTQL query to find model outputs with scores below 0.7 and their prompts

## Task Completion

### Task 1: Run a BTQL query to find all failed spans
- Defined "failed" as spans with an overall score below 0.7
- Created a query that selects all failed spans and orders them by score (ascending)

### Task 2: Run a query to count spans per prompt type
- Created a query that counts spans grouped by prompt type (using metadata.query)
- Ordered the results by count in descending order
- Provided an alternative version using tags instead of metadata

### Task 3: Write a Slack-style answer to the customer question
- Created a comprehensive Slack-style answer with:
  - The exact BTQL query needed
  - An explanation of what the query does
  - Additional tips for counting and grouping low-scoring outputs
