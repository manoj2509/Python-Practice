__author__ = 'Mj'
import timeit
def Brute(A, low, high):
    result = [0, 0, float('-inf')]
    for i in range(low, high):
        curr_sum = 0
        for j in range(i, high):
            curr_sum += A[j]
            if result[2] < curr_sum:
                result[0] = i
                result[1] = j + 1
                result[2] = curr_sum
    return result


def Mid(A, low, mid, high):
    result = [0, 0, float('-inf')]
    sum = 0
    Lsum = float('-inf')
    Rsum = float('-inf')
    for i in range(mid-1, int(low), -1):
        sum += A[i]
        if sum > Lsum:
            Lsum = sum
            result[0] = i
    sum = 0
    for j in range(mid, high):
        sum += A[j]
        if sum > Rsum:
            Rsum = sum
            result[1] = j + 1
    result[2] = Lsum + Rsum
    return result

def Rec(A, low, high):
    if high == low + 1:
        result = [low, high, A[low]]
        return result
    else:
        mid = int((low + high)/2)
        Left = Rec(A, low, mid)
        Right = Rec(A, mid + 1, high)
        Cross = Rec(A, low, mid, high)

        result = max(Left, Right, Cross)
        return result

# def Mixed(A, low, high):
#     if high - low <

i = 5
flag = 0
Arr = [20, -21, 43, -23, -92, 45, -56, -5, 34, -17,
                    34, 65, 89, -109, 125, 2, -10, 89, 46, 65, -49,
                    3, -45, 34, 76, 32, -76, -2, 3, -45, 44, 34, 67,
                    -67, 99, -104, 11, -37, 44, 76, -90, 89, -32, 34,
                    88, 56, -6, -89, -90, -34, -56, 23, 29, 2, 6, 9,
                    2, -34, -45, 34, 22, -177, 44, 90, -45, -36, 55,
                    23, 56, -56, -167, -54, 23, 45, 14, 62, -46, -56,
                    -34, 45, 32, 20, -87, 39, 82, 95, -67, -45, 88,
                    -36, 21, 18, 16, 81, -102, 99, -45, -67, -45, -76]

while flag == 0:
    start_time = timeit.default_timer()
    R1 = Brute(Arr, 0, i)
    B_elapsed = timeit.default_timer() - start_time
    print(i, B_elapsed)

    start_time = timeit.default_timer()
    R2 = Rec(Arr, 0, i)
    R_elapsed = timeit.default_timer() - start_time
    print(i, R_elapsed)

    i += 1
    if B_elapsed > R_elapsed:
        flag = 1