__author__ = 'Mj'
import sys
import os

def  closestNumbers( len,  s):
    text = s.split()
    text.sort()
    output = list()
    for i in range(0, len-1):
        min = i
        for j in range(i+1, len):
            if int(text[j]) < int(text[min]):
                min = j
        if min != i:
            temp = text[i]
            text[i] = text[min]
            text[min] = temp



    min = float("inf")

    for i in range(1, len):
        if  (int(text[i])-int(text[i-1])) <= min:
            output.append(int(text[i-1]))
            output.append(int(text[i]))
        if (int(text[i])-int(text[i-1])) < min:
            min = (int(text[i])-int(text[i-1]))
            del output[:]
            output.append(int(text[i-1]))
            output.append(int(text[i]))

    print (output)
    return output
f = open(os.environ['OUTPUT_PATH'], 'w')


_len = int(input());


_s = input()

res = closestNumbers(_len, _s);
f.write(res + "\n")

f.close()