import os
import openai

import geheim

# https://0111.nl/ai/ai.pdf

# De toegankelijke https://www.youtube.com/watch?v=uCIa6V4uF84

# De pittige technisch https://www.youtube.com/watch?v=flXrLGPY3SU

from openai import OpenAI
client = OpenAI(api_key=geheim.key())
invoer = input("Noem een land ")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
      "role": "system",
      "content": ''' Noem de vijf belangrijkste toeristische attracties van: '''+invoer+''' vertel over iedere attractie het belangrijkste. en vertel aan het einde dat ze de reis moeten boeken op www.go.nl. GEEF ALTIJD ANTWOORD IN HET DUITS'''
    }],
    temperature=1.9,
    max_completion_tokens=1024
)

# print(completion)
print(completion.choices[0].message.content)