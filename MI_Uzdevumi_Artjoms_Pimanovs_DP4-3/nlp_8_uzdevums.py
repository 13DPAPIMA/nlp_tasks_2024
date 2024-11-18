# Uzdevums 8: Frāžu atpazīšana (NER)
# Uzdevums:
# Izveido programmu, kas identificē šādas īpašas vienības tekstā:
# Personvārdi (piemēram, Egils Levits).
# Organizācijas (piemēram, Latvijas Universitāte). 


import re
import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("maxent_ne_chunker")
nltk.download("words")

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

tokens = word_tokenize(text)
pos_tags = pos_tag(tokens)
ner_tree = ne_chunk(pos_tags)


names = []
possible_organizations = []

for subtree in ner_tree:
    if hasattr(subtree, 'label'):
        entity = ' '.join(c[0] for c in subtree)  
        label = subtree.label() 
        if label == "PERSON":
            names.append(entity)
        elif label == "ORGANIZATION":
            possible_organizations.append(entity)

def find_organizations_with_regex(text, names):

    found = re.findall(r'[A-ZĀČĒĢĪĶĻŅŠŪŽ][a-zāčēģīķļņšūž]+(?:\s[A-ZĀČĒĢĪĶĻŅŠŪŽ][a-zāčēģīķļņšūž]+)+', text)
    return [org for org in found if org not in names]

organizations = find_organizations_with_regex(text, names)

organizations = list(set(possible_organizations + organizations))

organizations = [org for org in organizations if org not in names]

print("Names:")
print(names)
print("\nOrganisation:")
print(organizations)
