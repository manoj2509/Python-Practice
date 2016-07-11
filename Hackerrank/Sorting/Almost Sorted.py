__author__ = 'Mj'
import copy
import sys

N = int(input().strip())
num = list(map(int, input().strip().split()))
snum = copy.deepcopy(num)
snum.sort()
for i in range(N):
    print(snum[i], end=" ")
print()
if num == snum:
    print("yes")
else:
    for i in range(1, N):
        if num[i-1] > num[i]:
            temp = num[i-1]
            num[i-1] = num[i]
            num[i] = temp
            if num == snum:
                print("yes")
                print("swap", i, i+1)
                sys.exit()
            else:
                temp = num[i-1]
                num[i-1] = num[i]
                num[i] = temp
                temp = i - 1
                lval = temp
                while num[i-1] > num[i]:
                    i += 1
                temp2 = i - 1
                rval = temp2
                while(temp < temp2):
                    temp3 = num[temp]
                    num[temp] = num[temp2]
                    num[temp2] = temp3
                    temp += 1
                    temp2 -= 1
                if num == snum:
                    print("yes")
                    print("reverse", lval + 1, rval + 1)
                    sys.exit()
                else:
                    print("no")
                    sys.exit()