__author__ = 'Mj'
book = open("1. A very big sum.py", 'r')
n_char = 0
n_line = 0
n_word = 0
for line in book:
    n_char += len(line)
    n_line += 1
    for word in line:
        if word == ' ':
            n_word += 1
#    n_word += len(word)
print(n_char)
print(n_word)
print(n_line)
book.close()