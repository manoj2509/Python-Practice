__author__ = 'Mj'
n = int(input())
text = [[]for i in range(150)]
timing = [[]for j in range(150)]
count = list()
for i in range(0, n):
    text[i] = input().split(" ")
    timing[i] = input().split(" ", maxsplit=int(text[i][0]))
    coot = 0
    for j in range(0, int(text[i][0])):
        if int(timing[i][j]) <= 0:
            coot += 1
    count.append(coot)
for i in range(0, n):
    if count[i] < int(text[i][1]):
        print("YES")
    else:
        print("NO")