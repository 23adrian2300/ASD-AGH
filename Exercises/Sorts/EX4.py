"""
Sortowanie liniowe
_______________________________________________________________________________________________________________________
Algorytmy który w czasie liniowym sortuje liczby w tablicy N-elementowej w zakresie [0....n^2]

counting sort ma 4 pętle:
- zerowanie liczników
- zliczanie - ile razy dany element
- kumulowanie
- wpisywaanie
"""
A = [2, 3, 14, 23, 1]


def radixinnn(A):
    n = len(A)
    B = [0 for _ in range(n)]
    C = [0 for _ in range(n)]
    for x in A:
        C[x % n] += 1
    for i in range(1, n):
        C[i] += C[i - 1]
    for i in range(n - 1, -1, -1):
        k = A[i] % n
        C[k] -= 1
        B[C[k]] = A[i]
    C = [0 for _ in range(n)]
    for x in B:
        C[x // n] += 1

    for i in range(1, n):
        C[i] += C[i - 1]
    for i in range(n-1,-1,-1):
        k = (B[i] // n)
        C[k] -= 1
        A[C[k]] = B[i]
    return A

print(radixinnn(A))

"""
------------------------------------------------------------------------------------------------------------------------
Dana jest tablica A długości N. Wartosci są ze zbioru B, gdzie |B|=logN. 

Nowa tablcia, wstawiamy wartosci do nowej tabli bo bedzie ich tylko logN, 
wstawienie zajmuje log(logN)
log^2 N zajmuje wstwaienie wszytskich elementów (Nlog(logN))
skoro mamy liczniki i poźniej przepisać to do tablic(countsort)
łączna złożoność Nlog(logN) 



------------------------------------------------------------------------------------------------------------------------
Mając dane słowa A i B długości N, składajace sie z alfabetu długości N. Sprawdz czy słowo B jest anagramem liczby A
np: algorytm i logarytm. Ma być złożoność 0(n). 

nowa tablica rozmiaru k którą zerujemy
zliczamy ile razy wystepuje kazda litera w słowie a
nastepnie słowem b zmniejszamy i sprawdzamy czy wszytsko równe 0
"""


def anagrams(A, B, k):
    K = [0 for _ in range(k)]  # zerujemy tylko miejsca które były w A reszta smieci
    n = len(A)
    for i in range(n):
        K[ord(A[i])] += 1
        K[ord(B[i])] -= 1
    for i in range(n):
        if K[i] != 0:
            return False
    return True


# t = numpy.empty(n,int)
print(anagrams("adam", "mada", 256))

"""
------------------------------------------------------------------------------------------------------------------------
Pewien eksperyment fizyczny generuje szybko liczby z pzredziału [0...10^9-1] (Pewne paczki danych)
{}{}{}{}{}     {}{}{}{}{}{}{}      {}{}{}{}{}{}{}{}
ile różnych liczb znajduje się w danej paczce, złożoność 0(n)
zaproponuj strukture danych ktora pozwoli na przeprowadzenie eksperymrntu

tworzymy tablice C z indeksami od 0 do 10^9-1 
tworzymy licznik, sprawdzamy czy jest 0, wtedy licznik zwiększamy global licz.........(nuerowanie pakietów)

spoosb 2:
tworzymy tablice z boolami i aderesami (stos) 

------------------------------------------------------------------------------------------------------------------------
Mamy tablice o rozmiaze N. Prosze zaproponowac algorytm ktory znajduje dwie liczby x,y takieze różnice y-x jest najwieksza
takie zeby nie istaniałą liczba z miedzy nimi. Czas 0(n). Szukamy x i y takich ze y-x jest max i nie istnieje z ktore jest x<z<y

bucket sort: moze być liczba kubełków stała razy n
tworzymy n kubełków - zakres z min max, jesli mamy pusty kubełek szykamy dookoła niego z lewej naweikszy z prawej najmniejszy
w pierwszym jest min, a w ostanim max( wiec zanjdziemy lioniowo bo wezmeimy najwiekszy z 1 i poźniej najmnijeszy z ostatniego)
(musza być dwa puste!!!!!!!!!!!!) np [0,1)[1,2)


------------------------------------------------------------------------------------------------------------------------
Dana jest tablica 2 wymiarowo gdzie mamy k wierszy i mamy n elementów, k pasków w kazdym eleemnty uporządkowane rosnące. 
znajdz elelment który wystepuje nejwięcej razy i musi być co najmniej w 1/3 eleemntów
posortowane
merge(nlog(k)) parami merge albo kopiec i liniowo przebiegamy nlogk
oczekiwane: n (mały lider)



------------------------------------------------------------------------------------------------------------------------
dana jest tablica n elementowa a kazdy elekembnt ma jeden z k kolorów [liczby całkowite] [0...k]
znajdz najmniejszy pzredział w którym są wszytskie kolory,
idziemy j az znajdziemy wszytskie kolory i pzresuawamy i w tablicy k zwiekszam licznik w tab i licznik róznych kolorów

"""
