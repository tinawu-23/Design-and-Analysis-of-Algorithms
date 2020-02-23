def insertionsort(A):
    n = len(A)
    for i in range(1,n):
        v = A[i]
        j = i - 1
        while j >= 0 and A[j] > v:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = v
    return A

print(insertionsort([9,8,7,5,3,2,6,4,1]))