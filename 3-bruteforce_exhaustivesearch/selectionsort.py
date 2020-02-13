## Selection Sort ##

# Time: O(n^2)
# Space: O(1) 
# Max num of swaps: n


def selectionsort_tofront(A):
    n = len(A)
    for i in range(0,n-1):
        minInd = i
        for j in range(i+1,n):
            if A[j] < A[minInd]: 
                minInd = j
        A[i], A[minInd] = A[minInd], A[i]
    return A


def selectionsort_toback(A):
    n = len(A)
    for i in range(n-1,0,-1):
        maxInd = i
        for j in range(i-1,-1,-1):
            if A[j] > A[maxInd]:
                maxInd = j
        A[i], A[maxInd] = A[maxInd], A[i]
    return A


print(selectionsort_tofront([4, 3, 2, 1, 5, 6, 2, 3, 4, 1]))
print(selectionsort_toback([4, 3, 2, 1, 5, 6, 2, 3, 4, 1]))