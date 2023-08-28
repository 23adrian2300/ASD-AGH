# Heap sort

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[largest] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]


        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


def left(i):
    return (2 * i + 1)


def right(i):
    return (2 * i + 2)


def parent(i):
    return (i - 1) // 2


def heapify(A, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != 1:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify(A, n, max_ind)


def build_heap(A):
    n = len(A)
    for i in range(parent(n - 1), -1, -1):
        heapify(A, n, i)


def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)


# Sortowanie przez scalanie
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        Left = arr[:mid]
        Right = arr[mid:]

        mergeSort(Left)

        mergeSort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                arr[k] = Left[i]
                i += 1
            else:
                arr[k] = Right[j]
                j += 1
            k += 1
        while i < len(Left):
            arr[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            arr[k] = Right[j]
            j += 1
            k += 1
    return arr


def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def merge(T, p, s, k):
    global Tmp
    n = k - p
    l = p
    r = s
    j = p
    while l < s or r < k:
        if l == s:
            Tmp[j] = T[r]
            r += 1
        elif r == k:
            Tmp[j] = T[l]
            l += 1
        elif T[l] <= T[r]:
            Tmp[j] = T[l]
            l += 1
        else:
            Tmp[j] = T[n]
            r += 1
    for i in range(p, k):
        T[i] = Tmp[i]


def mergesort_cw(T, p, k):
    if k - p == 1:
        return
    else:
        s = (k + p) // 2
        mergesort_cw(T, p, s)
        mergesort_cw(T, s, k)
        merge(T, p, s, k)



# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def insertionSort(p):
    sorted = None
    current = p
    while current != None:
        next = current.next
        sorted = sortedInsert(sorted,
                              current)
        current = next
    p = sorted
    return p


def sortedInsert(p, new_node):
    current = None
    if (p == None or
            (p).val >= new_node.val):
        new_node.next = p
        head_ref = new_node
    else:
        current = p
        while (current.next != None and
               current.next.val < new_node.val):
            current = current.next

        new_node.next = current.next
        current.next = new_node

    return p

def push(p, new_data):
    new_node = Node(0)
    new_node.val = new_data
    new_node.next = p
    (p) = new_node
    return p

# kod z internetu
"""
class Node:

    def __init__(self, key):
        self.data = key
        self.next = None

def mergeSort(head):
    if (head.next == None):
        return head

    mid = findMid(head)
    head2 = mid.next
    mid.next = None
    newHead1 = mergeSort(head)
    newHead2 = mergeSort(head2)
    finalHead = merge(newHead1, newHead2)
    return finalHead


def merge(head1, head2):
    merged = Node(-1)

    temp = merged
    while (head1 != None and head2 != None):
        if (head1.data < head2.data):
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next
        temp = temp.next

    while (head1 != None):
        temp.next = head1
        head1 = head1.next
        temp = temp.next

    while (head2 != None):
        temp.next = head2
        head2 = head2.next
        temp = temp.next

    return merged.next

def findMid(head):
    slow = head
    fast = head.next
    while (fast != None and fast.next != None):
        slow = slow.next
        fast = fast.next.next
    return slow


# Function to print list
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next

"""

# Quicksort
def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:

        while start < len(array) and array[start] <= pivot:
            start += 1

        while array[end] > pivot:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]

    return end


def quick_sort(start, end, array):
    if (start < end):
        p = partition(start, end, array)
        quick_sort(start, p - 1, array)
        quick_sort(p + 1, end, array)

"""
dana jest n elementowa tablica posortowana, szukamy 2 elementów które sa rowne sumie t[i]+t[j] =x
n kroków O(nlogn) ale da się liniowo
ustaiwamy dwa wskazniki na pocz i koncu
x=30

  i                    j
 [2,3,5,7,11,13,17,19,23]
wskaznik i przesuwamy gdy suma jest za mala, a j gdy za duza jak sie zatrzyma jest ok

"""


def searchx(t, x):
    # sort(t) - sortujemy tablice chociaz w poleceniu posortowana
    n = len(t)
    j = n - 1
    i = 0
    while True:
        if t[i] + t[j] == x:
            return True
        elif t[i] + t[j] > x:
            j -= 1
        elif t[j] + t[i] < x:
            i += 1
        if i == j:
            return False


