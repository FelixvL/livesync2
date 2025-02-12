import os
import openai
import geheim

from openai import OpenAI
client = OpenAI(api_key=geheim.key())

with open("films.csv", "r") as file:
    file_content = file.read()

# print(file_content)

vraag = input("stel een vraag over het bestand: ")
response = client.chat.completions.create(
    model="gpt-4o",
    # model="o3-mini",
    # reasoning_effort="medium",
    messages=[
        {"role": "system", "content": "Dit is de inhoud van het bestand: " + file_content},
        {"role": "user", "content": vraag}
    ],
    temperature=0.7,
    max_completion_tokens=15000,
)

# print(response)
print(response.choices[0].message.content)