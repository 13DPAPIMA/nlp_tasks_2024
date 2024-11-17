# Uzdevums 3: Vārdu sakritību pārbaude divos tekstos

# Uzdevums:
# Izveido programmu, kas:
# Identificē vārdu sakritību starp abiem tekstiem.
# Aprēķina, cik procentuāli liels ir sakritības līmenis.


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

text1_tokens = set(word_tokenize(text1.lower()))
text2_tokens = set(word_tokenize(text2.lower()))

common_words = text1_tokens & text2_tokens

total_unique_words = len(text1_tokens | text2_tokens)

similarity = (len(common_words) / total_unique_words) * 100


print(f" Vienādi vārdi tekstos ir {common_words} ")
print(f"\n Teksti is vienādi uz {round(similarity)} procentiem")

