__author__ = 'Mj'
N, K = list(map(int, input().strip().split()))
count = [None] * K
price = list(map(int, input().strip().split()))
price.sort(reverse = True)
for i in range(N):
    count[i%K] += price[i] * (int((i/K)) + 1)
ans = 0
for each in count:
    ans += each
print(ans)