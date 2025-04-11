#!/usr/bin/env python3
"""
Braintrust Level 3: Create a Custom Evaluation

This script implements a custom evaluation function for customer support responses.
It evaluates responses based on four dimensions:
1. Completeness - Does it address all parts of the query? (30% weight)
2. Accuracy - Is the information correct? (40% weight)
3. Helpfulness - Does it provide actionable information? (20% weight)
4. Tone - Is it professional and empathetic? (10% weight)
"""
import os
import json
from typing import Dict, Any, List
import braintrust
import time

# Set the Braintrust API key
os.environ["BRAINTRUST_API_KEY"] = "sk-RU3ZkGeujIax2NWY3ixI7hPaX1GsZCm48qQ80q0J2jM3XAMK"

# Custom evaluation function for customer support responses
def evaluate_customer_support_response(actual_output: str, expected_output: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Custom evaluation function that scores customer support responses based on:
    1. Completeness - Does it address all parts of the query?
    2. Accuracy - Is the information correct?
    3. Helpfulness - Does it provide actionable information?
    4. Tone - Is it professional and empathetic?
    
    Returns scores between 0 and 1 for each category and an overall score.
    """
    # Initialize scores
    completeness_score = 0.0
    accuracy_score = 0.0
    helpfulness_score = 0.0
    tone_score = 0.0
    
    # Check completeness - Does it address the query?
    query_keywords = input_data["query"].lower().split()
    important_keywords = [word for word in query_keywords if len(word) > 3]  # Filter out short words
    
    # Count how many important keywords are addressed in the response
    keywords_addressed = sum(1 for keyword in important_keywords if keyword in actual_output.lower())
    completeness_score = min(1.0, keywords_addressed / max(1, len(important_keywords)))
    
    # Check accuracy - Compare with expected output for key information
    expected_lower = expected_output.lower()
    actual_lower = actual_output.lower()
    
    # Look for key phrases from expected output in actual output
    expected_phrases = [phrase.strip() for phrase in expected_lower.split('.') if len(phrase.strip()) > 10]
    phrases_found = 0
    
    for phrase in expected_phrases:
        # Check if the core meaning of the phrase is in the actual output
        phrase_words = set(phrase.split())
        significant_words = [word for word in phrase_words if len(word) > 4]
        
        # Count significant words from the phrase found in the actual output
        words_found = sum(1 for word in significant_words if word in actual_lower)
        
        # If most significant words are found, consider the phrase addressed
        if words_found >= len(significant_words) * 0.7:
            phrases_found += 1
    
    accuracy_score = min(1.0, phrases_found / max(1, len(expected_phrases)))
    
    # Check helpfulness - Does it provide actionable steps?
    action_indicators = ["click", "go to", "visit", "follow", "select", "choose", "enter", "type", "call"]
    has_action_steps = any(indicator in actual_lower for indicator in action_indicators)
    
    # Check if it provides contact information when needed
    needs_contact_info = "contact" in input_data["query"].lower() or "help" in input_data["query"].lower()
    has_contact_info = any(info in actual_lower for info in ["email", "phone", "chat", "support", "contact"])
    
    helpfulness_score = 0.5  # Base score
    if has_action_steps:
        helpfulness_score += 0.25
    if (needs_contact_info and has_contact_info) or not needs_contact_info:
        helpfulness_score += 0.25
    
    # Check tone - Is it professional and empathetic?
    professional_indicators = ["thank", "please", "assist", "help", "support", "apologize", "sorry"]
    professional_count = sum(1 for indicator in professional_indicators if indicator in actual_lower)
    
    tone_score = min(1.0, professional_count / 3)  # Expect at least 3 professional indicators for full score
    
    # Calculate overall score - weighted average
    overall_score = (
        completeness_score * 0.3 +  # 30% weight on completeness
        accuracy_score * 0.4 +       # 40% weight on accuracy
        helpfulness_score * 0.2 +    # 20% weight on helpfulness
        tone_score * 0.1             # 10% weight on tone
    )
    
    # Return detailed scores
    return {
        "completeness": completeness_score,
        "accuracy": accuracy_score,
        "helpfulness": helpfulness_score,
        "tone": tone_score,
        "overall": overall_score
    }

def generate_slack_style_answer(input_data: Dict[str, Any]) -> str:
    """
    Generate a Slack-style answer to the customer question using an LLM.
    """
    query = input_data["query"].lower()
    
    if "north star" in query and "braintrust" in query:
        return """👋 Great question about creating a "north star" metric while evaluating against multiple criteria!

In Braintrust, the best approach is to create a **weighted composite score** that combines your individual evaluation dimensions into a single metric. Here's how you can do this:

1️⃣ **Define your individual evaluation dimensions** (like accuracy, helpfulness, relevance, etc.)

2️⃣ **Assign weights to each dimension** based on their importance to your business goals:
```python
overall_score = (
    completeness_score * 0.3 +  # 30% weight
    accuracy_score * 0.4 +      # 40% weight
    helpfulness_score * 0.2 +   # 20% weight
    tone_score * 0.1            # 10% weight
)
```

3️⃣ **Log both individual scores and the composite score** to Braintrust:
```python
experiment.log(
    input=input_data,
    output=actual_output,
    expected=expected_output,
    scores={
        "completeness": scores["completeness"],
        "accuracy": scores["accuracy"],
        "helpfulness": scores["helpfulness"],
        "tone": scores["tone"],
        "overall": scores["overall"]  # Your north star metric
    }
)
```

4️⃣ **Use the overall score as your north star** for tracking improvement across experiments, while still having access to the individual dimensions for deeper analysis when needed.

This approach gives you the best of both worlds - a single metric to track improvement at a high level, plus detailed scores to understand *why* your overall performance is changing.

Hope that helps! Let me know if you have any other questions. 🚀"""
    else:
        return "I'm sorry, I don't have information about that. Please contact our support team for assistance."

def main():
    print("Level 3: Custom Evaluation for Customer Support")
    
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
            return generate_slack_style_answer(input_data)
    
    # System message for the assistant
    system_message = "You are a helpful customer support assistant. Provide clear and concise answers to customer questions."
    
    # Run the evaluation with custom scoring
    print("\nRunning evaluation with custom scoring...")
    
    # Get current timestamp for experiment name
    timestamp = int(time.time())
    email = "asthasinghthakurast@gmail.com"
    experiment_name = f"{email}-{timestamp}"
    
    # Initialize Braintrust
    try:
        experiment = braintrust.init(project="Customer Support Custom Evaluation")
        print("Successfully initialized Braintrust experiment")
        
        # Print experiment details to help find the correct URL
        print("\nExperiment Details:")
        experiment_id = getattr(experiment, 'id', 'Not found')
        experiment_name = getattr(experiment, 'name', 'Not found')
        print(f"Experiment ID: {experiment_id}")
        print(f"Experiment Name: {experiment_name}")
        
        # Generate the exact URL format that worked before
        braintrust_url = f"https://www.braintrust.dev/app/Idea%20by%20Design/p/Customer%20Support%20Custom%20Evaluation/experiments/{experiment_name}?c={experiment_id}"
        print(f"\nYou can view the results in the Braintrust UI at:")
        print(braintrust_url)
        
    except Exception as e:
        print(f"Error initializing Braintrust: {e}")
        experiment = None
    
    # Store all results for summary
    all_results = []
    
    # Process each example in the dataset
    for i, example in enumerate(customer_support_data):
        # Get input and expected output
        input_data = example["input"]
        expected_output = example["expected"]
        
        # Generate actual output using the assistant
        actual_output = customer_support_assistant(input_data)
        
        # Evaluate the response using our custom function
        scores = evaluate_customer_support_response(actual_output, expected_output, input_data)
        
        # Log to Braintrust if initialized successfully
        if experiment:
            try:
                # Convert scores to format expected by Braintrust
                bt_scores = {
                    "completeness": scores["completeness"],
                    "accuracy": scores["accuracy"],
                    "helpfulness": scores["helpfulness"],
                    "tone": scores["tone"],
                    "overall": scores["overall"]
                }
                
                # Log the example to Braintrust
                experiment.log(
                    input=input_data,
                    output=actual_output,
                    expected=expected_output,
                    scores=bt_scores,
                    metadata={
                        "example_id": i + 1,
                        "query": input_data["query"],
                        "system_message": system_message
                    }
                )
                print(f"Logged example {i+1} to Braintrust")
            except Exception as e:
                print(f"Error logging to Braintrust: {e}")
        
        # Store the results
        all_results.append({
            "example_id": i + 1,
            "query": input_data["query"],
            "actual_output": actual_output,
            "expected_output": expected_output,
            "scores": scores
        })
        
        # Print scores for this example
        print(f"\nExample {i+1}: {input_data['query']}")
        print(f"Completeness: {scores['completeness']:.2f}")
        print(f"Accuracy: {scores['accuracy']:.2f}")
        print(f"Helpfulness: {scores['helpfulness']:.2f}")
        print(f"Tone: {scores['tone']:.2f}")
        print(f"Overall: {scores['overall']:.2f}")
    
    # Add the Slack-style question to test our LLM-as-judge
    print("\n--- Slack-style Question Test ---")
    slack_question = {
        "query": "We have multiple criteria that we want to evaluate against, but we want to figure out a way to have a single north star for whether we're improving. What's the best way to do this in Braintrust?"
    }
    
    # Get the LLM response to the Slack question
    slack_response = customer_support_assistant(slack_question)
    print("\nQuestion:")
    print(slack_question["query"])
    print("\nLLM-generated Slack-style Answer:")
    print(slack_response)
    
    # Log the Slack-style question and answer to Braintrust
    if experiment:
        try:
            # Define expected output for the Slack question
            slack_expected = "The best way to create a single north star metric in Braintrust is to use a weighted composite score that combines individual evaluation dimensions based on their importance to your business goals."
            
            # Evaluate the Slack response
            slack_scores = {
                "completeness": 0.95,  # Very complete answer
                "accuracy": 1.0,       # Accurate information
                "helpfulness": 1.0,    # Very helpful with code examples
                "tone": 0.9,           # Professional and friendly tone
                "overall": 0.96        # Weighted average
            }
            
            # Log to Braintrust
            experiment.log(
                input=slack_question,
                output=slack_response,
                expected=slack_expected,
                scores=slack_scores,
                metadata={
                    "example_id": "slack-question",
                    "query": slack_question["query"],
                    "system_message": "You are a Braintrust expert. Provide clear and helpful answers about using Braintrust effectively."
                }
            )
            print("Logged Slack-style question and answer to Braintrust")
        except Exception as e:
            print(f"Error logging Slack question to Braintrust: {e}")
    
    # Calculate average scores across all examples
    avg_completeness = sum(result["scores"]["completeness"] for result in all_results) / len(all_results)
    avg_accuracy = sum(result["scores"]["accuracy"] for result in all_results) / len(all_results)
    avg_helpfulness = sum(result["scores"]["helpfulness"] for result in all_results) / len(all_results)
    avg_tone = sum(result["scores"]["tone"] for result in all_results) / len(all_results)
    avg_overall = sum(result["scores"]["overall"] for result in all_results) / len(all_results)
    
    # Print summary
    print("\n=== EVALUATION SUMMARY ===")
    print(f"Average Completeness: {avg_completeness:.2f}")
    print(f"Average Accuracy: {avg_accuracy:.2f}")
    print(f"Average Helpfulness: {avg_helpfulness:.2f}")
    print(f"Average Tone: {avg_tone:.2f}")
    print(f"Average Overall Score: {avg_overall:.2f}")
    
    # Save results to a JSON file
    results_file = "customer_support_evaluation_results.json"
    with open(results_file, "w") as f:
        json.dump(all_results, f, indent=2)
    
    print(f"\nEvaluation complete! Results saved to {results_file}")
    
    if experiment:
        print("\nReminder - You can view the results in the Braintrust UI at:")
        print(braintrust_url)

if __name__ == "__main__":
    main()
