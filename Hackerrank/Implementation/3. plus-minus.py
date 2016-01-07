n = int(input())                # input size
pos = neg = zer = 0
text = input().split(' ')       # input data as a complete list
for i in range(0,n):
    if int(text[i]) == 0:
        zer += 1
    elif int(text[i]) < 0:
        neg += 1
    else:
        pos += 1
#pos = float("0:.3f".format(pos))
#neg = float("0:.3f".format(neg))
#zer = float("0:.3f".format(zer))
print("%0.6f" %(pos/n))
print("%0.6f" %(neg/n))
print("%0.6f" %(zer/n))     #setting up the decimal precision