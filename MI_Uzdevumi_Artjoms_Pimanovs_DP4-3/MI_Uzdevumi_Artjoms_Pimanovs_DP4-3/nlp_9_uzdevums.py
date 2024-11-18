# Uzdevums 9: Teksta ģenerēšana
# Uzdevums:
# Izveido tekstu ģenerēšanas modeli, kas turpina šo frāzi un izveido īsu stāstu (3-4 teikumi).

from translate import Translator
from transformers import pipeline

translator_to_en = Translator(from_lang="lv", to_lang="en")
translator_to_lv = Translator(from_lang="en", to_lang="lv")

start_phrase = "Reiz kādā tālā zemē dzīvoja pūķis."
translated_phrase = translator_to_en.translate(start_phrase)

generator = pipeline("text-generation", model="gpt2")
result = generator(
    translated_phrase,
    max_length=60,
    num_return_sequences=1,
    temperature=1.2,
    truncation=True
)

generated_text_en = result[0]["generated_text"]
translated_back = translator_to_lv.translate(generated_text_en)

print("Original (Latvian):", start_phrase)
print("\n\nGenerated (English):", generated_text_en)
print("\n\nTranslated back to Latvian:", translated_back)
