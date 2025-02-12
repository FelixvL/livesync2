from openai import OpenAI
import webbrowser
import geheim

client = OpenAI(api_key=geheim.key())

invoer = input("Waar wil je een afbeelding over? ")
for x in range(10):
    response = client.images.generate(
    model="dall-e-3",
    prompt=''''''+invoer+'''''',
    n=1,
    size="1792x1024",
    style="vivid",
    quality="hd"
    )

    print(response)
    webbrowser.open(response.data[0].url)