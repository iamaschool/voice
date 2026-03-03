from system import rate_system as rate
libs = ["f5", "gtts", "etts", "qwen3", "sys", "gradio", "gradioapi"]
score = rate()
try:
    response = requests.get("https://example.com", timeout=5)
    wifi =  True
except requests.RequestException:
    wifi = False

if score < 4:
    libs.remove("f5", "qwen3", "gradio")
if not wifi:
    libs.remove("gtts", "etts", "gradioapi")

def select(language, text, strain):
    for lib in libs:
        import lib
        if language not in lang():
            libs.remove(lib)
    strain = round(strain/len(libs))
    lib = libs[strain]
    from lib import lib
    lib(language)