def  cavityMap(arr):
    n = len(arr)
    for i in range(n):
        temp = ""
        for j in range(n):
            if (i in range(1, n-1) and j in range(1, n-1)):
                if (arr[i][j] > arr[i][j-1] and arr[i][j] > arr[i-1][j] and arr[i][j] > arr[i+1][j] and arr[i][j] > arr[i][j+1]):
                    temp += 'X'
                else:
                    temp += arr[i][j]
            else:
                temp+= arr[i][j]
        arr[i] = temp
    return arr


arr = ['1112', '1912', '1892', '1234']
ans = cavityMap(arr)
for i in range(len(arr)):
    print(ans[i])