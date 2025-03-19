from deep_translator import GoogleTranslator

french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]

translated_dict = {}
for word in french_words:
    translation = GoogleTranslator(source='fr', target='en').translate(word)
    translated_dict[word] = translation

print(translated_dict)