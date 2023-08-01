"""
Adrian Żerebiec
Algorytm rozwiązujący zadany problem wykorzytsuje implementacje algorytmu Forda-Fulkersona, czyli Edmondsa-Karpa.
Funkcja matrix_generator początkowo znajduje wierzchołki grafu, następnie tworzy tablice 2d, wypełnioną zerami, o długości len(vertex)+1, którą
wypełnia odpowiednimi wartościami - w tym przypadku są to przepustowości rurociągów. Funkcja zwraca także jej długość.
Funkcja edmonds_karp wykorzystując bfs, zwiększa przepływ dowolnej ścieżki ze źródła aż do jej ujścia, jeśli jest to tylko możliwe.
W głównej funkcji wykorzytsujemy tablice tworzoną przez matrix_generator i tworzymy dzięki map nową listę w której zmieniamy wartosci
new_g[i][n] oraz new_g[j][n] na float("inf") i  wywołujemy edmonds_karp dla zadanego s oraz n. Na końcu funkcja zwraca największą
możliwą wartość.
"""

from zad9testy import runtests


def matrix_generator(G):
    vertex = []
    for elements in G:
        if elements[0] not in vertex:
            vertex.append(elements[0])
        if elements[1] not in vertex:
            vertex.append(elements[1])
    n = len(vertex)
    mat = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(len(G)):
        mat[G[i][0]][G[i][1]] = G[i][2]
    return mat, n


def BFS(g, s, t, parent):
    visited = [False for _ in range(t + 1)]
    queue = [s]
    visited[s] = True
    while queue:
        element = queue.pop()
        for i, el in enumerate(g[element]):
            if visited[i] or el <= 0:
                continue
            queue.append(i)
            visited[i] = True
            parent[i] = element
            if i == t:
                return True
    return False


def edmonds_karp(graph, source, sink):
    max_flow = 0
    parent = [-1 for _ in range(sink + 1)]
    bfs = BFS(graph, source, sink, parent)
    while bfs:
        path_flow = float("inf")
        s = sink
        while s != source:
            if path_flow > graph[parent[s]][s]:
                path_flow = graph[parent[s]][s]
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[v][u] += path_flow
            graph[u][v] -= path_flow
            v = parent[v]
        bfs = BFS(graph, source, sink, parent)
    return max_flow


def maxflow(G, s):
    sol = 0
    mat, n = matrix_generator(G)
    for i in range(n):
        for j in range(i, n):
            if i != s and j != s:
                new_g = list(map(list, mat))
                new_g[i][n] = float("inf")
                new_g[j][n] = float("inf")
                value = edmonds_karp(new_g, s, n)
                if value > sol:
                    sol = value
    return sol


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
