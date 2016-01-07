__author__ = 'Mj'
n = int(input())
str = list()
rstr = list()
for i in range(n):
    sta = input()
    str.append(sta)
    rstr.append(sta[::-1])
for i in range(n):
    flag = 0
    for j in range(1, len(str[i])):
        if(abs(ord(str[i][j]) - ord(str[i][j-1])) != abs(ord(rstr[i][j]) - ord(rstr[i][j-1]))):
            flag = 1
    if(flag == 0):
        print("Funny")
    else:
        print("Not Funny")