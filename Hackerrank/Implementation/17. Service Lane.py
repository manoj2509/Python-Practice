__author__ = 'Mj'
import sys

output = list()
n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]
    min = width[i]
    for temp in range(i+1, j+1):
        if (min > width[temp]):
            min = width[temp]
    output.append(min)
for i in range(t):
    print(output[i])