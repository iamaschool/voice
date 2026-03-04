from fast_langdetect import detect_multilingual

text = "გამარჯობა! ሠላም བཀྲ་ཤིས་བདེ་ལེགས། ᖁᕕᐊᓇᖅ नमस्ते สวยงาม"
# k=5 tells the model to return the top 5 most likely languages found
results = detect_multilingual(text, k=5)
print(results)