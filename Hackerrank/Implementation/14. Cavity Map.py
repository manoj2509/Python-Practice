__author__ = 'Mj'

n = int(input())
temp2 = [[0 for j in range(0,n)] for i in range(0,n)]
temp = [[0 for j in range(0,n)] for i in range(0,n)]
two_dlist = [[] for i in range(0,n)]
for i in range(0,n):
    two_dlist[i] = input()
for i in range(0, n ):
    for j in range(0, n):
        temp2[i][j] = temp[i][j] = int(two_dlist[i][j:j+1])
        two_dlist[1:]


for i in range(1, n-1):
    for j in range(1, n-1):
        if int(temp[i][j]) > int(temp[i][j+1]) and int(temp[i][j]) > int(temp[i][j-1]) and int(temp[i][j]) > int(temp[i+1][j]) and int(temp[i][j]) > int(temp[i-1][j]):
            temp2[i][j] = 'X'
        else:
            temp2[i][j] = temp[i][j]

for i in range(0, n ):
    for j in range(0, n):
        print(temp2[i][j], end='')
    print('')