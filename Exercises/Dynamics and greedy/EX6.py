# Programowanie dynamiczne

"""
Problem plecakowy w czasie wielomianowym względem liczby przedmiotów i profitów

F(T,n,w) = {max(T[n].val + f(T,n-1,w-T[n]}.w), f(T,n-1,w)}
           warunki konca: 0,n<0,w<=0

            { v:  1000   500     800     800   100
            { w: 15     5       3       14     20

"""


class Item:
    def __init__(self, id, value, weight):
        self.weight = weight
        self.id = id
        self.val = value


def f(T, n, w, results):
    if n < 0 or w <= 0:
        return 0
    if results[n][w] == 0:
        results[n][w] = max(T[n].val + f(T, n - 1, w - T[n].weight, results), f(T, n - 1, w, results))
    return [n][w]


def f2(T, n, w):
    result = [[0 for i in range(w)] for j in range(n)]
    return f(T, n, w, result)


# return max((T[n].val + knapsack_wielomianowo(T, n - 1, w - T[n].w), knapsack_wielomianowo(T, n - 1, w)))

"""
________________________________________________________________________________________________________________________
Problem sumy podzbiory
Dana jest tablica liczb, znajdz ciąg sumujący się do zadanej sumy
A - tablica liczb naturalnych
Wersja rekurencyjna, badamy czy bierzemy czy nie, a nastpenie badamy czy dodanie da nam sumę
Czy isntnieje podciag o sumie ==x

Analogia do popzredniego zadania

def szukanie(A, i, S)
Przypadki:
1. f(A,i-1,S)  or
2. f(A,i-1,S - A[i])

Przypadki brzegowe: 1 -> if s == 0
                    0 -> if s!=0 and i <0
________________________________________________________________________________________________________________________
Najdłuższy wspolny podciag miedzy dwoma tablicami
________________________________________________________________________________________________________________________
Ciąg macierzy A[] , B[], C[], D[], E[] - wstawienie nawiasów żeby było jak najszybciej
Zadanie: znajdz koszt mnożenia macierzy np. A(axb) B(bxc) to koszt ich mnożenia to: a*b*c

Funkcja: f(M,a,b) :            
                     b 
                    min(f(M,a,x) + f(M,x+1,b)+ g(M,a,x,b))
                    x=a
                    0, a=b

Funkcja g(M,a,x,b) = M[a][0] * M[x][1] * M[b][1]      

Spamiętywanie w tablicy dwuwymiarowej              
            b   
    [__      ]   
   a[  |     ]
    [   __   ]
    [     |__]               

________________________________________________________________________________________________________________________
Wydawnie monet
np: N = {2,3,5,7,11,13]
    k = 27
Chcemy zwrocić liczbe monet

                 len(N)-1
Funkcja: F(N,k): min({f(N,k - N[i])+1 | N[i]<=k})
                 i=0
                Warunki brzegowe: 0,  k == 0
                Możemy spamiętywać w tablicy jakie monety sprawdzaliśmy
                Złożonośc: O(k*||N||)                  
________________________________________________________________________________________________________________________
Dwie tablice: A i B które są N-elementowe w z liczbami naturalnymi
a) O(n^2) długość najwiekszego wspolny podciagu(dwa takie same podciągi)

Wykorzystjąc algorytm znajdz algorytm dla najdłuższego podciagu rosnacego O(n^2)


"""
