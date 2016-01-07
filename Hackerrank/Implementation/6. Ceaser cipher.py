__author__ = 'Mj'
text1 = list()
length = int(input())
text = input()
k = int(input())
for i in range(0, length):
    val = ord(text[i])

    if val in range(65, 91):
        val += k
        if val > 90:
            val -= 26

    elif val in range(97, 123):
        val += k
        if val > 122:
            val -= 26

    text1.append(chr(val))
#''.join(text1)
#print(text1)
for a in text1:
    print (a, end='')