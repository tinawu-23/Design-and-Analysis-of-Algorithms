def findmissing(A):
    l, r = 0, len(A)-1
    while l <= r:
        mid = (l+r)//2
        if A[mid]-mid == 1:
            l = mid + 1
        elif A[mid]-mid == 2:
            r = mid - 1

    return A[r]+1

print(findmissing([1,2,3,4,5,7]))