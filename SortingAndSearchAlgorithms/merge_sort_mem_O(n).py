# Computing complexity  = O(nlogn)
# Memory complexity     = O(n)
# n - number of elements
# Stable

from random import randint


#-----------------------------------------------------------------------------------------------------------------------
def mergesort(A, left, right, tmp):
    if abs(left - right) < 2:
        return left, right

    mid = (left + right) // 2

    left_1, left_2 = mergesort(A, left, mid, tmp)
    right_1, right_2 = mergesort(A, mid, right, tmp)

    i, j, k = left_1, right_1, left_1
    while i < left_2 and j < right_2:
        if A[i][0] <= A[j][0]:
            tmp[k] = A[i]
            i += 1
        else:
            tmp[k] = A[j]
            j += 1
        k += 1

    while i < left_2:
        tmp[k] = A[i]
        k += 1
        i += 1

    while j < right_2:
        tmp[k] = A[j]
        k += 1
        j += 1

    for i in range(left_1, right_2):
        A[i] = tmp[i]

    return left_1, right_2
#-----------------------------------------------------------------------------------------------------------------------

def msort(A): # Method just to visualize indexes and call mergesort
    n = len(A)
    tmp = [None] * n
    A = [(A[i], i) for i in range(n)]
    print("Before: \t",A)
    mergesort(A, 0, n, tmp)
    print("After: \t",A)
    return A


A = []
for i in range(0,10):
    A = A + [randint(0,13)]

print("\nAt first list of numbers is changed to list of tuples where list[i][0] is number and list[i][1] is index, \nso that we can see stability of algorithm\n")
msort(A)
