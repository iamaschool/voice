import sys
import subprocess
from pathlib import Path
ref_path = Path("./dataset/reference.wav")

try:
    from gradio_client import Client, handle_file
except ImportError:
    print("gradio_client not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gradio_client"])
    from gradio_client import Client, handle_file

languages = ["en"]

def lang():
    return languages

def gradioapi(language, text, filename, url):
    if language not in languages:
        raise ValueError(f"Unsupported language: {language}. Supported languages are: {', '.join(languages)}")
    client = Client(url)
    result = client.predict(
        ref_audio=handle_file("reference.wav"),
        ref_text="Reference audio transcript",
        gen_text=text,
        remove_silence=False,
        api_name="/predict"
    )
    temp_audio_path = result[0] if isinstance(result, tuple) else result
    final_name = f"{filename}.mp3"
    import shutil
    shutil.move(temp_audio_path, final_name)
    
    return final_name