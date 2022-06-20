'''
Jakub Domogala
Algorytmy i Struktury danych

Na wejściu otrzymujemy listę jednokierunkową, w której wartość każdego elementu zawiera się w przedziale [0, 10) - rozkład równomierny
Funkcja def sort(L) sortuję listę i zwraca wskaźnik do jej pierwszego elementu(!).

Rozwiązanie:
Funkcja sortuję listę przy użyciu algorytmu bucketsort zaimplementowanego dla list jednokierunkowych.
Stabilny dla stabilnej funkcji sorted() sortującej pojedyńcze kontenery(buckety)
Złożoność obliczeniowa: O(n)
Złożoność pamięciowa: O(n)
n - długość listy wejściowej
'''
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

def show_list(first):
    if first == None:
        print("pusta")
    else:
        while first:
            print(first, end = ' -> ')
            first = first.next
        print('None')


def tab2list( A ):
  H = Node('!')
  C = H
  for i in range(len(A)):
    X = Node()
    X.value = A[i]
    C.next = X
    C = X
  return H

def sort(L):
    tmp = L
    n = 0
    while tmp.next:
        n += 1
        tmp = tmp.next
    norm = 10
    buckets = [[] for i in range(n)]
    tmp = L.next
    while tmp:
        norm_num = tmp.value / norm
        buck_ind = int(n * norm_num)
        buckets[buck_ind].append(tmp.value)
        tmp = tmp.next
    for i in range(n):
        buckets[i] = sorted(buckets[i])
    res = Node('!')
    tmp = res
    for i in range(n):
        for j in range(len(buckets[i])):
            tmp.next = Node(buckets[i][j])
            tmp = tmp.next
    return res



A = [3,4.1,2,1,5,7,6,8,9,0,4,2,1,0.1,0.2,3.1,5.1, 9.99]
B = [1,2,3,4]
L = tab2list(A)
show_list(L)
L = sort(L)
show_list(L)



