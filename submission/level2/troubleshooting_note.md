# If a customer got stuck here, what would you check first?

If a customer was having trouble creating datasets and triggering evaluations in Braintrust, I would check these things first:

1. **API Key Configuration**: Verify that the Braintrust API key is correctly set in the environment or directly in the code. Invalid or missing API keys are a common source of authentication errors.

2. **Data Format**: Check that their dataset is properly structured with the expected fields (input, expected output). Malformed data is a frequent cause of evaluation failures.

3. **Project Configuration**: Ensure they've created a project in Braintrust and are referencing it correctly in their code. Typos in project names or using non-existent projects will cause errors.

4. **SDK Version**: Confirm they're using the latest version of the Braintrust SDK, as older versions might have bugs or incompatibilities with newer Braintrust features.

5. **Network Connectivity**: Check if there are any network issues or firewall settings preventing communication with Braintrust's servers.

By addressing these common issues first, we can quickly resolve most problems customers encounter when setting up evaluations in Braintrust.
