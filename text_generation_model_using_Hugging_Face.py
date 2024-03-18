import requests

# Access the API key correctly
api_key = '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'

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {api_key}"}  # Use f-string for formatting

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

while True:  # Create an infinite loop for continuous interaction
    question = input("Ask Your Question: ")

    response_data = query({"inputs": question})

    # Access the answer correctly
    try:
        answer = response_data[0]['generated_text']
        print("Answer:", answer)
    except IndexError:
        print("Error: API response does not contain the expected structure.")
