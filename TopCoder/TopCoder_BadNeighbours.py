__author__ = 'Mj'
text = list()
text = input().split(" ")
l = len(text)
temp = list()
for i in range(0, l):
    temp.append(0)
maxdon = [0] * l
locmax = 0
for i in range(0, l):
    for j in range(0, i):
        if (temp[j-1] and temp[j+1]) == 0:
            temp[j] = 1
            locmax += int(text[j])
        if (temp[0] and temp[l-1]) == 1:
            locmax -= min(temp[0], temp[l-1])
    maxdon[i] = max(maxdon[i-1], locmax)
    print(maxdon[i])
print(maxdon[l-1])