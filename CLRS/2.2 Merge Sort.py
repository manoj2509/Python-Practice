__author__ = 'Mj'
def merge(A, p, q, r):
    L = R = [[]for i in range(r-p)]
    n1 = q - p + 1
    n2 = r - q
    for i in range(n1):
        L[i] = A[p + i]
    for i in range(n2):
        R[i] = A[q + i]
    i = j = k = 0
    while(i <= q and j <= r):
        if(L[i] <= R[i]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    if(i == q):
        for m in range(j, r + 1):
            A[k] = R[m]
            k += 1
    else:
        for m in range(j, r + 1):
            A[k] = L[m]
            k += 1
    for i in range(p, r):
        print(A[i], end=' ')
    print()

def mergesort(A, p, r):
    if(p < r):
        q = (p + r)/2
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)

text = input().strip().split(' ')
leng = len(text)
mergesort(text, 0, leng)