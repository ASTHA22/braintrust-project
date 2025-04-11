# Braintrust Integration Project

This project demonstrates how to integrate with Braintrust for LLM evaluation and logging.

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

4. **Run the Logger Script**
   ```
   python3 braintrust_logger.py
   ```

## Project Structure

- `braintrust_logger.py` - Main script to log LLM calls to Braintrust
- `requirements.txt` - Python dependencies
- `.env` - Environment variables for API keys
- `.env.template` - Template for environment variables

## Slack-style Answer to Customer Question

**Customer Question:** "Can you give us some advice on how we should structure our Braintrust organization and projects?"

**Answer:**
For structuring your Braintrust organization and projects, I recommend:

1. **Organization Structure**:
   - Create separate projects for different LLM use cases or product features
   - Use consistent naming conventions for projects (e.g., `product-feature-evaluation`)

2. **Project Management**:
   - Start with a development project for initial testing
   - Create separate production projects for ongoing evaluation
   - Use tags to categorize different types of prompts or use cases

3. **Evaluation Strategy**:
   - Define clear expected outputs for each dataset
   - Create scorers that align with your specific quality metrics
   - Set up regular evaluation cycles to track model performance over time

This approach will help you maintain a clean organization while scaling your evaluation efforts as your LLM applications grow.
