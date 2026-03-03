https://github.com/QwenLM/Qwen3-TTS?tab=readme-ov-file#python-package-usage

pyttsx3

from gradio_client import Client, handle_file
# Initialize the client with the space ID or URL
# In this case, we use a space ID "abidlabs/whisper"
client = Client("abidlabs/whisper")

# Call the predict method with the input (an audio file)
# The `handle_file` utility helps manage file inputs
result = client.predict(
    audio=handle_file("audio_sample.wav"),
    api_name="/predict" # api_name might be optional for simple apps, but is a good practice
)

print(result)
# Expected output: "This is a test of the whisper speech recognition model."