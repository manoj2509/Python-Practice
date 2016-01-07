__author__ = 'Mj'
n = int(input())
input_case = [[0 for j in range(0,3)] for i in range(0, n)]
for i in range(0,n):
    input_case[i] = input().split(" ")
ans = [[]for i in range(0, n)]
wrap = [[]for i in range(0, n)]
for i in range(0, n):
    ans[i] = wrap[i] = int(int(input_case[i][0])/int(input_case[i][1]))
    while(wrap[i] >= int(input_case[i][2])):
        ans[i] += int(wrap[i]/int(input_case[i][2]))
        wrap[i] = int(wrap[i]%int(input_case[i][2])) + int(wrap[i]/int(input_case[i][2]))
        print("%d, %d", ans[i], wrap[i])
    print(int(ans[i]))