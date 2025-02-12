from openai import OpenAI
import geheim

client = OpenAI(api_key=geheim.key())

invoer = input("kies een onderwerp? ")

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[{
      "role": "system",
      "content": '''maak in html een website over: '''+invoer+''''''
    }],
    temperature=1.4,
    max_completion_tokens=5000
)

# print(completion)

print(completion.choices[0].message.content)

tekst = completion.choices[0].message.content
bestandsnaam = "voorbeeld.html"

with open(bestandsnaam, "w") as bestand:
    bestand.write(tekst)