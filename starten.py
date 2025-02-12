import os
import openai

import geheim


from openai import OpenAI
client = OpenAI(api_key=geheim.key())
invoer = input("Noem een land ")
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[{
      "role": "system",
      "content": ''' Ik wil de hoofdstad weten van: '''+invoer+''' als je vermoed dat het land niet bestaat, zeg dat dan'''
    }],
    temperature=0.8,
    max_completion_tokens=1024
)

# print(completion)
print(completion.choices[0].message.content)