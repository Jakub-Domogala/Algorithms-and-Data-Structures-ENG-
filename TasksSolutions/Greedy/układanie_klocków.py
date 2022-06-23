'''
Jakub Domogala
Algorytmy i Struktury danych

Dany jest zbiór klocków K = {K1, . . . , Kn}. Każdy klocek Ki opisany
jest jako jednostronnie domknięty przedział (ai, bi], gdzie ai, bi ∈ N, i ma wysokość 1 (należy
założyć, że żadne dwa klocki nie zaczynają się w tym samym punkcie, czyli wartości ai są
parami różne). Klocki są zrzucane na oś liczbową w pewnej kolejności. Gdy tylko spadający
klocek dotyka innego klocka (powierzchnią poziomą), to jest do niego trwale doczepiany i
przestaje spadać. Kolejność spadania klocków jest poprawna jeśli każdy klocek albo w całości
ląduje na osi liczbowej, albo w całości ląduje na innych klockach.

Funkcja def perfect_tower(K) zwraca kolejność poprawnego zrzucania klocków przy odgórnym założeniu, że taka kolejność istnieje

Rozwiązanie:
Tworzymy tablicę 'T' posortowaną rosnąco po początkach, malejąco po końcach, 
następnie kładziemy klocki poziomami kolejno od lewej do prawej(od 0 w górę)
Złożoność: O(n^2)
n - liczba klocków
'''

#-----------------------------------------------------------------------------------------------------------------------
def divide(T, b, e, o):
  if b < e:
    mid = (b + e) // 2
    divide(T, b, mid, o)
    divide(T, mid+1, e, o)
    return merge(T, b, mid, mid+1, e, o)


def merge(T, bl, el, br, er, o):
  temp = []
  pom_start_index = bl
  for i in range (er - bl + 1):
    if bl > el:
      while br <= er:
        temp.append(T[br])
        br += 1
      break
    if br > er:
      while bl <= el:
        temp.append(T[bl])
        bl += 1
      break

    if T[bl][o] > T[br][o]:
      temp.append(T[br])
      br += 1
    else:
      temp.append(T[bl])
      bl += 1
  j = 0
  for i in range(pom_start_index, er + 1):
    T[i] = temp[j]
    j += 1
  return T


def mergesort(T, o): return divide(T, 0, len(T)-1, o)


def perfect_tower(K):
    n = len(K)
    T = [None] * n
    for i in range(n):
        T[i] = (K[i][0], K[i][1], i+1)
    T = mergesort(T, 1)
    T.reverse()
    T = mergesort(T, 0)
    print(T)
    A = []
    k = n
    while k > 0:  # loop with each another cycle meaning next level of blocks layed
        end = 0
        for i in range(n):  # loop for placing individual blocks 
            if T[i] and T[i][0] >= end:
                A.append(T[i][2])
                k -= 1
                end = T[i][1]
                T[i] = None
    return A
#-----------------------------------------------------------------------------------------------------------------------

K = [(2, 4), (5, 7), (3, 6), (4, 5)]
result = perfect_tower(K)
print(result)