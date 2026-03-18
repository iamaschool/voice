import subprocess
engine = pyttsx3.init()
voices = engine.getProperty('voices')
languages = [voice.languages[0].decode('utf-8') for voice in voices]
def lang():
    return languages
def gtts(language, text, filename):
    try:
        import pyttsx3
    except ImportError:
        print("edge-tts not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyttsx3"])
        import pyttsx3
    if language not in languages:
        raise ValueError(f"Unsupported language: {language}. Supported languages are: {', '.join(languages)}")
    # Specify the language (e.g., 'en' for English) and set speed (False for normal, True for slow)
    tts = gTTS(text=text, lang=language, slow=False)
    file_name = f"{filename}.mp3"
    tts.save(file_name)
    return f"{file_name}"
