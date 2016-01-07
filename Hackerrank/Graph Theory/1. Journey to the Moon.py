__author__ = 'Mj'
l = []
N, I = list(map(int, input().strip().split()))
for i in range(I):
    p1, p2 = list(map(int, input().strip().split()))
    flag = 0
    for j in l:
        if p1 in j or p2 in j:
            j.append(p1)
            j.append(p2)
            flag = 1
    if flag == 0:
        l.append([p1, p2])
ml = []
for j in l:
    ml.append(list(set(j)))
for j in range(len(ml)):
    for i in range(j, len(ml)):
        if set(ml[j]) & set(ml[i]) is not None:
            


Total = (N*(N - 1)) / 2
for j in ml:
    tempset = set(j)
    print(tempset)
    temp = (len(tempset)*(len(tempset) - 1))/2
    print("Length is: ", len(tempset))
    Total -= temp
print(int(Total))