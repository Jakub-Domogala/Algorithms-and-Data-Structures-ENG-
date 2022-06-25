# Computing complexity  = O(n + k)
# Memory complexity     = O(n + k)
# n - number of elements
# k - span of elements
# k is usually so small that we can call computing complexity linear - O(n)
# Unstable 

from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def counting_sort(A,k):
    C = [0]*(k + 1)
    B = [0]*len(A)
    for i in range(len(A)):
        C[A[i]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[A[i]] -= 1
        B[C[A[i]]] = A[i]
    return B
#-----------------------------------------------------------------------------------------------------------------------
A = []
k = 10
for i in range(0,10):
    A = A + [randint(0,k)]

print("przed: \t",A)
A = counting_sort(A, k)
print("po: \t",A)
