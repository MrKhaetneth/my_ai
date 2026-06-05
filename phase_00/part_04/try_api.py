import os 
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv("apikey.env")

hf_key = os.getenv("hf_key")

print(f"Token loaded: {hf_key[:5]}..." if hf_key else "TOKEN IS NONE!")

client = InferenceClient(provider = "hf-inference", token = hf_key)
response = client.text_generation(
    prompt = "What is a neural network in one sentence?",
    model = "mistralai/Mistral-7B-Instruct-v0.3",
    max_new_tokens = 256,
)
print(response)

# error: Model 'mistralai/Mistral-7B-Instruct-v0.3' doesn't support task 'text-generation'. Supported tasks: 'None', got: 'text-generation'