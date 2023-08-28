"""
17.03.2021 Cwiczenia 3
________________________________________________________________________________________________________________________
Zadanie 1. Lider ciągu
np: 2 2 7 1 1 5 2 2 3 więcej niż połowa
Kod z internetu nie z zajęć
________________________________________________________________________________________________________________________
"""


def lider(L, left, right):
    # Wyszukiwanie lidera w ciągu nieuporządkowanym
    if left > right:
        return None
    # Etap I - wykrywanie kandydata na lidera.
    k = left  # kandydat na lidera (indeks)
    number = 1  # krotność kandydata
    for i in range(left + 1, right + 1):
        if number == 0:  # nowy kandydat na lidera
            k = i
            number = 1
        else:  # porównujemy z kandydatem
            if L[k] == L[i]:
                number += 1
            else:
                number -= 1
    # Etap II - sprawdzanie kandydata na lidera.
    if number == 0:  # na liście nie ma lidera
        return None
    # Sprawdzamy ile razy kandydat jest na liście.
    number = 0
    for i in range(left, right + 1):
        if L[i] == L[k]:
            number += 1
    if number > (right - left + 1) // 2:
        return k  # indeks lidera
    else:
        return None  # na liście nie ma lidera


# Zadanie 2. Quicksort rekurencjyjny

def partion(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if x >= A[j]:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partion(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)  # stos systemowy urosnie tyle samo niezaleznie od tego czy najpierw duze czy małe


A = [2, 5, 1, 5, 2, 5, 6, 1, 5, 8, 65, 43, 324, 143, 41, 4124, 1]
"""
pop(0) usuwa 1 element {}{}{}{}{}{}{}{}{} append dodaje na koniec, pop usuwa koniec
________________________________________________________________________________________________________________________
Zadanie 3. Quicksort iteracyny
"""


def quicksort_iter(A):
    st = [(0, len(A) - 1)]  # st=[] / st.append(0,len(A)-1)
    while len(st) > 0:
        p, r = st.pop()
        if p < r:
            q = partion(A, p, r)
            st.append((q + 1, r))  # najpierw duży później mały
            st.append((p, q - 1))


"""
________________________________________________________________________________________________________________________
Zadanie 4. bez rekurencji ogonowej
"""


def quicksort_bezogona(A, p, r):
    while p < r:
        q = partion(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1


# Sortowanie n elementowej tablicy aby wykorzystywac co najwyzej nlogn pamieci sytemowej
# bez while dodajemy ifa i sprawdzamy który mniejszy i tam dajemy quickosort

"""
________________________________________________________________________________________________________________________
Zadanie 5.  Jak scalić k posotrowanych list(linked list)
wyjmujemy z kopca najmniejszy i naprawiamy nlogk

scalanie parami: złożoność nlogk   1z2 3z4 pozniej 12z34

________________________________________________________________________________________________________________________
Zadanie 6. w jaki sposob zrealizowac sturkture danych wykonujacych operacje:
- insert (O(N))
-remove mini (O(1))
-remove max (O(1))
Rozwiązanie przed wdi xD: tablica złożoność logN

Lepsze rozwiazanie:
1)dwa kopce: w kopcach trzymamy poza danymi miejsce w drugim kopcu(indeks bo kopiec to tab)
    kopie z maksem i kpiec z minem
    usuwajac z góry usuwamy z drugiego kopca

________________________________________________________________________________________________________________________
Zadanie 7.  prosze zaimplementowac funkcje wstawiajacy dowolny element do kopca binarnego
nie wolno robić linked listą
Kopiec: drzewo binarne (drzewo kompletne), tablica(musimy zrobic wieksza tablice, na pierwszym miejscu możemy trzymać 
        długość kopcam tablica bedzie wieksza np
        ([7]-tutaj trzymamy liczbe elementów w kopcu) [13][11][7][3][5][2][][][][][][][][][][][][][][][] 
"""


def parent(n): return n // 2


def left(n): return 2 * n


def right(n): return 2 * n + 1


def wstaw(k, val):
    k[k[0] + 1] = val
    # tą wartość porównujemy z rodzicem i jesli wieksza swap z nim

    # heapify naprawia tylko za mały numer za wysoko
    pass

# quicksort Cormen

def partion(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort(A, p, r):
    if p < r:
        q = partion(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    return A

#________________________________________________________________________________________________________________________
# Proszę zaimplementować algorytm QuickSort do sortowania listy jednokierunkowej. 1

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def paritionLast(start, end):
    if (start == end or start == None or end == None):
        return start

    pivot_prev = start
    curr = start
    pivot = end.data

    while (start != end):
        if (start.data < pivot):
            pivot_prev = curr
            temp = curr.data
            curr.data = start.data
            start.data = temp
            curr = curr.next
        start = start.next

    temp = curr.data
    curr.data = pivot
    end.data = temp

    return pivot_prev


def sort(start, end):
    if (start == None or start == end or start == end.next):
        return

    pivot_prev = paritionLast(start, end)
    sort(start, pivot_prev)

    if (pivot_prev != None and pivot_prev == start):
        sort(pivot_prev.next, end)

    elif (pivot_prev != None and pivot_prev.next != None):
        sort(pivot_prev.next.next, end)
    return start


def print_ll(first):
    while first is not None:
        print('-->', first.data, end=' ')
        first = first.next
    print()


def make_ll(t):
    first = None
    n = len(t)
    for i in range(n - 1, -1, -1):
        temp = Node(t[i])
        temp.next = first
        first = temp
    return first


t = [9, 4, 5, 7, 2, 8, 4, 6, 3, 3]
new2 = make_ll(t)
n = new2
while n.next != None:
    n = n.next
print_ll(sort(new2, n))

# Proszę zaimplementować algorytm, który w czasie liniowym sortuje tablicę A zawierającą n liczb ze zbioru [0, 1, ..., n2 − 112] 2
from random import randint


def sorting(n):
    t = [randint(1, n ** 2) for _ in range(n)]

# Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki maja kształty prostokątów (2d), 3
# rury nie maja objętości (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego
# górnego rogu i prawego dolnego rogu. Wiemy, ze do pojemników nalano A wody (oczywiście woda rurami
# spłynęła do najniższych pojemników). Obliczyć ile pojemników zostało w pełni zalanyc
