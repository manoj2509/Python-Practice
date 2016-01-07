__author__ = 'Mj'
t = int(input())
text = list()
text2 = list()
for i in range(t):
    temp = input().split(' ')
    text.append(temp)
    temp2 = input().split(' ')
    text2.append(temp2)
for i in range(t):
    if ((int(text2[i][0])+int(text2[i][2])) < int(text2[i][1])):
        cost = int(text[i][0])*int(text2[i][0]) + int(text[i][1])*(int(text2[i][0]) + int(text2[i][2]))
    elif ((int(text2[i][1])+int(text2[i][2])) < int(text2[i][0])):
        cost = int(text[i][1])*int(text2[i][1]) + int(text[i][0])*(int(text2[i][1]) + int(text2[i][2]))
    else:
        cost = int(text[i][1])*int(text2[i][1]) + int(text[i][0])*int(text2[i][0])
    print(cost)