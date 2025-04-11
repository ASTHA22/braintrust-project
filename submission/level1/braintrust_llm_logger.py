#!/usr/bin/env python3
"""
Braintrust LLM Logger - A script to log LLM calls to Braintrust
"""
import os
from braintrust import Eval
from autoevals import LevenshteinScorer

# Set the Braintrust API key
# Replace with your own API key
os.environ["BRAINTRUST_API_KEY"] = "sk-RU3ZkGeujIax2NWY3ixI7hPaX1GsZCm48qQ80q0J2jM3XAMK"

def main():
    # Define a simple LLM function (simulating an OpenAI call)
    # In a real scenario, you would use the OpenAI API here
    def llm_call(prompt):
        return f"This is a response to: {prompt}"
    
    # Run the evaluation
    Eval(
        "Braintrust LLM Demo",  # Project name
        data=lambda: [
            {
                "input": {"prompt": "Tell me about Braintrust"},
                "expected": "Braintrust is a platform for evaluating LLM applications."
            }
        ],  # Test dataset
        task=lambda input_data: llm_call(input_data["prompt"]),  # The function to evaluate
        scores=[LevenshteinScorer],  # Scoring method
    )
    
    print("Successfully logged LLM call to Braintrust!")
    print("You can now view this log in the Braintrust UI.")

if __name__ == "__main__":
    main()
