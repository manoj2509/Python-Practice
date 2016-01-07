__author__ = 'Mj'

def factl(a):
    if a == 1:
        return 1
    else:
        return factl(a-1) *a

num = int(input())
ans = factl(num)
print(ans)