# Uzdevums 2: Teksta valodas noteikšana

# Uzdevums:
# Izveido programmu, kas nosaka, kurā valodā ir katrs teksts. Izmanto bibliotēku vai algoritmu, kas ļauj identificēt valodu.


from langdetect import detect
from langdetect import detect_langs

string_lv = "Šodien ir saulaina diena."
string_en = "Today is a sunny day."
string_ru = "Сегодня солнечный день."

language = detect(string_lv.lower())
print(string_lv, language)

# Nezinu kapēc šo izvada kā Somali valodu

language = detect_langs(string_en.lower())
print(string_en, language)

language = detect(string_ru.lower())
print(string_ru, language)
