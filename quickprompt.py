import requests
import os

def quickprompt(prompt):
    """
    Sends a prompt to the Anthropic Haiku model and returns the response.

    Args:
        prompt (str): The prompt to send to the Haiku model.

    Returns:
        str: The response from the Haiku model.
        ANTHROPIC_API_KEY

    curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
        '{
            "model": "claude-3-opus-20240229",
            "max_tokens": 1024,
            "messages": [
                {"role": "user", "content": "Hello, world"}
            ]
        }'
    """
    # Set up the request headers and payload
    headers = {
        "content-type": "application/json",
        "anthropic-version": "2023-06-01",
        "x-api-key": os.environ.get('ANTHROPIC_API_KEY')
    }
    payload = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Send the request to the Anthropic API
    response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract and return the response from the model
        return response.json()['content'][0]['text']
    else:
        # Handle the error
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example usage
email_content="Hello my name is John Doe, My number is 555-123-1234 and my email is john.doe@example.com, please send me information on your ABC Widget"
my_prompt = f"Extract information from this source data: {email_content}"
output_format = """
output in this json format:
{
    "name": "<extracted name here>",
    "telephone": "<extracted telephone here>",
    "email": "<extracted email address here>"
}
"""
my_prompt=f"{my_prompt}\n{output_format}"
extracted_information = quickprompt(my_prompt)
if extracted_information:
    print(extracted_information)
