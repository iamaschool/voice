try:
    from gtts import gTTS
except ImportError:
    print("edge-tts not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "gtts"])
    from gtts import gTTS
languages = ["af","sq","ar","hy","ca","zh-CN","zh-TW","hr","cs","da","nl","en","eo","fi","fr","de","el","ht","hi","hu","is","id","it","ja","ko","la","lv","mk","no","pl","pt","ro","ru","sr","sk","es","sw","sv","ta","th", "tr", "vi", "cy"]
def gtts(language, text, filename):
    if language not in languages:
        raise ValueError(f"Unsupported language: {language}. Supported languages are: {', '.join(languages)}")
    # Specify the language (e.g., 'en' for English) and set speed (False for normal, True for slow)
    tts = gTTS(text=text, lang=language, slow=False)
    file_name = f"{filename}.mp3"
    tts.save(file_name)
    return f"{file_name}"
