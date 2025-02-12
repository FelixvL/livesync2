from openai import OpenAI
import geheim

client = OpenAI(api_key=geheim.key())

invoer = input("Stel hier uw vraag? ")
response = client.chat.completions.create(
  model="gpt-4o",
  messages=[{
      "role": "system",
      "content": ""+invoer
    }],
    temperature=0.7,
    max_tokens=5000
   # stream=True
)
print(chunk.choices[0].delta.content)
#for chunk in response:
 #   print(chunk.choices[0].delta.content, end="", flush=True)