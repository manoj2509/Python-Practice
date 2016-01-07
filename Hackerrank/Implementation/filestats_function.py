__author__ = 'Mj'
def file_stats(filename):
    book = open(filename, 'r')
    n_char = n_line = n_word = 0
    for line in book:
        n_line += 1
        n_char += len(line)
        for word in line:
            if word == ' ':
                n_word +=  1
    book.close()
    return n_line, n_word, n_char

file_name = input('Enter a filename: ')
print(file_name, file_stats(file_name))