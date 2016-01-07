__author__ = 'Mj'
n = int(input())
text = [[] for j in range(n)]
for i in range(0, n):
    text[i] = int(input())
for i in range(0, n):
    div = int(text[i] / 5)
    while div > 0:
        if (text[i] - (5 * div)) % 3 == 0:
            for j in range(0, text[i] - (5 * div)):
                print('5', end='')
            for j in range(0, 5 * div):
                print('3', end='')
            div = -1
            print('')
        else:
            div -= 1
    if text[i] % 3 == 0:
        for j in range(0, text[i]):
            print('5', end='')
        print('')
    elif div == 0:
        print(-1)