'''
Jakub Domogala
Algorytmy i Struktury danych

Cyfra jednokrotna to taka, która występuje w danej liczbie dokładnie
jeden raz. Cyfra wielokrotna to taka, która w liczbie występuje więcej niż jeden raz. Mówimy,
że liczba naturalna A jest ładniejsza od liczby naturalnej B jeżeli w liczbie A występuje więcej
cyfr jednokrotnych niż w B, a jeżeli cyfr jednokrotnych jest tyle samo to ładniejsza jest ta
liczba, która posiada mniej cyfr wielokrotnych. Na przykład: liczba 123 jest ładniejsza od
455, liczba 1266 jest ładniejsza od 114577, a liczby 2344 i 67333 są jednakowo ładne.
Dana jest tablica T zawierająca liczby naturalne.

Funkcja def pretty_sort(T) sortuje elementy tablicy T od najładniejszych do najmniej ładnych.

Rozwiązanie:
Funkcja zlicza cyfry jednokrotne oraz wielokrotne, a następnie sortuje je za pomocą zmodyfikowanego algorytmu radix sort
Złożoność: O(n)
n - długość listy wejściowej
'''

def counting_sort(A,k):
    C = [0]*10
    B = [[0,0,0] for i in range(len(A))]
    for i in range(len(A)):
        C[A[i][k]] += 1
    for i in range(1, 10):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        C[A[i][k]] -= 1
        for j in range(3):
            B[C[A[i][k]]][j] = A[i][j]
    return B


def radix_sort(A):
    A = counting_sort(A,1)
    A = counting_sort(A,0)
    return A


def count_single_multi(num):
    N = [0] * 10
    while num > 0:
        N[num%10] += 1
        num //= 10
    single = 0
    multi = 0
    for i in range(10):
        if N[i] == 1: single += 1
        if N[i] > 1: multi += 1
    return single, multi


def pretty_sort(T):
    n = len(T)
    X = [[None, None, None] for _ in range(n)]
    for i in range(n):
        s, m = count_single_multi(T[i])
        X[i][0] = -s
        X[i][1] = m
        X[i][2] = T[i]
    X = radix_sort(X)
    for i in range(n):
        T[i] = X[i][2]
    return T


A = [123, 455, 1266, 114577, 2344, 67333]
print(pretty_sort(A))
