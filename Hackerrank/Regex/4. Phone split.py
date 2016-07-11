import re
n = int(input())
for i in range(n):
    case = input().strip()
    ans = re.split('-| ', case)
    print(ans)
    print('CountryCode=',end='')
    print(case[0],end='')
    print(',LocalAreaCode=', end='')
    print(case[1], end='')
    print(',Number=', end='')
    print(case[2])