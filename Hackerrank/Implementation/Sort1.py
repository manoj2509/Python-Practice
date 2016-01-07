__author__ = 'Mj'


leng = int(input())
text = list()
text = input().split(" ")
count = 0
for i in range(1, leng):
    val = int(text[i])
    hole = i
    while(hole > 0 and int(text[hole - 1]) > int(val)):
        text[hole] = int(text[hole - 1])
        hole = hole - 1
        count = count + 1
    text[hole] = val
    print(count)