t = int(input())
n = []
count = []
initial = []
for i in range(t):
    n.append(int(input()))
    temp = list(map(int,input().strip().split(' ')))
    initial.append(temp)
for i in range(t):
    temp1 = max(initial[i])
    temp2 = min(initial[i])
    count.append(0)
    while temp1 != temp2:
        pos = initial[i].index(max(initial[i]))
        if temp1 - temp2 >= 5:
            count[i] += 1
            initial[i][pos] = temp1 - 5
        elif temp1 - temp2 >= 2:
            count[i] += 1
            initial[i][pos] = temp1 - 2
        else:
            count[i] += 1
            initial[i][pos] = temp - 1
        temp1 = max(initial[i])
        temp2 = min(initial[i])
for i in range(t):
    print(count[i])