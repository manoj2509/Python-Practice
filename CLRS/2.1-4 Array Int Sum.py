__author__ = 'Mj'
#Sum of 2 n-digit numbers. Numbers are stored in list
a = input().strip()
b = input().strip()
c = list()
n = len(a)
carry = 0
for i in range(n-1, -1, -1):
    temp = int(a[i]) + int(b[i]) + carry
    if(temp > 10 ):
        carry = 1
        c.insert(0, temp - 10)
    else:
        carry = 0
        c.insert(0, temp)
if(carry == 1):
    c.insert(0, carry)
print(c)