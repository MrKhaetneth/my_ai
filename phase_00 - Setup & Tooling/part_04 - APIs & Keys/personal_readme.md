# What is API? (The Waiter)

**API** stands for **Application Programming Interface**. In simple terms, it is a software intermediary that allows two different applications to talk to each other.

The Restaurant Analogy: Imagine you are sitting at a restaurant table looking at a menu. The kitchen (the server/database) has the ingredients and the ability to cook your food. However, you aren't going to walk into the kitchen and shout your order at the chefs. Instead, you tell the waiter (the API) what you want. The waiter takes your order to the kitchen, and then brings the food back to you.

In programming, if your app wants to show a Google Map, it doesn't download all of Google's map data. It uses Google's API to ask for a specific map, and Google sends it back.

## What is an API Key? (The Restaurant Reservation)

An **API Key** is a long, unique string of characters given to a developer. It acts as both a unique identifier and a secret password. In the previous analogy, the API key tells the server *who* is making the request. It is also like making a reservation under our name: the restaurant knows who you are, how many times you visit, and bill your account at the end of the night. 

This key is used to track usage and prevent abuse. If a malicious programmer tries to crash a service, the server can jjust block that specific API Key.

# What is a Token? (The Wristband / Coat Check)

A **Token** (often called an **Authentication Token** or **Bearer Token**) is a highly secure, temporary piece of data generated after a user successfully logs in. While an API Key says "This is my app," a Token says "This specific user has logged in and has permission to do X, Y, and Z for the next hour."

What it does: It handles temporary authorization.

Why we need it: Security. Instead of sending your actual username and password across the internet with every single click, you log in once, get a token, and use that token for the rest of your session.

The Restaurant Analogy: Imagine you go to a VIP club inside the restaurant. You show your ID at the door, and they give you a VIP wristband (the Token). For the rest of the night, you don't show your ID to buy a drink; you just show the wristband. At the end of the night, the wristband is cut off (the token expires).

# Hugging Face API and python-dotenv

In this section of the project, I made use of the Hugging Face AI models. Hugging Face is like the "GitHub of Machine Learning." It is a massive platform where AI researchers store and share AI models. After creating an account on Hugging Face (from hereon referred to as HF), I created an API Key within the website. I will be using the DeepSeek-R1 model for this section. The process of making us of Hugging Face AI is as follows:

1. Our computer computes the code and sends a request via API Key to Hugging Face Servers;
2. The servers run DeepSeek-R1 model;
3. The servers send back AI's response into our computer.

To store my API Key safely, I created a file called `apikey.env` within `my_ai` directory. To make use of this file, I had to install a library known as `python-dotenv` via 

```bash
uv pip install python-dotenv
```

A major rule in computer science is to **NEVER** hardcode your API keys directly into your code. These `.env` files store secrets as "Environment Variables."

When I want to extract out the stored API keys within my `apikey.env` file, I just run this script in python,

```python
import os 
from dotenv import load_dotenv

# Reading .env file. The file path is relative to the root directory of this project (my_ai in this case), not relative to the location of the code files.
load_dotenv("apikey.env")

hf_key = os.getenv("HF_KEY")
```

Additionally, I also have to install `openai` library because OpenAI's syntax became the standard code format for AI, which HF also adopted.

```bash
uv pip install openai
```
