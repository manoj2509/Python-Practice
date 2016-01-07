__author__ = 'Mj'
book = open('output.txt', 'w')
for i in range(0, 11):
    book.write(str(i))
    book.write('\n')
book.close()