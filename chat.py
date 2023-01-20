import openai 
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("api_key")

conversation =""

i = 1

while (i !=0):
    question =input("User: ")
    conversation += "\nUser: " + question + "\nAI:"
    response = openai.Completion.create(
        model = "davinci",
        prompt = conversation,
        temperature = 0.1,
        max_tokens = 60,
        top_p = 1.0,
        frequency_penalty = 0.5,
        presence_penalty = 0.0,
        stop =["\n", "User: ", "AI:"]
    )
    answer = response.choices[0].text.strip()
    conversation += answer
    print("AI:" + answer + "\n")