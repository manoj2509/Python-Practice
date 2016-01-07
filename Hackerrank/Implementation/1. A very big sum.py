num = list()
text = input()
n = int(text)
sum = 0
text = input().split(' ')
for i in range(0, n):
    num.append(int(text[i]))
    sum += num[i]
print(sum)