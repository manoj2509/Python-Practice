__author__ = 'Mj'
import sys
import math

s = input().strip()
s.replace(" ", "")
st = list()
r = math.floor(math.sqrt(len(s)))
c = math.ceil(math.sqrt(len(s)))
text = [[0 for j in range(0,c)] for i in range(0,r)]
text2 = [[0 for j in range(0,r)] for i in range(0,c)]
for i in range(r):
    text[i].append(s[(8*i):(8*(i+1))])
for i in range(r):
    for j in range(c):
        text2[j].append(text[i][j])
    print(text2[i], end=' ')