__author__ = 'Mj'
dict = {}
def fib(n):
    if n in dict:
        return dict[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    dict[n] = f
    return f
n = int(input())
ans = fib(n)
print(ans)
print(dict.items())
