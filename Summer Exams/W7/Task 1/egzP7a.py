from egzP7atesty import runtests
from math import inf


# metoda forda fulkersona
def dfs(g, s, t, p):
    def dfsVisit(g, p, i):
        visited[i] = True
        for v in range(len(g)):
            if not visited[v] and g[i][v] != 0:
                p[v] = i
                dfsVisit(g, p, v)

    n = len(g)
    visited = [False] * n
    dfsVisit(g, p, s)
    return visited[t]


def fordfulkersonmatrix(g, s, t):
    p = [None] * len(g)
    max_flow = 0
    while dfs(g, s, t, p):
        currflow = inf
        curr = t
        while curr != s:
            currflow = min(currflow, g[p[curr]][curr])
            curr = p[curr]
        max_flow += currflow
        v = t
        while v != s:
            u = p[v]
            g[u][v] -= currflow
            g[v][u] += currflow
            v = p[v]
    return max_flow


def akademik(T):
    # lista sasiedztwa
    s = len(T) * 2
    t = s + 1
    n = t + 1
    n1 = len(T)

    G = [[] for _ in range(n)]
    for i in range(len(T)):
        for j in range(3):
            if T[i][j] != None:
                G[i].append(n1 + T[i][j])

    for i in range(n1):
        G[s].append(i)
        G[n1 + i].append(t)

    puste = 0
    for i in range(len(T)):
        if T[i] == (None, None, None):
            puste += 1

    # macierz
    G2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(G)):
        for v in G[i]:
            G2[i][v] = 1

    return len(T) - puste - fordfulkersonmatrix(G2, s, t)


runtests(akademik)
