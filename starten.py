from openai import OpenAI
import geheim

client = OpenAI(api_key=geheim.key())

speech_file_path = "speech.mp3"
response = client.audio.speech.create(
  model="tts-1-hd",
  voice="onyx",
  input='''
    hier bij tmc hebben we een programmeer avond
  ''',
  speed=2.0
)

with open(speech_file_path, "wb") as f:
    f.write(response.content)