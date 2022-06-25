'''
Jakub Domogala
Algorytmy i Struktury danych

Dana jest tablica A zawierająca n = len(A) liczb naturalnych. Dodatkowo wiadomo, że A w sumie
zawiera k różnych liczb (należy założyć, że k jest dużo mniejsze niż n). Proszę zaimplementować
funkcję longest incomplete(A, k), która zwraca długość najdłuższego spójnego ciągu elementów
z tablicy A, w którym nie występuje wszystkie k liczb. (Można założyć, że podana wartość k jest
zawsze prawidłowa.)

Rozwiązanie:
Tworzę drzewo, w którym zliczam ilość wystąpień poszczególnych wartości(w zadaniu zakazane było używanie struktur typu słownik).
Idąc przez listę dodaje kolejne elementy, a gdy ilość różnyh wartości wyniesie 'k' usuwam elementy dodane najdawniej 
tak długo aż liczba różnych wartości wyniesie 'k-1'.
Cały czas zliczam najdłuższy poprawny uzyskany podciąg

Złożoność obliczeniowa: O(nlogk)
Złożoność pamięciowa: O(n)
'''
class BSTNode:
    def __init__(self, value, count = 1):
        self.value = value
        self.left = None
        self.right = None
        self.count = count


# Funkcja dla decide = 1 dodaje element, a dla decide = -1 usuwa, 
# wartość zwracana przez funkcje to liczba elementów danej wartości
def insert_or_delete_bst_element(root, val, decide):
    p = root
    while root:
        p = root
        if root.value > val:
            root = root.left
        elif root.value < val:
            root = root.right
        else:
            root.count += decide
            if root.count - decide == 0:
                return 1
            elif root.count == 0:
                return -1
            else:
                return 0
    if p.value > val:
        p.left = BSTNode(val)
        return 1
    elif p.value < val:
        p.right = BSTNode(val)
        return 1


def longest_incomplete(A, k):
    n = len(A)
    root = BSTNode(A[0])
    tk = 1
    l = 1
    j = 0
    ma = 0
    for i in range(1, n):
        tk += insert_or_delete_bst_element(root, A[i], 1)
        l += 1
        if ma < l and tk < k: 
            ma = l
        for a in range(j, i+1): 
            print(A[a], end= ' ')
        print('+++++')
        i -= 1
        while tk >= k:
            tk += insert_or_delete_bst_element(root, A[j], -1)
            l -= 1
            j += 1
        for a in range(j, i + 1): print(A[a], end=' ')
        print('--')
    return ma


A = [1,100, 5, 100, 1, 5, 1, 5] #1,5,1,5

print(longest_incomplete(A, 3))



