import subprocess
import sys
try:
    import pyttsx3
except ImportError:
    print("edge-tts not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3"])
    import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
languages = [voice.languages[0].decode('utf-8') for voice in voices]
def lang():
    return languages
def sysvc(language, text, filename):
    filename = "gg.mp3"
    return f"{file_name}"
