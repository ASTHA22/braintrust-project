# Braintrust Level 2 Submission

This directory contains the submission files for Level 2 of the Braintrust task: Create Dataset and Trigger Evaluation.

## Files Included

1. `create_dataset_and_evaluate.py` - A script that creates a dataset from logs and triggers an evaluation
2. `slack_answer.md` - Slack-style answer to the customer question about ensuring workflow integrity

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
   python create_dataset_and_evaluate.py
   ```

4. Check the Braintrust UI to see the dataset and evaluation results

## What This Script Does

1. **Creates a Dataset from Logs**:
   - Defines a dataset with customer support queries and expected responses
   - Labels the dataset with expected outputs for evaluation

2. **Sets up a Playground for Evaluation**:
   - Configures a system message for the assistant
   - Creates a user message template for the queries

3. **Configures Evaluation**:
   - Uses the LevenshteinScorer to evaluate response quality
   - Sets up metadata for the evaluation

4. **Runs the Evaluation**:
   - Processes each query in the dataset
   - Generates responses using the customer support assistant function
   - Scores the responses against the expected outputs
   - Logs the results to Braintrust

5. **Provides a Slack-style Answer**:
   - Answers the customer question about ensuring workflow integrity
   - Gives practical advice for using Braintrust to validate changes
