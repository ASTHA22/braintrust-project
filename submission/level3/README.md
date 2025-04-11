# Braintrust Level 3 Submission

This directory contains the submission files for Level 3 of the Braintrust task: Create a Custom Evaluation.

## Files Included

1. `custom_evaluation.py` - A script that implements a custom evaluation function for customer support responses based on four dimensions: completeness, accuracy, helpfulness, and tone
2. `slack_answer.md` - Slack-style answer to the customer question about evaluation metrics
3. `evaluation_explanation.md` - Detailed explanation of the custom evaluation metrics and methodology
4. `customer_support_evaluation_results.json` - The results of running the custom evaluation on sample customer support responses, including detailed scores for each dimension

## How to Run

1. Run the script:
   ```
   python custom_evaluation.py
   ```

2. The script will:
   - Load a sample dataset of customer support queries and expected responses
   - Generate responses using a simple customer support assistant function
   - Evaluate each response using the custom evaluation function
   - Print detailed scores for each example
   - Calculate and print average scores across all examples
   - Save the detailed results to `customer_support_evaluation_results.json`

## Evaluation Dimensions

The custom evaluation function assesses customer support responses based on four key dimensions:

1. **Completeness (30%)** - Does the response address all parts of the customer's query?
2. **Accuracy (40%)** - Is the information provided correct when compared to the expected response?
3. **Helpfulness (20%)** - Does the response provide actionable steps or information?
4. **Tone (10%)** - Is the response professional and empathetic?

Each dimension is scored between 0 and 1, and the overall score is calculated as a weighted average of these dimensions.

## Results Summary

The evaluation results show that the sample customer support responses perform well in terms of accuracy (average score: 1.00) and helpfulness (average score: 0.90), but have room for improvement in completeness (average score: 0.52) and tone (average score: 0.07). The overall average score across all examples is 0.74.

## Implementation Details

The custom evaluation function:

1. **Completeness**: Checks if important keywords from the query are addressed in the response
2. **Accuracy**: Compares key phrases from the expected output with the actual output
3. **Helpfulness**: Checks for action indicators and relevant contact information
4. **Tone**: Looks for professional and empathetic language

The weights for each dimension were chosen based on their relative importance to customer satisfaction and support effectiveness.
