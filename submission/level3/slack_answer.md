# Comprehensive Slack-style Answers to Customer Questions

## Question 1: Evaluation Metrics
"We're evaluating customer support responses. What metrics should we use to evaluate them?"

### Answer
👋 Great question about evaluating customer support responses! Based on our experience, here are the key metrics you should consider:

#### 1. Completeness (30% weight)
This measures whether the response addresses all parts of the customer's query.
- **Why it matters**: Incomplete answers lead to follow-up questions and customer frustration
- **How to measure**: Check if the response addresses all key aspects of the query
- **Implementation tip**: Create a list of essential points for each query type and verify coverage

#### 2. Accuracy (40% weight)
This evaluates whether the information provided is correct and aligned with your company's policies.
- **Why it matters**: Inaccurate information damages trust and can create legal/compliance issues
- **How to measure**: Compare against known correct answers or company documentation
- **Implementation tip**: Maintain a "golden dataset" of verified correct responses for common questions

#### 3. Helpfulness (20% weight)
This assesses whether the response provides actionable information that helps solve the customer's problem.
- **Why it matters**: The ultimate goal is to help customers solve their problems
- **How to measure**: Evaluate if the response provides clear next steps or solutions
- **Implementation tip**: Include specific action items in your evaluation criteria

#### 4. Tone (10% weight)
This checks if the response maintains a professional, friendly, and empathetic tone.
- **Why it matters**: Tone affects customer satisfaction and brand perception
- **How to measure**: Look for polite language, positive phrasing, and appropriate formality
- **Implementation tip**: Create a checklist of tone indicators (e.g., greeting, empathy statements)

These four dimensions provide a comprehensive framework for evaluating customer support responses! 📊

---

## Question 2: North Star Metric
"We have multiple criteria that we want to evaluate against, but we want to figure out a way to have a single north star for whether we're improving. What's the best way to do this in Braintrust?"

### Answer
👋 Great question about creating a "north star" metric while evaluating against multiple criteria!

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

Hope that helps! Let me know if you have any other questions. 🚀
