__author__ = 'Mj'

import sys
dict = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'quarter', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 21:'twenty one', 22:'twenty two', 23:'twenty three', 24:'twenty four', 25:'twenty five', 26:'twenty six', 27:'twenty seven', 28:'twenty eight', 29:'twenty nine', 30:'half'}

h = int(input().strip())
m = int(input().strip())
if(m == 30 or m == 15):
    print(dict[m], "past", dict[h])
elif(m > 30 and m <59 and m!=45):
    if(h == 12):
        print(dict[60-m], "minutes to", dict[1])
    else:
        print(dict[60-m], "minutes to", dict[h+1])
elif(m == 59):
    if(h == 12):
        print(dict[60-m], "minute to", dict[1])
    else:
        print(dict[60-m], "minute to", dict[h+1])
elif(m == 45):
    if(h == 12):
        print(dict[60-m], "to", dict[1])
    else:
        print(dict[60-m], "to", dict[h+1])
else:
    if(m == 0):
        print(dict[h], "o' clock")
    elif(m == 1):
        print(dict[m], "minute past", dict[h])
    else:
        print(dict[m], "minutes past", dict[h])
