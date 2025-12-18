from openai import OpenAI

api_key="abc"


client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Leg uit wat prompt engineering is in 2 zinnen."
)

print(response.output_text)