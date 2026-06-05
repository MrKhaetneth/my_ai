import os 
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv("apikey.env")

hf_key = os.getenv("hf_key")
print(f"First five letters of HF API key: {hf_key[:5]}")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=hf_key,
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-R1",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
    max_tokens = 150 # Force it to reply in less than 150 tokens (1 token approx 0.75 word)
)

print(completion.choices[0].message)

#First five letters of HF API key: hf_vH
#ChatCompletionMessage(content="\nThe capital of France is **Paris**.  \n\nParis is not only the political center of France, housing key institutions like the French President's residence (Élysée Palace) and the National Assembly, but also a global hub for art, fashion, cuisine, and culture. Iconic landmarks such as the Eiffel Tower, Louvre Museum, and Notre-Dame Cathedral are located there.  \n\nLet me know if you'd like more details! 😊", refusal=None, role='assistant', annotations=None, audio=None, function_call=None, tool_calls=None, reasoning_content='Okay, the user is asking "What is the capital of France?" That seems straightforward. Let me quickly confirm the answer: Paris is indeed the capital, and it\'s common knowledge.  \n\nHmm, the user might be a student doing homework, a traveler planning a trip, or someone testing basic knowledge. Since the question is simple, they probably want a quick, clear answer without extra fluff.  \n\nBut just to be helpful, I\'ll add a tiny bit of context—mentioning it\'s France\'s political and cultural hub—in case they\'re curious why Paris matters. No need to overload them with history though; the Eiffel Tower reference feels like a friendly touch that makes it feel human.  \n\n...Wait, should I worry they\'re testing if I\'m a bot? Nah, even if they are, a correct answer with light warmth would pass. Keeping it concise but not robotic.  \n\nFinal check: Yes, Paris. No complications here. Just deliver it cleanly.\n')

# To get only the content, just type completion.choices[0].message.content

# https://huggingface.co/deepseek-ai/DeepSeek-R1
# https://colab.research.google.com/#scrollTo=L3h5427nxXeh&fileId=https%3A//huggingface.co/deepseek-ai/DeepSeek-R1.ipynb