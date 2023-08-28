"""
1) Las na osi
0    1    2     3 .....      n-1
-----|---------|-------|---->

ci -zysk z wycinki i-tego drzewa
nie możemy wyciąć 2 sąsiednich drzew

Funckja:
         { C0, i=0
f(C,i) = { max(C0,C1), i=1 wybieramy jedno z 2
         { max(f(C,i-1), f(C,i-2)+Ci)
            nie scinamy
________________________________________________________________________________________________________________________
"""


def las(C, n):
    T = [-1 for _ in range(n)]
    T[0], T[1] = C[0], max(C[0], C[1])

    def f(C, i):
        if T[i] != -1:
            T[i] = max(f(C, i - 1), f(C, i - 2) + C[i])
        return T[i]

    return f(C, n - 1)


"""
alternatywnie:
    for i in range(2,n):
        T[i] = max(T[i-1],T[i-2]+C[i])
return T[n-1]
________________________________________________________________________________________________________________________
"""
"""
2) n spadających klocków na oś liczbową
Usuwamy je tak aby stworzyć piramidkę czyli ten leżący na innym nie możę wykraczać poza jego obręb
------------------------------------->
            { false, k>i
f(T,k,i) =  { true, k == 1 
            { f(T,i-1,k) || istnieje {f(T,i-j,k-1) | j nalezy {1,i} (ai>a id(j-i) i bi<b id(i-j)} 


g(T): argmax {f(T,i,k) == true
             { e nal {0,|T|}
"""


def g(T):
    n = len(T)
    res = [[-1 for _ in range(n)] for j in range(n)]

    for i in range(n):
        T[i][0] = True
        for j in range(i + 1, n + 1):
            res[i][j] = False
        for k in range(n, 0, -1):  # ???????????????
            if f(T, i, k, res):
                return k


def f(T, i, k, res):
    if res[i][k] == None:
        res[i][k] = f(T, i - 1, k, res)
        for j in range(1, i + 1):
            if T[i][0] >= T[i - j][0] and T[i][1] <= T[i - j][1]:
                res[i][k] = res[i][k] or f(T, i - j, k - 1, res)
        return res[i][k]


"""
f(i) =  {1, i = n-1
        { max f(i) if can_build(k,i)
        { k<i
________________________________________________________________________________________________________________________        
"""

"""
3) prom o długości l z dwoma pasami dla samochodów, kazdy samochód ma swoją długość
ile samochodów zmieści sie na promie wiezdzając po kolei A - tablica n elementowa, wymiary w metrach
j - wolne miejsce na 2 pokładzie
k - wolne miejsce na 1 pokładzie
             { 0, A[i]>j and A[i]>k
f(A,j,k,i) = {f(A,j,k-A[i],i+1) A[i] >k
             {f(A,j-[A[i], k,i+1) A[i]>j
             { max z 2,3 linijki A[i] <=j and A[i]<=k możemy na 2 linijkach
________________________________________________________________________________________________________________________
4) Zaba - os liczbowa, zaba chce sie dostac na n-1 pozycje, skok o 1 wartosc zmieneiejsza jej energie
na osi zanjdują się przekąski dodające energie, na T[0] jest na pewno energia, minimlana liczba skoków tak aby dotrzec do n-1 
oraz aby energia != 0 (Głupie ale funkcja jest xD)
zawsze jest przekąska na polu zanczy ze jest zawsze rozwiazanie

f(T,i,e) =  { 0 , i>=n 
            {   e
            { min{f(T,i+k,e-k+T[i+k)}             
               k=0

f(T,0,T[0])
_________________________________________________________________________________________________________________________
5) Algorytm plecakowy ale z dodatkowym ograniczeniem na maks wage i wysokosc

"""
