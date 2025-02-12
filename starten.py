from openai import OpenAI
import geheim

client = OpenAI(api_key=geheim.key())

invoer = input("kies een onderwerp? ")

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[{
      "role": "system",
      "content": ''''''+invoer+''''''
    }],
    temperature=0.8,
    max_completion_tokens=5000
)

# print(completion)

print(completion.choices[0].message.content)

tekst = completion.choices[0].message.content
bestandsnaam = "voorbeeld.txt"

with open(bestandsnaam, "w") as bestand:
    bestand.write(tekst)