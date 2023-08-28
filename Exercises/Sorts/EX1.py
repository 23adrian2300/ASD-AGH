# Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
# kolejność jej elementów.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def print_ll(first):
    while first is not None:
        print('-->', first.val, end=' ')
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


def odwr(p):
    if p == None:
        return
    if p.next == None:
        return p

    k = None
    prev = p
    curr = prev.next
    while prev is not None:
        prev.next = k
        k = prev
        prev = curr
        if curr is not None:
            curr = curr.next
    return k


t = [9, 4, 5, 7, 2, 8, 4, 6, 3, 3]
new2 = make_ll(t2)
new = make_ll(t)
# print_ll(new)
# print_ll(odwr(new))
print_ll(new)
print("___________________________________________________________")


# print("\n")


# Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
# funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
# wartość.

def push_front(p, value):
    q = Node(value)
    q.next = p
    return q


def push_back(first, val):
    if first is None:
        return Node(val)

    p = first
    while p.next is not None:
        p = p.next

    p.next = Node(val)
    return first


# print_ll(push_back(new,5))
# print_ll(push_front(new,0))


# Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
# element listy. Do funkcji należy przekazać wskazanie na pierwszy element
# listy


def remove2(first):
    if first == None:
        return
    p = first
    while p.next is not None:
        tmp = p.next.next
        p.next = tmp
        if p.next is not None:
            p = p.next
    return first

# print_ll(remove2(new))

# Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
# której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
# element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
# elementu o zadanym kluczu brak w liście należy element o takim kluczu
# wstawić do listy


def kokl(p, value):
    if p is None:
        return Node(value)
    k = p
    while k.next is not None:
        if k.next.val == value:
            k.next = k.next.next
            return p
        k = k.next

    k.next = Node(value)
    return p

# print_ll(kokl(new2,4))


# Znajdz najwiekszy element tablicy nie wykorzystujac porownan oraz min max > <


t = [1, 2, 3, 90, 2, 3, 4, 5, 7, 1, 83, 0, -19, 92, 8921, 929, 772, 821, 9321, 11111]
t2 = [0, -2, 0, 1]


def poro(a, b):
    if b == 0:
        return a
    if a // b == 0:
        return b
    else:
        return a


def wheremax(t):
    n = len(t)
    maxi = t[0]
    for i in range(n - 1):
        maxi = poro(maxi, t[i + 1])
    return maxi


# print(wheremax(t))
# print(wheremax(t2))
# print(-10 // 10)

"""
max(a,b) = (a+b+abs(a-b))/2
dla tablicy t[10]
max = t[0]
for i in range(1,n):
max = (max + t[i]+abs(max-t[i]))/2
"""

# Sortowanie struktury odsyłaczowej

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
#odwracanie listy
#tablica, nieposrt elm, min, max i indeksy, krków dla dwoch 3/2n
#dana jest tablica t posortowana(liczby pierwsze), dana jest liczba x, szukamy i,j, szukamy t[j] -t[i] = x
#gdy nie istnieje zwracamy None


def findmaxandremove(first):
    maxel = first.val
    maxprev = first
    tmp = first
    prevtmp = first.next
    while tmp is not None:
        if maxel.val < tmp.val:
            maxprev = prevtmp
            maxel = tmp
        prevtmp = tmp
        tmp = tmp.next
    maxprev.next = maxel.next
    return maxel


def sort_wybier(f):
    res = None
    guard = Node(-1)
    guard.next = f
    f = guard
    while f.next is not None:
        max = findmaxandremove(f)
        max.next = res
        res = max
    return res

#Insertion sort


def sort(t):
    n = len(t)
    for j in range(1, n):
        key = t[j]
        i = j - 1
        while i >= 0 and t[i] > key:
            t[i + 1] = t[i]
            i = i - 1
        t[i + 1] = key
    return t


# print(sort(t))
