"""
Zadanie 1. Problem stacji benzynowej
L-litrów
[]
|------------------->
1   2    3   4   5   n-1

1) jak najmniej razy - jedziemy dopoki paliwo sie nie skonczy, koszt == 0


2) kazda stacja ma przypisany koszt paliwa C[i], chcemy wydac jak najmniej
L = 3
|-------------------------------->
 0   1  2   3   4   5   6   7   8
==================================
 1  2   1   3   2   4   1   2

3) jesli tankujemy to musimy do pełna - dynamicznie
           { min {f(C,i+1,l-1,L), f(C,i+2,l-2),......... f(C,i+1,L-1,L)+C[i]*(L-i)}
f(C,i,l) = {
           {
________________________________________________________________________________________________________________________
Zadanie 2. Pokrycie zbioru liczb przedziałami jednostkowymi
{1,2.3,3.2,8}
   0.5   1.5
    ______
---|--1--|-2.3--------3.2-------------8-->
"""


# Implementacja

def przedzialy(T):
    if len(T) == 0:
        return 0
    licznik = 0
    sorted(T)
    curr = T[0]
    for elem in T[1:]:
        if elem > curr + 1:
            licznik += 1
            curr = elem
    return licznik


"""
Wykonaj zadania z listy tak aby miec maksymalne zyski
Z = [z1,z2,z3........zn] - zadania
D = [d1,d2,d3,.......dn] - deadline
P = [p1,.............pn] - zysk
"""


# Implementacja
class Z:
    def __init__(self):
        Z.d = None
        Z.p = None


def choose(Z):
    Z.sort(key=lambda x: x.p)
    Z.sort(key=lambda x: x.d, reverse=True)
    ret = []
    while Z:
        f = Z[0]
        ret.append(f)
        Z.pop(0)
        for e in Z:
            if e.d != f.d:
                break
            e.d -= 1
        Z.sort(key=lambda x: x.p)
        Z.sort(key=lambda x: x.d, reverse=True)
    return ret


"""
Zadanie 4. Ladunki, chcemy załadować jak najwiecej kg, jesli ładują tyle samo to to z najmniejsza liczą ładunków
K = [2,4,2,32,8,16,2,2,4]
(27) - potęgi dwójki
"""


# Implementacja:

def ladunek(P, K):
    K.sort(reverse=True)  # złożoność: nlogn
    tab = []
    for i in K:
        if (P >= i):
            tab.append(i)
            P -= i
    return tab

"""
Zadanie 5. Klocki
Zadanie 6. Najmniejsze k
A = [x1,.....xn] posortowana
k należy do R
suma od 0 do n-1:  |xi-k| ---> min

1) binary search
2) mediana
"""
