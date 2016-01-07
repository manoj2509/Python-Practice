__author__ = 'Mj'
find = int(input())
len = int(input())
text = list()
text = input().split(" ")
for i in range(len):
    if(find == int(text[i])):
        print(i)