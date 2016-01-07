__author__ = 'Mj'

def CUT_ROD(price, maxi, n):
    s = []
    if(n == 0):
        return 0
    q = -1

    for i in range(0, n):
        s.append(0)
        for j in range(i + 1):
            if q < int(price[i - j]) + int(maxi[j]):
                q = int(price[i - j]) + int(maxi[j])
                s[i] = i - j
        maxi.append(q)
    print(s)
    return q

price = input().strip().split(' ')
n = int(input())
maxi = [0]
s = []
maxim = CUT_ROD(price, maxi, n)
print('Max = ', maxim)
#while n > 0:
 #   print(s[n], end=' ')
  #  n = n - s[n]