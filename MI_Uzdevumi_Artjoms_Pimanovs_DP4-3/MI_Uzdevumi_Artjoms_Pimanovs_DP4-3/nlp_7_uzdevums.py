# Uzdevums 7: Vārdu iegulšana (word embeddings)

# Uzdevums:
# Izmanto vārdu iegulšanas modeli, lai:
# Iegūtu katra vārda vektoru.
# Salīdzinātu, kuri vārdi ir semantiski līdzīgāki.



from gensim.models import Word2Vec
import gensim
from nltk.tokenize import word_tokenize
import warnings

warnings.filterwarnings(action='ignore')

words = ["māja", "dzīvoklis", "jūra"]

corpus = [
    ["māja", "cilvēki", "dzīvo", "tur"],
    ["dzīvoklis", "mazs", "bet", "ērts"],
    ["jūra", "plaša", "dziļa", "un", "skaista"],
    ["māja", "un", "dzīvoklis", "ir", "mājokļi"]
]

model = gensim.models.Word2Vec(corpus, min_count=1, vector_size=100, window=5)

print("Word vectors:")
for word in words:
    print(f"Word '{word}': {model.wv[word][:5]}...")  

similarity_māja_dzīvoklis = model.wv.similarity("māja", "dzīvoklis")
similarity_māja_jūra = model.wv.similarity("māja", "jūra")
similarity_dzīvoklis_jūra = model.wv.similarity("dzīvoklis", "jūra")

print("\nSemantic similarity:")
print(f"Similarity between 'māja' and 'dzīvoklis': {similarity_māja_dzīvoklis:.4f}")
print(f"Similarity between 'māja' and 'jūra': {similarity_māja_jūra:.4f}")
print(f"Similarity between 'dzīvoklis' and 'jūra': {similarity_dzīvoklis_jūra:.4f}")
