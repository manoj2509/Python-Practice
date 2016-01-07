__author__ = 'Mj'
text = list()
def partition(text, start, end):
    pivot = start
    i = j = start + 1
    while(j < end):
        if int(text[pivot]) > int(text[j]):
                #swap(text[i], text[j])
            temp = text[i]
            text[i] = text[j]
            text[j] = temp
            i += 1
        j += 1
    temp = text[pivot]
    text[pivot] = text[i - 1]
    text[i - 1] = temp

    return i - 1

def QuickSort(text, p, r):
    if p < r:
        split = partition(text, p, r)
        QuickSort(text, p, split - 1)
        QuickSort(text, split + 1, len(text))

    else:
        return 0

n = int(input().strip())
text = input().strip().split(' ')
QuickSort(text, 0, n)