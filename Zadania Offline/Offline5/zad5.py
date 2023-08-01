#Adrian Żerebiec

#Algorytm zachlanny
from zad5testy import runtests

import heapq

def plan(T):
    stops = []
    curr_range = 0
    n = len(T)
    last = -1
    heap = []
    while curr_range < n - 1:
        mini = min(curr_range + 1, n)
        for i in range(last + 1, mini):
            heapq.heappush(heap, (-T[i], i))
            last = i
        soil, spos = heapq.heappop(heap)
        curr_range += -soil
        stops.append(spos)
    return sorted(stops)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
