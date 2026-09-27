from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

conversation_history = []

def chat(user_message):
    conversation_history.append({"role": "user", "content": user_message})
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "system", "content": "You are a helpful assistant."}] + conversation_history
)
    reply = response.choices[0].message.content
    conversation_history.append({"role":"assistant","content":reply})
    return reply 

print("Welcome to Chatbot")
while True:
    user_message = input("What would u like to talk about today: ")
    if user_message == "quit":
        break
    else:
        print(chat(user_message))
        



