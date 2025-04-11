# Braintrust Level 1 Submission

This directory contains the submission files for Level 1 of the Braintrust task.

## Files Included

1. `braintrust_llm_logger.py` - A script that logs an LLM call to Braintrust
2. `slack_answer.md` - Slack-style answer to the customer question about structuring Braintrust organization and projects

## How to Run

1. Make sure you have the required dependencies installed:
   ```
   pip install braintrust openai autoevals
   ```

2. Set your Braintrust API key in the script or as an environment variable:
   ```
   export BRAINTRUST_API_KEY=your_api_key_here
   ```

3. Run the script:
   ```
   python braintrust_llm_logger.py
   ```

4. Check the Braintrust UI to see the logged span

## Notes

- The script uses a simulated LLM call for demonstration purposes
- In a real scenario, you would use the OpenAI API or another LLM provider
- Make sure to take a screenshot of the span visible in the Braintrust UI for submission
