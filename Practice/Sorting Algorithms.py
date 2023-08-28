# mergesort
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


def heapsort(A):
    def heapify(A, n, i):
        l = 2 * i + 1
        r = 2 * i + 2
        max_ind = i
        if l < n and A[l] > A[max_ind]:
            max_ind = l
        if r < n and A[r] > A[max_ind]:
            max_ind = r
        if max_ind != i:
            A[i], A[max_ind] = A[max_ind], A[i]
            heapify(A, n, max_ind)

    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapify(A, n, i)

    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
    return A


# Quicksort

def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def quicksort_iter(A):
    st = [(0, len(A) - 1)]  # st=[] / st.append(0,len(A)-1)
    while len(st) > 0:
        p, r = st.pop()
        if p < r:
            q = partition(A, p, r)
            st.append((q + 1, r))  # najpierw duży później mały
            st.append((p, q - 1))


def quicksort_bezogona(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1


# select

def select(A, p, k, r):
    if p == r: return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return select(A, q + 1, k, r)
        else:
            return select(A, p, k, q - 1)


# countingsort
def countingsort(A, k):
    n = len(A)
    B = [0] * n
    C = [0] * k
    for x in A: C[x] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1
    for i in range(n):
        A[i] = B[i]


# Lider ciagu
def lider(L, left, right):
    if left > right:
        return None
    k = left
    number = 1
    for i in range(left + 1, right + 1):
        if number == 0:
            k = i
            number = 1
        else:
            if L[k] == L[i]:
                number += 1
            else:
                number -= 1
    if number == 0:
        return None

    number = 0
    for i in range(left, right + 1):
        if L[i] == L[k]:
            number += 1
    if number > (right - left + 1) // 2:
        return k
    else:
        return None


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


# Radixsort

def countingsorty(T, k):
    C = [0]*len(T)
    B = [0]*10
    for i in range(len(T)):
        index = int((T[i]/k) % 10)
        B[index] += 1
    for i in range(1, 10):
        B[i] += B[i-1]
    j = len(T)-1
    while j >= 0:
        index = int((T[j]/k) % 10)
        C[B[index]-1] = T[j]
        B[index] -= 1
        j -= 1
    for i in range(len(T)):
        T[i] = C[i]


def radix_sort(T):
    maximum = 0
    for i in range(len(T)):
        maximum = max(maximum, T[i])
    i = 1
    while maximum/i > 0:
        countingsorty(T, i)
        i *= 10



# bucketsort
def bucket_sort(input_list):
    def insertion_sort(bucket):
        for i in range(1, len(bucket)):
            var = bucket[i]
            j = i - 1
            while (j >= 0 and var < bucket[j]):
                bucket[j + 1] = bucket[j]
                j = j - 1
            bucket[j + 1] = var

    max_value = max(input_list)
    size = max_value / len(input_list)
    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([])
    for i in range(len(input_list)):
        j = int(input_list[i] / size)
        if j != len(input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
    final_output = []
    for x in range(len(input_list)):
        final_output = final_output + buckets_list[x]
    return final_output


"""
heapsort
def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def partent(i):
    return (i - 1) // 2
def heapify2(A, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    max_ind = i
    if l < n and A[l] > A[max_ind]:
        max_ind = l
    if r < n and A[r] > A[max_ind]:
        max_ind = r
    if max_ind != i:
        A[i], A[max_ind] = A[max_ind], A[i]
        heapify2(A, n, max_ind)


def build_heap(A):
    n = len(A)
    for i in range((n - 2) // 2, -1, -1):
        heapify(A, n, i)
================================================


"""

#magiczne piatki
def kthSmallest(arr, l, r, k):
    def findMedian(arr, l, n):
        lis = []
        for i in range(l, l + n):
            lis.append(arr[i])
        lis = mergeSort(lis)
        return lis[n // 2]

    if 0 < k <= r - l + 1:
        n = r - l + 1
        median = []
        i = 0
        while i < n // 5:
            median.append(findMedian(arr, l + i * 5, 5))
            i += 1
        if i * 5 < n:
            median.append(findMedian(arr, l + i * 5, n % 5))
            i += 1
        if i == 1:
            medOfMed = median[i - 1]
        else:
            medOfMed = kthSmallest(median, 0, i - 1, i // 2)
        pos = parti(arr, l, r, medOfMed)
        if pos - l == k - 1:
            return arr[pos]
        if pos - l > k - 1:
            return kthSmallest(arr, l, pos - 1, k)
        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)

    return float("inf")


def parti(arr, l, r, x):
    for i in range(l, r):
        if arr[i] == x:
            arr[i], arr[r] = arr[r], arr[i]
            break
    x = arr[r]
    i = l
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[j]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
