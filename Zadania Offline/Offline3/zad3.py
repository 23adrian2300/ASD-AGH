# Adrian Żerebiec
"""
Najpierw sprawdzamy czy w ogóle jest możliwe powstanie tablicy bo gdy prawodpodobieństwa będą równe
0 to nie ma sensu sprawdzać. Następnie tworzymy kubełki (jeśli długość tablicy większa to odpowiednio więcej stąd else),
a dokładniej n//10 kubełków, gdyż w ten sposób pozbędziemy się znacznej ilości pustych
Potem tworzymy uzupełniemy nasze kubełki elementami z tablicy przydzielając je w odpowiednie miejsce,
a w nastepnym kroku sortujemy za pomocą Insertionsorta
Na końcu wyciągamy elementy z kubełka i wstawiamy w odpowiednie miejsca w tablicy T którą na końcu zwracamy
"""
# Złożoność: 0(n)

from zad3testy import runtests


def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A


def SortTab(T, P):
    p = len(P)
    for i in range(p):
        if P[i][2] != 0:
            break
        else:
            return  # nie może powstać tablica
    B = []
    n = len(T)
    if n < 10 ** 6:
        bucket_no = n // 10
        for i in range(bucket_no):
            B.append([])

        for element in T:
            bucket_index = int(element * 0.1)
            B[bucket_index].append(element)

        for i in range(bucket_no):
            B[i] = insertionSort(B[i])

        index = 0

        for i in range(bucket_no):
            for j in range(len(B[i])):
                T[index] = B[i][j]
                index += 1
    else:
        bucket_no = n // 10 ** (n // (10 ** 6))
        for i in range(bucket_no):
            B.append([])

        for element in T:
            bucket_index = int(element * (1 / (10 ** (n // (10 ** 6)))))
            B[bucket_index].append(element)

        for i in range(bucket_no):
            B[i] = insertionSort(B[i])

        index = 0

        for i in range(bucket_no):
            for j in range(len(B[i])):
                T[index] = B[i][j]
                index += 1
    return T


runtests(SortTab)
