# Computing complexity  = O(n^2)
# Memory complexity     = O(c)
# n - number of elements
# c - constant 
# Stable

from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
#-----------------------------------------------------------------------------------------------------------------------
A = []
for i in range(0,9):
    A = A + [randint(0,9)]

print("przed: \t",A)
insertion_sort(A)
print("po: \t",A)

