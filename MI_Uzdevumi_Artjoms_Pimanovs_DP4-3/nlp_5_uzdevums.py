# Uzdevums 5: Teksta tīrīšana un normalizēšana

# Uzdevums:
# Noņem liekos simbolus (piemēram, @, #, !!!, URL).
# Pārveido tekstu uz mazajiem burtiem.
# Izveido tīru un viegli lasāmu tekstu.

import re

string  = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

string = string.lower()

string = re.sub(r'http\S+', '', string)

string = re.sub(r'[@#?!.,:;\'\"👏👏👏]+', '', string)

string = ' '.join(string.split())

string = string.strip()

print(string)
