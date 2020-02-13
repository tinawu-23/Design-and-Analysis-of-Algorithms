## Bubble Sort ##

# Time: O(n^2)
# Space: O(1)
# Max num of swaps: n^2

def bubblesort_toback(A):
    n = len(A)
    for i in range(0,n-1): # 0 to n-2 inclusive
        for j in range(0,n-i-1): # 0 to n-i-2 inclusive
            if A[j] > A[j+1]:
                A[j+1], A[j] = A[j], A[j+1]
    return A


def bubblesort_tofront(A):
    n = len(A) # 1,2,3,...,n-1
    for i in range(0, n-1):  # 0 to n-2 inclusive
        for j in range(n-1, i, -1):  # n-1 to i+1, backwards inclusive
            if A[j-1] > A[j]:
                A[j-1], A[j] = A[j], A[j-1]
    return A


print(bubblesort_toback([4, 3, 2, 1, 5, 6, 2, 3, 4, 1]))
print(bubblesort_tofront([4, 3, 2, 1, 5, 6, 2, 3, 4, 1]))
