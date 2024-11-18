# Uzdevums 1: Vārdu biežuma analīze tekstā

# Uzdevums:
# Izveido programmu, kas nosaka, cik bieži katrs vārds atkārtojas tekstā.
# Ignorē lielos burtus, lai "kaķis" un "Kaķis" tiktu uzskatīti par vienādiem.

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import FreqDist

string = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

tokens = word_tokenize(string.lower())

freq_dist = FreqDist(tokens)

print(f"{'Word':<15}{'Frequency':<10}")
print("-" * 25)
for word, frequency in freq_dist.items():
    print(f"{word:<15}{frequency:<10}")

