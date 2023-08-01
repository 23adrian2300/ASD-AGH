# Adrian Żerebiec
# Do uzyskania wyniku wykorzystujemy BFS-a. Funkcja shortestpath wykorzystując bfs szuka najkrótszej scieżki w zadanym grafie
# Następnie dzięki uzyskaniej sciezce możemy sprawdzić czy usunięcie którejś z krawedzi najkrótszej sicezki spowoduje jej wydłuzenie
# Do tego wykorzystujemy funckje delete_edge oraz add_edge. W pętli usuwamy odpowiednie krawedzi i patrzymy czy sie wydłuza
# Jesli tak to zamieniamy długosc new, i zapisujemy mini. Po sprawdzeniu wszystkich możliwosci zwracamy mini czyli wierzchołki krawdędzi
# Gdyby jednak nie nastąpiła zmiana to nie zwracamy nic bo długość sie nie zmienia

from zad6testy import runtests
from collections import deque


def delete_edge(G, u, v):
    for i in range(len(G[u])):
        if G[u][i] == v:
            G[u].pop(i)
            break
    for i in range(len(G[v])):
        if G[v][i] == u:
            G[v].pop(i)
            break
    return G


def add_edge(G, u, v):
    G[u].append(v)
    G[v].append(u)
    return G


def bfs(G, s, t, former, distance):
    queue = deque()
    visited = [False for _ in range(len(G))]
    for i in range(len(G)):
        distance[i] = float("inf")
        former[i] = -1
    visited[s] = True
    distance[s] = 0
    queue.append(s)
    while len(queue) != 0:
        u = queue[0]
        queue.popleft()
        for i in range(len(G[u])):
            if visited[G[u][i]] is False:
                visited[G[u][i]] = True
                distance[G[u][i]] = distance[u] + 1
                former[G[u][i]] = u
                queue.append(G[u][i])
                if G[u][i] == t:
                    return True
    else:
        return False


def longer(G, s, t):
    def shortestpath(G, s, t):
        former = [None for _ in range(len(G))]
        distance = [None for _ in range(len(G))]
        if not bfs(G, s, t, former, distance):
            return None
        path = []
        move = t
        path.append(move)
        while former[move] != -1:
            path.append(former[move])
            move = former[move]
        return path

    mini = (0, 0)
    path = shortestpath(G, s, t)
    new = len(path)
    change = False

    for i in range(len(path) - 1):
        delete_edge(G, path[i], path[i + 1])
        new_path = shortestpath(G, s, t)
        if new_path is None:
            return path[i], path[i + 1]
        if len(new_path) > new:
            mini = (path[i], path[i + 1])
            return mini
        add_edge(G, path[i], path[i + 1])
    if change is False:
        return None
    return mini


runtests(longer, all_tests=True)
