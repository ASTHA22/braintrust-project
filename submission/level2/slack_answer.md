# Slack-style Answer to Customer Question

## Question
"I'm worried my part of our workflow, and I want to make sure I'm not breaking anything."

## Answer
Your concern is completely valid! Here are some steps to ensure you're not disrupting the workflow:

1. **Use Braintrust's versioning** to track changes to your models and prompts
   - This creates a history of changes that can be compared and reverted if needed

2. **Set up automated evaluations** to compare new versions against baselines
   - Create a benchmark dataset with known good responses
   - Run evaluations against this dataset whenever you make changes
   - Monitor key metrics like accuracy, relevance, and toxicity

3. **Start with a small test dataset** before scaling to production
   - Validate your changes on a representative subset first
   - This limits potential impact while still giving you confidence

4. **Use the playground to manually verify critical examples**
   - Identify high-risk or edge cases that are particularly important
   - Test these manually in the Braintrust playground
   - Pay special attention to cases that have failed in the past

5. **Document your changes and share results with the team**
   - Create clear documentation of what changed and why
   - Share evaluation results showing the impact of your changes
   - Get feedback from teammates before pushing to production

This approach gives you confidence that your changes are improving, not breaking, the system. It also creates a safety net that makes it easier to identify and fix issues if they do occur.
