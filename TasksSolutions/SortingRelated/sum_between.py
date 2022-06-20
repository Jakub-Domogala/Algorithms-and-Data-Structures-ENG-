'''
Jakub Domogala
Algorytmy i Struktury danych

Na wejściu otrzymujemy listę tablicę losowych unikalnych wartości oraz indeksy 'f' 't', naszym zadaniem jest podać sumę elementów które 
znajdowałyby się pomiędzy indexami(włącznie) 'f', a 't' gdyby lista była posortowana.

Rozwiązanie:
Funkcja sum_between(A, f, t) używa algorytmu magicznych piątek(linear_select) by znaleźć 
elementy na indeksach 'f' i 't' posortowanej 'A', a następnie sumuje 
elementy o wartościach z przedziału znalezionych elementów.
Złożoność obliczeniowa: O(n)
Złożoność pamięciowa: O(c)
n - długość listy wejściowej
c - stała

Note:
W przypadku tablicy z powtórzeniami algorytm może z dużym prawdopodobieństwem
podać niepoprawną odpowiedź
'''



from math import ceil

def partition(A, x, l, r):
    i = l
    while i <= r:
        if A[i] == x:
            i += 1

        elif A[i] < x:
            A[l], A[i] = A[i], A[l]
            l += 1
            i += 1
        else:
            A[r], A[i] = A[i], A[r]
            r -= 1
    return l


def insert_sort(A, l, r):
    for i in range(l + 1, r + 1):
        key = A[i]
        j = i - 1
        while j >= l and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key


def find_median(A, l, r):
    if r - l <= 5:
        insert_sort(A, l, r)
        index = l + ((r - l) // 2)
        return A[index]

    n = r - l + 1
    i = 0
    j = 0
    while i + 4 <= n:
        insert_sort(A, i, i + 4)
        A[j], A[i + 2] = A[i + 2], A[j]
        i += 5
        j += 1

    if i < n:
        insert_sort(A, i, n - 1)
        A[j], A[i + ((n - 1 - i) // 2)] = A[i + ((n - 1 - i) // 2)], A[j]

    return find_median(A, 0, ceil(n / 5))


def linear_select(A, k, l=0, r=None):
    if r == None:
        r = len(A) - 1
    if k == 0:
        mini = A[0]
        for i in range(len(A)): mini = min(mini, A[i])
        return mini
    median = find_median(A, l, r - 1)
    pivot = partition(A, median, l, r)
    if pivot == k:
        return A[pivot]
    elif pivot > k:
        return linear_select(A, k, 0, pivot - 1)
    else:
        return linear_select(A, k, pivot + 1, r)


def sum_between(A, f, t):
    n = len(A)
    if f == t:
        return linear_select(A, f)
    if f > t or f < 0 or t > n: return False
    f = linear_select(A, f)
    t = linear_select(A, t)
    sum = 0
    for i in range(n):
        if A[i] >= f and A[i] <= t:
            sum += A[i]
    return sum




A = [3,2,1,4,6,5,7,9,8,0]
f = 0
t = 5
x = sum_between(A, f, t)
print(x, "to suma elementów:", sorted(A)[f:t+1])