'''
Jakub Domogala
Algorytmy i Struktury danych

Rozważmy słowa x[0]x[1] · · · x[n - 1] oraz y[0]y[1] · · · y[n - 1] składające się z małych liter alfabetu łacińskiego. Takie dwa słowa są t-anagramem (dla t ∈ {0, . . . , n - 1}), jeśli każdej literze
pierwszego słowa można przypisać taką samą literę drugiego, znajdującą się na pozycji różniącej
się o najwyżej t, tak że każda litera drugiego słowa jest przypisana dokładnie jednej literze słowa
pierwszego.
funkcja def tanagram(x, y, t) zwraca true jeśli podane słowa to tanagramy i false w przeciwnym razie

Złożoność obliczeniowa: O(n)
Złożoność pamięciowa: O(n)
n - długość listy wejściowej
c - stała
'''

#-----------------------------------------------------------------------------------------------------------------------
def t_anagram(string1, string2, distance):
    A = [[None] for _ in range(26)]
    B = [1] * 26
    for i, c in enumerate(string1):
        ind = ord(c) - 97
        A[ind].append(i)
    for i, c in enumerate(string2):
        ind = ord(c) - 97
        if abs(A[ind][B[ind]] - i) > distance:
            return False
        B[ord(string2[i]) - 97] += 1
    return True
#-----------------------------------------------------------------------------------------------------------------------


a = "kotomysz"
b = "tokmysoz"
# False for t = 2
# True for t = 3
t = 2
print(t_anagram(a, b, t))