t = [2, 3, 5, 13, 19, 23]
print(searchx(t, 30))

"""
dana jest n elementowa tablica posortowana, szukamy 2 elementów które sa rowne sumie t[i]+t[j] =x
n kroków O(nlogn) ale da się liniowo
ustaiwamy dwa wskazniki na pocz i koncu
x=30

  i                    j
 [2,3,5,7,11,13,17,19,23]
wskaznik i przesuwamy gdy suma jest za mala, a j gdy za duza jak sie zatrzyma jest ok

_____________________________________ _______
sortowanie listy odsyłaczowej
stala zloznonosc
rosnie wspolczynnik
mozna scalac serie naturalne - naturalnie posortowane

p1           p2          p
[2] [3] [5] [1] [2] [4] [3] [4] [7] [9]
|    1     |      2    |    3      |
        None          None
wycinamy
while true:
    p1 = odetnij serie naturalna(p)
    if empty(p): brak
    p2 = odetnij serie naturalna (p)
    p3 = scal(p1,p2)
    #scalone serie dodajemy na koniec!!!!!!!!!!!!
    dolacz na koniec(p,p3)

link listy mozna implementowac dodajac wskazania na poczatek i koniec
dolaczanie na koniec jest prostsze
________________________________________________________________________________________________________________________
pojemniki z wodą(zbiorniki)
zbiorniki sa walcami
przekroj wewnetrzny wynosi 1 m2 srednia
wysokosc zbiornika h
miesci sie w im h litrów wody
mamy wspolcrzne y1,y2 zbiornikow, rowno zalanae woda
dane: D[(0,3),((4,9),(2,6)......] - kolejnosc rozna
nalewamy l metrów 3 wody
ile zbiorników jest całkowicie zapełnionych
woda zawsze splywa najnizej


sortujemy tablice D po dolnyuch i gornych na raz
[(0,d),(2,d),(3,g),(4,d)(9,g)]
gdy dotrzemy do dodataniego dodajemy 1 bo tymczasowa pojemnosc osiagnieta!!!!


|||||||||||||||||||||
Wersja bez sortowania

f(H) = L wyznacza ile litrow wody
f^-1 dla litrów wyznaczy h
i przebiagajac po zbiornikach wyliczymy
wyznaczamy to bisekją i w ten sposob szukamy f^-1
intertsuja nas tylko górne indeksy

złożoność: nlogn dla obydwu


_____________________________________________________________________________________________________________________
Dany jest ciag przedziałow (a1,b1)(a2,b2)(a3,b3)
algorytm ktory znajduje przedzial at,bt w ktorym w calosci miesci sie najwiecej innych przedziałow
np [2,4] miesci sie w [2,5] i sa to loczby całkowite
sortujemy dokładnie tak samo jak w poprzednim zadaniu
___________________________________________________________________________________________________________________
"""

# program liczacy liczb einwersji T[i]>T[j]
# bubble sort ale szybszy merge sort

# t = [2, 3, 5, 7, |1, 2, 4, 8]
global licz

def merge(T, p, s, k):
    # zlozonosc nlogn, nie ma sensu alokowac co chwile tablicy, lepiej alokowac globalna

    global Tmp
    n = k - p
    l = p
    r = s
    j = p
    while l < s or r < k:
        if l == s:
            Tmp[j] = T[r]
            r += 1
        elif r == k:
            Tmp[j] = T[l]
            l += 1
        elif T[l] <= T[r]:
            Tmp[j] = T[l]
            l += 1
        else:
            Tmp[j] = T[n]
            r += 1
            licz += s - l
            # tutaj wstawiamy !!!!!!!!!!!!!!!!!!!!!!!!!!

    for i in range(p, k):
        T[i] = Tmp[i]
    return

def mergesort_cw(T, p, k):
    if k - p == 1:
        return 0
    s = (k + p) // 2
    return mergesort_cw(T, p, s) + mergesort_cw(T, s, k) + merge(T, p, s, k)
            #        a                         b                       c
    #return a + b + c

#lider ciągu - przeglądraka i algorytmy lider to element wystepujący więcej niż na połowie pozycji np dla 11 6 razy
#w czasie liniowym, podp. usune 2 elementy różne to w nowej tablicy też bedzie lider!



