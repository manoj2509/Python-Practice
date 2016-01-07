__author__ = 'Mj'

n = int(input())
d1 = d2 = 0
text = [[]for i in range(n)]
for i in range(0, n):
    text[i] = [[] for k in range(n)]
    text[i] = input().split(' ')
for i in range(0, n):
    d1 += int(text[i][i])
    d2 += int(text[i][n-i-1])
print(abs(d1-d2))