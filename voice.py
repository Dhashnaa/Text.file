
from google.cloud import speech_v1p1beta1 as speech
from google.oauth2 import service_account

# Set up credentials
credentials = service_account.Credentials.from_service_account_file(
    'path/to/your/service-account-key.json')

# Set up the Speech-to-Text client
client = speech.SpeechClient(credentials=credentials)

# Load the audio file
with open('path/to/your/audio-file.wav', 'rb') as audio_file:
    content = audio_file.read()

# Configure the request
audio = speech.RecognitionAudio(content=content)
config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US',
)

# Make the request
response = client.recognize(config=config, audio=audio)

# Print the transcription
for result in response.results:
    print(result.alternatives[0].transcript)