__author__ = 'Mj'
t = int(input())
text = [[]for i in range(t)]
for i in range(0, t):
    text[i] = int(input())
for i in range(0, t):
    count = 0
    for j in range(0, int(text[i]/2)):
        if((j*2) == text[i]):
            count += 1
        else:
            count += (text[i] - j)
    for j in range(0, int(text[i]/3)):
        if((j*3) == text[i]):
            count += 1
        else:
            count += (text[i] - j)
    for j in range(0, int(text[i]/4)):
        if((j*4) == text[i]):
            count += 1
        else:
            count += (text[i] - j)
    print(int(count)%((10**9) + 7))