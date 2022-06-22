'''
Jakub Domogala
Algorytmy i Struktury danych

Proszę zaimplementować funkcję heavy path(T), która na wejściu otrzymuje drzewo T z ważonymi krawędziami (wagi to liczby całkowite—mogą być zarówno dodatnie, ujemne, jak i o wartości zero) i zwraca długość (wagę) najdłuższej ścieżki prostej w
tym drzewie.

Rozwiązanie:
Dla każdego pola definiujemy zmienne f i g, w których zapisujemy kolejno:
f - największa waga schodzącej gałęzi od liścia aż do tego punktu
g - największa waga ścieżki, która w całości zawiera się poniżej lub do danego punktu
Rekurencyjnie wspinamy się od dołu aż do głównego korzenia przepisując w górę najlepsze(największe) rowziązania
Złożoność: O(n)
n - ilość elementów w drzewie
'''
class Node:
    def __init__(self, children = 0, value = None, child = [], parent = None, f = None, g = None):
        self.children = children    # number of children
        self.child = child          # list for children
        self.parent = parent        # parent node
        self.value = value          # weight of edge above this node
        self.f = f                  # heaviest branch from this node
        self.g = g                  # heaviest branch through or below this node


def heavy_path(T):
    if T.children == 0:
        return 0, 0
    f = 0
    g = 0
    tmax = 0
    pmax = 0
    for i in range(T.children):
        tmpf, tmpg = heavy_path(T.child[i])
        f = max(f, tmpf + T.child[i].value)
        if tmpf + T.child[i].value > tmax:
            tmax = tmpf + T.child[i].value
        elif tmpf + T.child[i].value > pmax:
            pmax = tmpf + T.child[i].value
        g = max(g, tmpg, tmax + pmax)
    if T.value == None:
        return (f, g)
    return f, g





#Node(children, value, [         ])
#[(5, 2), (3, 0), (-1, 1), (2, 0), (7, 0), (-2, 2), (20, 0), (17, 0)]
T = Node(3, None, [Node(2, 5, [Node(0, 2), Node(0, 17)]), Node(0, 3), Node(1, -1, [Node(2, -2, [Node(0, 20), Node(1, 17,[Node(0,1)])])])])
print(max(heavy_path(T)))
