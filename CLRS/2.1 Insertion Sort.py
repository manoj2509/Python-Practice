__author__ = 'Mj'
text = input().strip().split(' ')
for i in range(1, len(text)):
    val = int(text[i])
    key = i
    while(key > 0 and int(text[key-1]) < val):
        text[key] = int(text[key - 1])
        key = key - 1
    text[key] = val
print(text)