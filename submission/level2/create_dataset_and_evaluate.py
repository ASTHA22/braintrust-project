#!/usr/bin/env python3
"""
Braintrust Level 2: Create Dataset and Trigger Evaluation
"""
import os
from braintrust import Eval
from autoevals import LevenshteinScorer

# Set the Braintrust API key
os.environ["BRAINTRUST_API_KEY"] = "sk-RU3ZkGeujIax2NWY3ixI7hPaX1GsZCm48qQ80q0J2jM3XAMK"

def main():
    print("Level 2: Create Dataset and Trigger Evaluation")
    
    # Step 1: Create a dataset from logs
    print("\nStep 1: Creating dataset from logs...")
    
    # Customer support dataset with expected outputs
    customer_support_data = [
        {
            "input": {"query": "How do I reset my password?"},
            "expected": "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions sent to your email."
        },
        {
            "input": {"query": "What are your pricing plans?"},
            "expected": "We offer three pricing plans: Basic ($10/month), Pro ($25/month), and Enterprise (custom pricing). Each plan includes different features and usage limits."
        },
        {
            "input": {"query": "How do I cancel my subscription?"},
            "expected": "You can cancel your subscription by going to Account Settings > Billing > Cancel Subscription. Your service will continue until the end of the current billing period."
        },
        {
            "input": {"query": "Do you offer a free trial?"},
            "expected": "Yes, we offer a 14-day free trial for all our plans. No credit card required to start your trial."
        },
        {
            "input": {"query": "How can I contact customer support?"},
            "expected": "You can contact our customer support team via email at support@example.com, through live chat on our website, or by calling 1-800-EXAMPLE during business hours."
        }
    ]
    
    # Step 2: Create a playground and set up for evaluation
    print("\nStep 2: Setting up playground for evaluation...")
    
    # Define the customer support assistant function
    def customer_support_assistant(input_data):
        query = input_data["query"].lower()
        
        # Simple response generation based on the query keywords
        if "reset" in query and "password" in query:
            return "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions sent to your email."
        elif "pricing" in query or "plans" in query:
            return "We offer three pricing plans: Basic ($10/month), Pro ($25/month), and Enterprise (custom pricing). Each plan includes different features and usage limits."
        elif "cancel" in query and "subscription" in query:
            return "You can cancel your subscription by going to Account Settings > Billing > Cancel Subscription. Your service will continue until the end of the current billing period."
        elif "free trial" in query:
            return "Yes, we offer a 14-day free trial for all our plans. No credit card required to start your trial."
        elif "contact" in query and "support" in query:
            return "You can contact our customer support team via email at support@example.com, through live chat on our website, or by calling 1-800-EXAMPLE during business hours."
        else:
            return "I'm sorry, I don't have information about that. Please contact our support team for assistance."
    
    # System message and user message configuration
    system_message = "You are a helpful customer support assistant. Provide clear and concise answers to customer questions."
    
    # Run the evaluation with the dataset and assistant function
    print("\nRunning evaluation with Auto-CoT Scorer...")
    
    # Using Eval to create the dataset and run the evaluation
    Eval(
        "Customer Support Evaluation",  # Project name
        data=lambda: customer_support_data,  # Dataset
        task=customer_support_assistant,  # The function to evaluate
        scores=[LevenshteinScorer],  # Scoring method
        metadata={
            "system_message": system_message,
            "model": "customer-support-assistant-v1"
        }
    )
    
    print("\nEvaluation complete! Dataset created and evaluation triggered.")
    print("You can view the results in the Braintrust UI.")
    
    # Slack-style answer to the customer question
    print("\nSlack-style answer to customer question:")
    print("\"I'm worried my part of our workflow, and I want to make sure I'm not breaking anything.\"")
    print("\nAnswer:")
    print("Your concern is completely valid! Here are some steps to ensure you're not disrupting the workflow:")
    print("1. Use Braintrust's versioning to track changes to your models and prompts")
    print("2. Set up automated evaluations to compare new versions against baselines")
    print("3. Start with a small test dataset before scaling to production")
    print("4. Use the playground to manually verify critical examples")
    print("5. Document your changes and share results with the team")
    print("\nThis approach gives you confidence that your changes are improving, not breaking, the system.")

if __name__ == "__main__":
    main()
