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
cents = after_comma
print(million)
print(thousand)
print(hundred)
print(cents)

print(conv.base_convert(million))
print(conv.base_convert(thousand))
print(conv.base_convert(hundred))
print(conv.base_convert(cents))
print(conv.base_transform_phrase(conv.base_convert(million)))
print(conv.base_transform_phrase(conv.base_convert(thousand)))
print(conv.base_transform_phrase(conv.base_convert(hundred)))

a = conv.base_transform_phrase(conv.base_convert(million))
b = conv.base_transform_phrase(conv.base_convert(thousand))
c = conv.base_transform_phrase(conv.base_convert(hundred))
print(conv.convert_million_phrase(conv.base_convert(million), a))
print(conv.convert_thousand_phrase(b))






