# Computing complexity  = O(n)
# Memory complexity     = O(n)
# n - number of elements
# Stable until sorted() method is stable

from random import randint
#-----------------------------------------------------------------------------------------------------------------------
def bucket_sort(A):
    n = len(A)
    norm = max(A)+1
    buckets = [[] for _ in range(n)]

    for num in A:
        norm_num = num / norm
        buck_ind = int(n * norm_num)
        buckets[buck_ind].append(num)
    for i in range(n):
        buckets[i] = sorted(buckets[i])
    out = []
    for i in range(n):
        for j in range(len(buckets[i])):
            out.append(buckets[i][j])
    return out
#-----------------------------------------------------------------------------------------------------------------------
A = []
for i in range(0,10):
    A = A + [randint(0,13)]

print("przed: \t",A)
A = bucket_sort(A)
print("po: \t",A)

