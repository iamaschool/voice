from pydoc import text
from system import rate_system as rate
import importlib
import requests
import random
import os
import sys
from lingua import Language, LanguageDetectorBuilder
from nltk.tokenize import sent_tokenize
from pydub import AudioSegment

try:
    from ftlangdetect import detect
except ImportError:
    print("edge-tts not found. Installing...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fasttext-langdetect"])
    from ftlangdetect import detect

libs = ["sys", "gtts", "etts", "f5", "qwen3", "gradioapi"]
score = rate()
try:
    response = requests.get("https://example.com", timeout=5)
    wifi =  True
except requests.RequestException:
    wifi = False

if score < 4:
    badlist = ["f5", "qwen3"]
    for bad in badlist:
        libs.remove(bad)
if not wifi:
    badlist = ["gtts", "etts", "gradioapi"]
    for bad in badlist:
        libs.remove(bad)
#intead of using strain strain has to narrow down the list so only the lnaguages can be picked form the numbers after the list for every language a lib closest to the tob has to be picked out that slanguage list contains the language and then use that lib to generte the text.
def auto(text, strain, filename):
    global languagetext
    filenames = []
    strain = round(strain/len(libs))
    libs = libs[:strain]
    for langtext in languagetext:
        sentence, language = langtext.split(":")
        for libname in libs:
            lib = getattr(importlib.import_module(libname), libname)
            lang = getattr(lib, "lang")
            if language in lang():
                filename = lib(language, sentence, filename)
                filenames.append(filename)
                break
        libname = libs[0]
        lib = getattr(importlib.import_module(libname), libname)
        lang = getattr(lib, "lang")
        filename = lib(language, sentence, filename)
        filenames.append(filename)
    #libname = libs[strain]
    #lib = getattr(importlib.import_module(libname), libname)

    #languages = detect(text)
    #for language in languages:
    #    sentence, lang = language.split(":")
    #    filenames.append(lib(lang, sentence, filename))
    audio = filenames[0]
    for filename in filenames[1:]:
        audio += filename
    audio.export(filename, format="mp3")
    for filename in filenames:
        os.remove(filename)
    return filename

def select(text, filename, gradiopi = 'False', libname = None):
    global languagetext
    languagetext = detect(text)
    languages = []
    for language in languagetext:
        sentence, lang = language.split(":")
        languages.append(lang)
    liblangs = []
    for libname in libs:
            lib = importlib.import_module(libname)
            lang = getattr(lib, "lang")
            liblangs.append(f"{libname}:{lang()}")
    for l in liblangs:
        sentence, language = language.split(":")
        libname, lang = l.split(":")
        for lan in lang:
            if lan in languages:
                pass
        else:
            libs.remove(libname)
    if gradiopi == 'False':
        libs.remove('gradioapi')
    if libname not in libs:
        filename = auto(language, text, libs.index(libname), filename)
    else:
        libname = libs[libs.index(libname)]
        lib = getattr(importlib.import_module(libname), libname)
        filename = lib(language, text, filename)
        name = f"{random.uniform(1, 10)}.{filename.split(".")[1]}"
        os.rename(filename, name)
    return name

def language(text):
    text = sent_tokenize(text)
    languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
    detector = LanguageDetectorBuilder.from_languages(*languages).build()
    langtext = []
    for i, sentence in enumerate(text):
        if detector.detect_language_of(text) == None:
            detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()
        langtext.append(f"{sentence}:{detector.detect_language_of(sentence).iso_code_639_1.name.lower()}")
    return langtext

