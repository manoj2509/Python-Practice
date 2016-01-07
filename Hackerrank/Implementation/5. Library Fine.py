text = list()
text = input().split(" ")
text2 = input().split(" ")
if text2[2] != text[2]:
    print(10000)
elif text2[1] != text[1]:
    print(500*(int(text[1]) - int(text2[1])))
elif text2[0] != text[0]:
    print(15*(int(text[0]) - int(text2[0])))
else:
    print(0)
