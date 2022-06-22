'''
Jakub Domogala
Algorytmy i Struktury danych

Mamy n żołnierzy różnego wzrostu i nieuporządkowaną tablicę, w której
podano wzrosty żołnierzy. Żołnierze zostaną ustawieni na placu w szeregu malejąco względem
wzrostu.

Funkcja def section(T,p,q) zwróci tablicę ze wzrostami żołnierzy na pozycjach od p do q włącznie.

Rozwiązanie:
Używając algorytmu mediany-median znajdujemy w czasie miejsce dla pojedyńczego żołnierza w czasie logn.
Wykonujemy q-p takich operacji dla każdego miejsca z przedziału

Złożoność: O((q-p)logn)
n - długość listy wejściowej
(q-p) - wielkość przedziału do posortowania
'''


from random import randint
def partition(A,left,right):
    i = left - 1
    pom = randint(left,right-1)
    A[right], A[pom] = A[pom], A[right]
    x = A[right]
    for j in range(left,right):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[right] = A[right], A[i+1]
    return i + 1

def select(A, p, r, k):
    if p == r:
        return A[p]
    q = partition(A, p, r)
    if q == k:
        return A[q]
    elif k < q:
        return select(A, p, q - 1, k)
    else:
        return select(A, q + 1, r, k)

def qselect(A, ind):
    return select(A, 0, len(A)-1, ind)

def section(T, p, q):
    n = q - p + 1
    R = [0] * n
    p = qselect(T, p)
    q = qselect(T, q)
    j = 0
    for i in range(len(T)):
        if T[i] >= p and T[i] <= q:
            R[j] = T[i]
            j += 1
    return R


A = [195, 185, 173, 188, 199, 200, 210, 201, 154, 163]
# A = [154, 163, 173, 185, 188, 195, 199, 200, 201, 210]

print(section(A, 3, 7))