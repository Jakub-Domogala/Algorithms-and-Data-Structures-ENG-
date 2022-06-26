
# Computing complexity  = O(logn)
# Memory complexity     = O(c)
# n - number of elements
# c - constant
# Only for sorted arrays 
#-----------------------------------------------------------------------------------------------------------------------
def binary_search(A, x):
    r = len(A)-1
    l = 0
    while l <= r:
        m = (l + r)//2
        if A[m] == x:
            return m
        if x < A[m]:
            r = m - 1
        else:
            l = m + 1
    return False
#-----------------------------------------------------------------------------------------------------------------------

B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(binary_search(B, 4))