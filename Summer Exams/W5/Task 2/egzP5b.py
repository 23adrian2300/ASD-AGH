from egzP5btesty import runtests

time = 0


def dfs(g, art, low, d, p, v):
    global time
    children = 0
    time += 1
    low[v] = time
    d[v] = time

    for s in g[v]:
        if d[s] is None:
            children += 1
            dfs(g, art, low, d, p, s)
            if low[s] >= d[v]:
                art[v] = True
            low[v] = min(low[v], low[s])
        else:
            low[v] = min(low[v], d[s])

    return children


def acc(g):
    global time

    n = len(g)

    art = [False for _ in range(n)]
    low = [None for _ in range(n)]
    d = [None for _ in range(n)]
    p = [None for _ in range(n)]

    for i in range(n):
        if d[i] is None:
            if dfs(g, art, low, d, p, i) > 1:
                art[i] = True
            else:
                art[i] = False

    points = 0

    for i in range(n):
        if art[i] == True:
            points += 1

    return points


def koleje(B):
    for i in range(len(B)):
        if B[i][0] > B[i][1]:
            B[i] = (B[i][1], B[i][0])

    B.sort(key=lambda x: (x[0], x[1]))
    n = 0

    for el in B:
        n = max(n, el[1])

    n += 1
    G = [[] for _ in range(n)]
    last = None

    for i in range(len(B)):
        if last != B[i]:
            last = B[i]
            G[B[i][0]].append(B[i][1])
            G[B[i][1]].append(B[i][0])

    return acc(G)



runtests(koleje, all_tests=True)
