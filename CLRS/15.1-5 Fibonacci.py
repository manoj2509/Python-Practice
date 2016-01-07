__author__ = 'Mj'


def fib(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(int(f[i - 1] + f[i - 2]))
    return f

num = int(input())
fi = fib(num)
print(fi)