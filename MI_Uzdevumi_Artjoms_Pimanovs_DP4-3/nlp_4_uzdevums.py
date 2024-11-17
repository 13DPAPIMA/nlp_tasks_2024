# Uzdevums 4: Noskaņojuma analīze
# Uzdevums:
# Izveido programmu, kas nosaka katra teikuma emocionālo noskaņojumu: pozitīvs, negatīvs vai neitrāls.

# Vajadzēja iztulkot, jo citadi vienmēr bija neitrāls

from deep_translator import GoogleTranslator
from nltk.sentiment import SentimentIntensityAnalyzer

translator = GoogleTranslator(source='lv', target='en')
sia = SentimentIntensityAnalyzer()

text_1_lv = "Šis produkts ir lielisks, esmu ļoti apmierināts!"
text_2_lv = "Esmu vīlies, produkts neatbilst aprakstam."
text_3_lv = "Neitrāls produkts, nekas īpašs."

text_1_en = translator.translate(text_1_lv)
text_2_en = translator.translate(text_2_lv)
text_3_en = translator.translate(text_3_lv)


sentiment = sia.polarity_scores(text_1_en)
print(f"{text_1_lv}")
print(f"Sentiment: {sentiment}")

sentiment = sia.polarity_scores(text_2_en)
print(f"{text_2_lv}")
print(f"Sentiment: {sentiment}")

sentiment = sia.polarity_scores(text_3_en)
print(f"{text_3_lv}")
print(f"Sentiment: {sentiment}")
