from system import rate_system as rate
import importlib
import requests
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

def auto(language, text, strain, filename):
    strain = round(strain/len(libs))
    libname = libs[strain]
    lib = getattr(importlib.import_module(libname), libname)
    return lib(language, text, filename)

def select(libname, language, text, filename, gradiopi = 'False'):
    for lib in libs:
        lib = importlib.import_module(lib)
        lang = getattr(lib, "lang")
        if language not in lang():
            libs.remove(lib)
    if gradiopi == 'False':
        libs.remove('gradioapi')
    if libname not in libs:
        filename = auto(language, text, libs.index(libname), filename)
    else:
        libname = libs[libs.index(libname)]
        lib = getattr(importlib.import_module(libname), libname)
        filename = lib(language, text, filename)
    return filename