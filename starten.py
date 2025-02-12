from openai import OpenAI
import geheim

client = OpenAI(api_key=geheim.key())

# https://audio-samples.github.io/#section-1

audio_file = open("geluid.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1",
  file=audio_file
)

print(transcript)