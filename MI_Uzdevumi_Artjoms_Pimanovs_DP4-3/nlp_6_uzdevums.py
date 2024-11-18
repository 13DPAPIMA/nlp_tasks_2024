# Uzdevums 6: Automātiska rezumēšana
# Uzdevums:
# Izveido programmu, kas automātiski rezumē rakstu un izceļ galvenās idejas. 


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

nltk.download('punkt')
nltk.download('stopwords')

# Pievieno latviešu stopvārdus manuāli
latvian_stopwords = [
    "ir", "un", "ka", "par", "vai", "arī", "tā", "šis", "tas", "ar", "no",
    "uz", "pie", "to", "kur", "bet", "lai", "tāpēc", "ne", "es", "tu", "viņš",
    "viņa", "mēs", "jūs", "viņi", "viņas", "tas", "šo"
]

def summarize_text(article, num_sentences=2):
    sentences = sent_tokenize(article)
    
    stop_words = set(stopwords.words('english') + latvian_stopwords)
    words = [word.lower() for word in word_tokenize(article) if word.isalnum() and word.lower() not in stop_words]
    
    word_frequencies = FreqDist(words)
    
    sentence_scores = {sentence: sum(word_frequencies[word.lower()] for word in word_tokenize(sentence) if word.lower() in word_frequencies) for sentence in sentences}
    
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    return " ".join(summarized_sentences)

article = "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."

summary = summarize_text(article)
print("Original Article:")
print(article)
print("\nSummary:")
print(summary)
