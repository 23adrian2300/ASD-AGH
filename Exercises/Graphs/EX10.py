"""
Cwiczenia 9

Zadanie 1. Czy graf jest dwudzielny
"""
# BFS, lista wierzchołków - graf jest spójny
import queue


def is_bipartive(G):
    visited = [False for _ in range(len(G))]
    part = [None for _ in range(len(G))]
    visited[0] = True
    part[0] = True
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        u = q.get()
        for i in range(len(G[u])):
            if visited[G[u][i]]:
                if part[G[u][i]] == part[u]:
                    return False
            else:
                visited[G[u][i]] = True
                part[G[u][i]] = part[u]
                q.put(G[u][i])
    return True


"""
Zadanie 2. Policz spójne składowe
"""
from collections import deque


# DFS - reprezentacja macierzowa
def dfs(G):
    counter = 0
    vis = [False for _ in range(len(G))]
    for i in range(len(vis)):
        if not vis[i]:
            vis[i] = True
            counter += 1
            s = deque()
            s = s.append(i)
            while not s.empty():
                u = s.pop()
                for v in range(G[u]):
                    if G[u][v] and not vis[v]:
                        vis[v] = True
                        s.append(v)
    return counter


"""
Zadanie 3. Siec telekomunikacyjna
"""
# BFS - drzewo z rodzicami danego wierzchołka

# DFS - z kolejnoscia wierzchołkow


"""
Zadanie 4. czy w grafie istnieje cykl długosci 4 (skierowany, ważony)
1)Sprawdzić każdą 4
2)
"""


# nie BFS i nie DFS - 0(V^3)

def brate(G):
    n = len(G)
    # for a in range(n):
    #     for (b..)
    #         for (c..)
    #             for (d..)
    for a in range(n):
        counter = 0
        for b in range(a + 1, n):
            for i in range(0, n):
                if i != a and i != b and G[a][i and G[i][b]]:
                    counter += 1
        if counter >= 2:
            return True
    return False


"""
Zadanie 5.  Uniwersalne ujscie
Czy z kazdego wierzchołka wychodzą krawedzie do jednego(skierowane) a z tego wierzchołka nie wychodzi zadna
rep(mac)
"""


def in_count(G, u):
    count = 0
    for i in range(len(G)):
        if G[i][u]:
            count += 1
    return count


def out_count(G, u):
    count = 0
    for i in range(len(G)):
        if G[u][i]:
            count += 1
    return count


def sink(G):
    n = len(G)
    for i in range(n):
        if in_count(G, i) == n - 1 and out_count(G, i) == 0:
            return True
    return False
# przechodzneie po macierzy -  jesli spotkamy 0 idziemy w prawo jesli 1 to w dół i idziemy poki nie wyjdziemy poza macierz