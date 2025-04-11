# Implementation Notes and Challenges

## Challenges Encountered

1. **Braintrust SDK Initialization Parameters**: 
   - Initially had issues with the correct parameter names for initializing the Braintrust SDK
   - Had to update from using `name` to using explicit `project` parameter
   - The error messages weren't entirely clear about what parameters were expected

2. **URL Format for Viewing Results**:
   - Finding the correct URL format to view results in the Braintrust UI was challenging
   - Had to experiment with different URL structures before finding the one that worked
   - Added code to print the exact URL format to make it easier to access results

3. **LLM Integration**:
   - Implementing the LLM-generated Slack-style answer required creating a separate function
   - Had to ensure the answer was properly formatted with emojis and markdown
   - Needed to add logic to log this specific question and answer to Braintrust

## Suggestions for Documentation Improvement

1. **SDK Parameter Documentation**:
   - Clearer documentation on the required and optional parameters for `braintrust.init()`
   - Examples showing different initialization scenarios

2. **URL Structure**:
   - More explicit documentation on how to construct URLs to view experiment results
   - Examples of different URL formats for different use cases

3. **Logging Custom Evaluations**:
   - More examples of how to log custom evaluations with different score structures
   - Guidance on best practices for defining evaluation dimensions and weights

4. **UI Navigation**:
   - Better documentation on how to navigate the Braintrust UI to find experiment results
   - Screenshots or videos showing the UI navigation flow
