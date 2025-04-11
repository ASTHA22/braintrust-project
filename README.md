# Braintrust Project

This project demonstrates how to integrate with Braintrust for LLM evaluation and logging. It includes implementations for all four levels of the Braintrust challenge:

1. **Level 1**: Set Up and Log to Braintrust
2. **Level 2**: Create a Dataset and Run an Evaluation
3. **Level 3**: Custom Evaluation for Customer Support
4. **Level 4**: Querying with BTQL

## Setup Instructions

1. **Create a Braintrust Account**
   - Sign up at https://braintrust.dev/signup
   - Create a new Project in the Braintrust UI

2. **Configure Environment Variables**
   - Copy the `.env.template` file to `.env`: `cp .env.template .env`
   - Update the `.env` file with your Braintrust API key
   - Update the `.env` file with your OpenAI API key (if needed)

3. **Install Dependencies**
   ```
   python3 -m pip install -r requirements.txt
   ```

## Project Structure

### Submission Folder
The `submission` folder contains all the code and documentation for each level:

- **Level 1**: Basic logging to Braintrust
  - `braintrust_llm_logger.py` - Script to log LLM calls to Braintrust
  - `Level1SS.pdf` - Screenshot showing logged results
  
- **Level 2**: Dataset creation and evaluation
  - `create_dataset_and_evaluate.py` - Script to create a dataset and run an evaluation
  - `Level2SS.pdf` - Screenshot showing evaluation results
  
- **Level 3**: Custom evaluation for customer support
  - `custom_evaluation.py` - Custom scorer for evaluating customer support responses
  - `Level3_TerminalSS.pdf` - Logs from the SDK-run experiment
  - `Level3UI_SS.pdf` - Screenshot showing scores in the UI
  
- **Level 4**: BTQL queries
  - `btql_queries.md` - BTQL queries for analyzing evaluation data
  - `slack_answer.md` - Slack-style answer to customer question about BTQL

### Root Directory
- `requirements.txt` - Python dependencies
- `.env.template` - Template for environment variables (copy to `.env` and add your API keys)
