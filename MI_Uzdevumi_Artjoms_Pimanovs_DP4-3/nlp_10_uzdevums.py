from translate import Translator

texts_lv = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translator = Translator(from_lang="lv", to_lang="en")

translations = [translator.translate(text) for text in texts_lv]

for i, translation in enumerate(translations):
    print(f"Latviešu valodā: {texts_lv[i]}")
    print(f"Angļu valodā: {translation}\n")
