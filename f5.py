from pathlib import Path
ref_path = Path("./dataset/reference.wav")
try:
    from f5_tts.infer import TTS
except ImportError:
    print("edge-tts not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "f5-tts"])
    from f5_tts.infer import TTS
languages = ["en", "zh"]
def f5(language, text, filename):
    if language not in languages:
        raise ValueError(f"Unsupported language: {language}. Supported languages are: {', '.join(languages)}")
    tts = TTS(model_name="F5TTS_v1_Base", device="cuda")
    audio = tts.synthesize(
        text=text,
        reference_audio_path=ref_path,
        reference_text="Reference audio transcript"
    )
    filename = f"{filename}.mp3"
    audio.save(filename)
    return filename