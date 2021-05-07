from collections import deque
import ConvertText as conv

million = []
thousand = []
hundred = []
money = input("Money: ")
separate = money.split(',')
before_comma = deque(separate[0])
after_comma = deque(separate[1])
after_comma.appendleft("0")
for _ in range(len(before_comma), 9):
    before_comma.appendleft("0")

million = [before_comma[i] for i in range(0, 3)]
thousand = [before_comma[i] for i in range(3, 6)]
hundred = [before_comma[i] for i in range(6, 9)]
cents = [after_comma[i] for i in range(0, 3)]

print(million)
print(thousand)
print(hundred)
print(cents)
"""
print(conv.base_convert(million))
print(conv.base_convert(thousand))
print(conv.base_convert(hundred))
print(conv.base_convert(cents))
"""
# Conversão de array de número para array com as palavras de cada número
million_base = conv.base_convert(million)
thousand_base = conv.base_convert(thousand)
hundred_base = conv.base_convert(hundred)
cents_base = conv.base_convert(cents)

print("Conversão de array de número para array com as palavras de cada número")
print(million_base)
print(thousand_base)
print(hundred_base)
print(cents_base)

# transformando o array de palavras na frase que representa o número
million_as_phrase = conv.base_transform_phrase(conv.base_convert(million))
thousand_as_phrase = conv.base_transform_phrase(conv.base_convert(thousand))
hundred_as_phrase = conv.base_transform_phrase(conv.base_convert(hundred))
cents_as_phrase = conv.base_transform_phrase(conv.base_convert(cents))

print("transformando o array de palavras na frase que representa o número")
print(million_as_phrase)
print(thousand_as_phrase)
print(hundred_as_phrase)
print(cents_as_phrase)

million_final_phrase = conv.million_phrase(million_base, thousand_base, hundred_base, million_as_phrase)
print(million_final_phrase)
thousand_final_phrase = conv.thousand_phrase(million_base, thousand_base, hundred_base, thousand_as_phrase)
print(thousand_final_phrase)
hundred_final_phrase = conv.hundred_phrase(million_base, thousand_base, hundred_base, hundred_as_phrase)
print(hundred_final_phrase)
cents_final_phrase = conv.cents_phrase(cents_base, cents_as_phrase)
print(cents_final_phrase)

print("Frase final")

final_phrase = ""
if million_final_phrase:
    if not thousand_final_phrase and not hundred_final_phrase:
        final_phrase += million_final_phrase + "reais"
    else:
        final_phrase += million_final_phrase + " "

if thousand_final_phrase:
    final_phrase += thousand_final_phrase + " "

if hundred_final_phrase:
    if not len(million_final_phrase) and not len(thousand_final_phrase):
        if hundred_final_phrase == "um":
            final_phrase += hundred_final_phrase + " real"
        else:
            final_phrase += hundred_final_phrase + " "
    else:
        final_phrase += hundred_final_phrase + " "

if "reais" in final_phrase or "real" in final_phrase:
    pass
else:
    final_phrase += "reais"

if cents_final_phrase:
    final_phrase += " e " + cents_final_phrase

print(final_phrase)
