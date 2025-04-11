# Feedback on Braintrust Setup and Usage

## Setup Friction

1. **API Key Configuration**:
   - The documentation wasn't entirely clear on where to find the API key in the Braintrust UI
   - Having to set the API key in both the environment and directly in the code was redundant
   - A clearer explanation of API key management would be helpful

2. **Command Line Tool Issues**:
   - The `braintrust` CLI command wasn't automatically added to PATH after installation
   - The documentation suggests using `braintrust eval` but doesn't explain how to ensure the command is available

3. **Package Dependencies**:
   - The starter code mentions installing `braintrust` and `autoevals`, but doesn't specify other dependencies like `openai`
   - Version compatibility between packages wasn't specified

## Confusing Steps

1. **SDK Documentation Mismatch**:
   - Some methods mentioned in the documentation (like `create_dataset` and `create_playground`) didn't work as expected
   - The examples in the documentation didn't always match the actual API behavior

2. **Evaluation Flow**:
   - The relationship between spans, logs, and evaluations wasn't clearly explained
   - It wasn't immediately obvious how to view the results in the UI after logging

3. **Project Creation**:
   - The process for creating a new project via the SDK vs. the UI wasn't well documented
   - It wasn't clear if project names need to be unique across all users

## Bugs

1. **Error Handling**:
   - When the API key was invalid or missing, the error messages weren't always helpful
   - Some SDK functions failed silently or with generic errors

2. **UI Refresh Issues**:
   - Sometimes the UI didn't immediately show new logs/spans without a manual refresh
   - The URL provided in the console output sometimes led to a page that needed additional navigation to see results

## Suggestions for Improvement

1. Add a more comprehensive getting started guide with step-by-step instructions
2. Provide clearer error messages that suggest specific solutions
3. Include more complete examples that cover common use cases
4. Better explain the relationship between different Braintrust concepts (projects, datasets, evaluations)
5. Improve the CLI tool installation and PATH configuration
