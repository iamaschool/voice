text = """
"Hello! Bonjour! ¡Hola! Hallo!
Welcome to our global community. Es ist wunderbar, Menschen aus der ganzen Welt hier zu treffen. C'est magnifique de rencontrer des gens du monde entier ici. ¡Es maravilloso conocer gente de todo el mundo!
Today, we will share ideas. Wir möchten gemeinsam lernen und wachsen. Nous voulons apprendre et grandir ensemble. Queremos aprender y crecer juntos.
Danke, merci, gracias, and thank you for being here."""
from lingua import Language, LanguageDetectorBuilder
languages = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]
detector = LanguageDetectorBuilder.from_languages(*languages).build()
from nltk.tokenize import sent_tokenize

# 2. Split the text into a list of sentences
sentences = sent_tokenize(text)

# 3. Print or process each sentence
for i, sentence in enumerate(sentences):
    print(f"Sentence {i+1}: {sentence}")
    if detector.detect_language_of(text) == None:
        detector = LanguageDetectorBuilder.from_all_languages().with_preloaded_language_models().build()
    print(detector.detect_language_of(sentence))

