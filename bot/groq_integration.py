import os
import requests

# Ensure your API key is being loaded from the environment variable
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    print("API Key is missing!")
    exit()

# Groq API URL for content generation
groq_url = "https://api.groq.com/openai/v1/chat/completions"

# Updated model from available models
model = "mixtral-8x7b-32768"  # Replace with your chosen model

# Prepare the payload for the request
payload = {
    "model": model,
    "messages": [{"role": "user", "content": "Generate a Reddit post about AI advancements in 2025."}],
    "max_tokens": 200,
    "temperature": 0.7
}

# Headers for the request
headers = {
    "Authorization": f"Bearer {groq_api_key}",
    "Content-Type": "application/json"
}

# Send the request to Groq API for content generation
def generate_content():
    try:
        response = requests.post(groq_url, json=payload, headers=headers)

        if response.status_code == 200:
            # Print the generated content
            generated_text = response.json().get("choices", [])[0].get("message", {}).get("content", "")
            if generated_text:
                print("Generated Content:")
                print(generated_text)
            else:
                print("No content generated.")
        else:
            print(f"Error: {response.status_code}, {response.text}")
    except Exception as e:
        print("An error occurred:", e)

# Run the function to generate content
generate_content()
