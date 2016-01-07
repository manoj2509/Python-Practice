__author__ = 'Mj'
import math
n = int(input())
text = [[] for i in range(n)]
for i in range(n):
    text[i] = input().split(" ")
for i in range(n):
    #for j in range(int(text[i][0]), int(text[i][1])):
    temp1 = int(math.sqrt(int(text[i][0])))
    temp2 = int(math.sqrt(int(text[i][1])))

    if (temp1 - math.sqrt(int(text[i][0]))) == 0.0:
        print(temp2 - temp1 + 1)
    else:
        print(temp2 - temp1)
