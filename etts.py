import asyncio
import subprocess

# Map short language codes to Edge voices
languages = {
    "af": "af-ZA-AdriNeural",
    "ar": "ar-SA-ZariyahNeural",
    "de": "de-DE-KatjaNeural",
    "el": "el-GR-AthinaNeural",
    "en": "en-US-AriaNeural",
    "es": "es-ES-ElviraNeural",
    "fr": "fr-FR-DeniseNeural",
    "hi": "hi-IN-SwaraNeural",
    "it": "it-IT-ElsaNeural",
    "ja": "ja-JP-NanamiNeural",
    "ko": "ko-KR-SunHiNeural",
    "nl": "nl-NL-ColetteNeural",
    "pl": "pl-PL-ZofiaNeural",
    "pt": "pt-BR-FranciscaNeural",
    "ru": "ru-RU-DariyaNeural",
    "sv": "sv-SE-SofieNeural",
    "tr": "tr-TR-EmelNeural",
    "zh-CN": "zh-CN-XiaoxiaoNeural",
    "zh-TW": "zh-TW-HsiaoChenNeural",
}

def lang():
    return languages

async def edge_tts_generate(language, text, filename):
    try:
        import edge_tts
    except ImportError:
        print("edge-tts not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "edge-tts"])
        import edge_tts
    if language not in languages:
        raise ValueError(
            f"Unsupported language: {language}. "
            f"Supported languages are: {', '.join(LANGUAGE_VOICES.keys())}"
        )

    voice = LANGUAGE_VOICES[language]
    file_name = f"{filename}.mp3"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file_name)

    return file_name