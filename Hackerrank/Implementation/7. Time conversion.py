__author__ = 'Mj'

text = input().split(':')
cha = text[2]
del text[2]
text.append(cha[0:2])
text.append(cha[2:4])
if text[3] == 'PM':
    val = int(text[0])
    if val != 12:
        val += 12
        text[0] = str(val)
else:
    val = int(text[0])
    if val == 12:
        val = 0
        text[0] = str(val) + str(val)
    else:
        text[0] = str("%.2d" %val)
del text[3]
str = ":".join(text)
print(str)
