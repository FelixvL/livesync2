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
      "content": '''
      JIJ BENT ONDERDEEL VAN EEN SYSTEEM.

      ANTWOORD ALLEEN IN JSON 
      '''+invoer+''' 
      
      '''
    }],
    temperature=1.8,
    max_completion_tokens=1024
)

# print(completion)
print(completion.choices[0].message.content)