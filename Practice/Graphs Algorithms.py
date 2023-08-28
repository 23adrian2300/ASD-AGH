def DFS(G):  # tab sasidztwa
    def dfsVisit(G, v):
        nonlocal time
        time += 1
        visited[v] = True
        for i in range(len(G[v])):
            u = G[v][i]
            if not visited[u]:
                parent[u] = v
                dfsVisit(G, u)
            time += 1

    n = len(G)
    time = 0
    visited = [False] * n
    parent = [None] * n
    for v in range(n):
        if not visited[v]:
            dfsVisit(G, v)
    return parent


def dfs(graph, node, visited):  # lista sasiedztwa
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            dfs(graph, n, visited)
    return visited


def DFSmatrix(graph, root):  # matrix
    def dfs_visit(u, graph, visited, result):
        nonlocal time
        visited[u] = True
        result.append(u)
        for i in range(len(graph)):
            if visited[i] is False and graph[u][i] == 1:
                dfs_visit(i, graph, visited, result)
            time += 1

    time = 0
    visited = [False] * len(graph)
    result = []
    dfs_visit(root, graph, visited, result)
    return result


def BFS(graph, root):  # lista sasiedztwa
    queue = []
    visited = [False] * len(graph)
    result = []
    queue.append(root)
    visited[root] = True

    while queue:
        u = queue[0]
        queue.pop(0)
        result.append(u)
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

    return result


def bfs(G):  # lista sasiedztwa
    n = len(G)
    d = [0] * n
    queue = []
    parent = [None] * n
    visited = [False] * n
    queue.append(0)
    visited[0] = True
    while queue:
        v = queue[0]
        queue.pop(0)
        for i in range(len(G[v])):
            nei = G[v][i]
            if not visited[nei]:
                visited[nei] = True
                parent[nei] = v
                queue.append(nei)
                d[nei] += d[v] + 1
    return parent, d


from queue import Queue


def BFSmatrix(graph, root):  # matrix
    queue = []
    visited = [False] * len(graph)
    result = []
    queue.append(root)
    visited[root] = True

    while queue:
        u = queue[0]
        queue.pop(0)
        result.append(u)
        for v in range(len(graph)):
            if visited[v] is False and graph[u][v] == 1:
                queue.append(v)
                visited[v] = True

    return result


def detect_cycle(graph, source):  # cykle/sasiedztwa
    def dfs(graph, source):
        visited[source] = True
        for v in graph[source]:
            if not visited[v]:
                parent[v] = source
                return dfs(graph, v)
            elif visited[v] and parent[source] != v:
                return True
        return False

    visited = [False] * len(graph)
    parent = [None] * len(graph)
    return dfs(graph, source)


def topological_sort(graph):  # sasiedztwa
    def dfs(graph, source, visited, result):
        visited[source] = True
        for v in graph[source]:
            if not visited[v]:
                dfs(graph, v, visited, result)
        result.insert(0, source)

    visited = [False] * len(graph)
    result = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, result)
    return result


def eulerian_path(graph):  # matrix
    def dfs(graph, source):
        for i in range(len(graph)):
            if graph[source][i] == 1:
                graph[source][i], graph[i][source] = 0, 0
                dfs(graph, i)
        result.append(source)

    for i in range(len(graph)):
        edges = 0
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                edges += 1
        if edges % 2 == 1:
            return False

    result = []
    dfs(graph, 0)
    result.reverse()
    return result


def SCC(graph):
    def dfs(graph, source, visited, result, index):
        visited[source] = True
        result[index].append(source)
        for v in graph[source]:
            if not visited[v]:
                dfs(graph, v, visited, result, index)

    def DFSUtil(graph, source, visited, stack):
        visited[source] = True
        for v in graph[source]:
            if not visited[v]:
                DFSUtil(graph, v, visited, stack)
        stack.append(source)

    def transpose_graph(graph, new_graph):
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                new_graph[graph[i][j]].append(i)

    visited = [False] * len(graph)
    stack = []

    for i in range(len(graph)):
        if not visited[i]:
            DFSUtil(graph, i, visited, stack)

    new_graph = [[] for _ in range(len(graph))]
    transpose_graph(graph, new_graph)

    for j in range(len(visited)):
        visited[j] = False
    result = [[] for _ in range(len(graph))]
    index = 0

    while len(stack):
        u = stack.pop()
        if not visited[u]:
            dfs(new_graph, u, visited, result, index)
            index += 1

    return result


def sss(G):  # lista sasiedztwa
    def dfsVisit(G, v):
        nonlocal time
        time += 1
        visited[v] = True
        timer[v] = (time, v)
        for i in range(len(G[v])):
            u = G[v][i]
            if not visited[u]:
                parent[u] = v
                dfsVisit(G, u)
            time += 1

    def dfsUntil(G, v):
        visited[v] = True
        dag[l].append(v)
        for i in range(len(G[v])):
            u = G[v][i]
            if not visited[u]:
                parent[u] = v
                dfsUntil(G, u)

    n = len(G)
    time = 0
    timer = [0] * n
    visited = [False] * n
    parent = [None] * n
    for v in range(n):
        if not visited[v]:
            dfsVisit(G, v)
    graph = [[] for i in range(n)]
    for i in range(n):
        for ver in G[i]:
            graph[ver].append(i)
    timer = sorted(timer)
    visited = [False] * n
    parent = [None] * n
    dag = [[]]
    l = 0
    for i in range(n):
        if not visited[timer[i][1]]:
            dfsUntil(graph, timer[i][1])
            if i != n - 1:
                dag.append([])
                l += 1
    return dag


from math import inf


def bridge(graph):  # sasiedztwa
    def dfs(graph, source):
        nonlocal time
        visited[source] = True
        time_visit[source] = time
        time += 1
        low[source] = time_visit[source]
        for v in graph[source]:
            if not visited[v]:
                parent[v] = source
                dfs(graph, v)
                low[source] = min(low[source], low[v])
            elif parent[source] != v:
                low[source] = min(low[source], time_visit[v])

    visited = [False] * len(graph)
    time_visit = [0] * len(graph)
    low = [inf] * len(graph)
    parent = [None] * len(graph)
    time = 0

    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i)

    for i in range(len(graph)):
        if time_visit[i] == low[i] and parent[i] is not None:
            print(parent[i], i)

time = 0
def acc(g):
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



def paths_in_DAG(edges, start, end):  # lista krawdzi
    def dfs(graph, source):
        visited[source] = True
        for v in graph[source]:
            if not visited[v]:
                DP[v] = 1
                dfs(graph, v)
            elif visited[v]:
                DP[v] += 1
                dfs(graph, v)

    max_vertex = 0
    for i in range(len(edges)):
        max_vertex = max(max_vertex, max(edges[i]))

    graph = [[] for _ in range(max_vertex + 1)]

    for i in range(len(edges)):
        graph[edges[i][0]].append(edges[i][1])

    DP = [0] * len(graph)
    visited = [False] * len(graph)
    dfs(graph, start)
    return DP[end]


class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def make_set(v):
    return Node(v)


def convert_to_edges(graph):
    edges = []

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (graph[i][j][0], i, graph[i][j][1]) not in edges:
                edges.append((i, graph[i][j][0], graph[i][j][1]))

    return edges


def kruskal_algorithm(graph):  # lista sasiedztwa
    edges = convert_to_edges(graph)
    edges.sort(key=lambda x: x[2])
    MST = []
    V = []

    for i in range(len(graph)):
        V.append(make_set(i))

    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])

    return MST


def kruskal_algorithmmat(graph):  # matrix
    def convert_to_edges(graph):
        edges = []
        for i in range(len(graph)):
            for j in range(len(graph)):
                if graph[i][j] != 0 and (j, i, graph[i][j]) not in edges:
                    edges.append((i, j, graph[i][j]))
        return edges

    edges = convert_to_edges(graph)
    edges.sort(key=lambda x: x[2])
    MST = []
    V = []

    for i in range(len(graph)):
        V.append(make_set(i))

    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]
        if find(V[u]) != find(V[v]):
            MST.append(edges[i])
            union(V[u], V[v])

    return MST


from queue import PriorityQueue


def prim_algorithm(graph, source):  # lista sasiedztwa
    queue = PriorityQueue()
    parent = [None] * len(graph)
    d = [inf] * len(graph)
    d[source] = 0
    visited = [False] * len(graph)
    visited[source] = True
    queue.put((0, source))

    while not queue.empty():
        dist, u = queue.get()
        visited[u] = True
        for v in graph[u]:
            vertex = v[0]
            weight = v[1]
            if d[vertex] > weight and not visited[vertex]:
                parent[vertex] = u
                d[vertex] = weight
                queue.put((d[vertex], vertex))

    MST = []

    for i in range(len(parent)):
        if parent[i] is not None:
            MST.append((i, parent[i], d[i]))

    return MST


def prim_algorithmmat(graph, source):  # matrix
    queue = PriorityQueue()
    parent = [None] * len(graph)
    key = [inf] * len(graph)
    key[source] = 0
    visited = [False] * len(graph)
    visited[source] = True
    queue.put((0, source))

    while not queue.empty():
        dist, u = queue.get()
        visited[u] = True
        for i in range(len(graph)):
            if graph[u][i] != 0 and key[i] > graph[u][i] and not visited[i]:
                parent[i] = u
                key[i] = graph[u][i]
                queue.put((key[i], i))

    result = []

    for i in range(len(parent)):
        if parent[i] is not None:
            result.append((i, parent[i], key[i]))

    return result


def dijkstra_algorithm(graph, source):
    def relax(u, v):
        if distance[v[0]] > distance[u] + v[1]:
            distance[v[0]] = distance[u] + v[1]
            parent[v[0]] = u
            return True
        return False

    queue = PriorityQueue()
    queue.put((0, source))
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    visited = [False] * len(graph)
    distance[source] = 0

    while not queue.empty():
        dist, u = queue.get()
        for v in graph[u]:
            if not visited[v[0]] and relax(u, v):
                queue.put((dist + v[1], v[0]))
        visited[u] = True

    return parent, distance


def dijkstra_algorithmmat(graph, source):  # matrix
    def relax(graph, u, v):
        if distance[v] > distance[u] + graph[u][v]:
            distance[v] = distance[u] + graph[u][v]
            parent[v] = u
            return True
        return False

    queue = PriorityQueue()
    queue.put((0, source))
    visited = [False] * len(graph)
    parent = [None] * len(graph)
    distance = [inf] * len(graph)
    distance[source] = 0

    while not queue.empty():
        dist, u = queue.get()
        for v in range(len(graph[u])):
            if graph[u][v] != 0 and not visited[v]:
                if relax(graph, u, v):
                    queue.put((dist + graph[u][v], v))
        visited[u] = True

    return parent, distance


def bellman_ford_algorithm(graph, source):  # lista krawedzi
    def relax(graph, j):
        if distance[graph[j][1]] > distance[graph[j][0]] + graph[j][2]:
            distance[graph[j][1]] = distance[graph[j][0]] + graph[j][2]
            parent[graph[j][1]] = graph[j][0]

    V = 0

    for i in range(len(graph)):
        V = max(V, graph[i][0], graph[i][1])

    E = len(graph)
    distance = [inf] * (V + 1)
    parent = [None] * (V + 1)
    distance[source] = 0

    for i in range(V - 1):
        for j in range(E):
            relax(graph, j)

    for i in range(E):
        if distance[graph[i][1]] > distance[graph[i][0]] + graph[i][2]:
            return False

    return True, distance, parent


def Floyd_Warshall_algorithm(graph):  # matrix
    distance = [[inf] * len(graph) for _ in range(len(graph))]

    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != 0:
                distance[i][j] = graph[i][j]

    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                distance[u][v] = min(distance[u][v], distance[u][k] + distance[k][v])

    return distance


def floyd_warshall_path(graph):  # matrix ale jak nie ma to -1
    distance = [[inf] * len(graph) for _ in range(len(graph))]
    parent = [[None] * len(graph) for _ in range(len(graph))]

    for i in range(len(distance)):
        for j in range(len(distance)):
            if i == j:
                distance[i][j] = 0
            elif graph[i][j] != -1:
                distance[i][j] = graph[i][j]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] != -1:
                parent[i][j] = i

    for k in range(len(graph)):
        for u in range(len(graph)):
            for v in range(len(graph)):
                if distance[u][v] > distance[u][k] + distance[k][v]:
                    distance[u][v] = distance[u][k] + distance[k][v]
                    parent[u][v] = parent[k][v]

    return parent


def edmonds_karp_algorithm(graph, s, t):  # matrix
    def bfs(graph, s, t):
        queue = []
        visited = [False] * len(graph)
        visited[s] = True
        queue.append(s)
        while queue:
            u = queue[0]
            queue.pop(0)
            for v in range(len(graph)):
                if not visited[v] and graph[u][v] != 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
        return visited[t]

    parent = [None] * len(graph)
    max_flow = 0

    while bfs(graph, s, t):
        current_flow = inf
        current = t
        while current != s:
            u = parent[current]
            current_flow = min(current_flow, graph[u][current])
            current = parent[current]  # albo u
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]

    return max_flow


def ford_fulkerson(graph, s, t):
    def dfs_visit(graph, source, visited, parent):
        visited[source] = True
        for v in range(len(graph)):
            if not visited[v] and graph[source][v] != 0:
                parent[v] = source
                dfs_visit(graph, v, visited, parent)

    def dfs(graph, s, t, parent):
        visited = [False] * len(graph)
        dfs_visit(graph, s, visited, parent)
        return visited[t]

    parent = [None] * len(graph)
    max_flow = 0

    while dfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]

    return max_flow


def bfs(graph, s, t, parent):
    queue = Queue()
    visited = [False] * len(graph)
    visited[s] = True
    queue.put(s)
    while not queue.empty():
        u = queue.get()
        for v in range(len(graph)):
            if not visited[v] and graph[u][v] != 0:
                visited[v] = True
                parent[v] = u
                queue.put(v)
    return visited[t]


def ford_fulkerson_algorithm(graph, s, t):
    parent = [None] * len(graph)
    max_flow = 0
    while bfs(graph, s, t, parent):
        current_flow = inf
        current = t
        while current != s:
            current_flow = min(current_flow, graph[parent[current]][current])
            current = parent[current]
        max_flow += current_flow
        v = t
        while v != s:
            u = parent[v]
            graph[u][v] -= current_flow
            graph[v][u] += current_flow
            v = parent[v]
    return max_flow


def multiple_source_and_sinks(graph, source, sink):
    new_graph = [[0] * len(graph) for _ in range(len(graph))]
    start_source = min(source)
    end_sink = min(sink)

    for i in range(len(source)):
        for j in range(len(graph)):
            if graph[source[i]][j] != 0 and j not in source and j not in sink:
                new_graph[start_source][j] = graph[source[i]][j]
            elif j in sink and graph[i][j] != 0:
                new_graph[start_source][end_sink] = graph[source[i]][j]

    for i in range(len(sink)):
        for j in range(len(graph)):
            if graph[sink[i]][j] != 0 and j not in sink and j not in source:
                new_graph[end_sink][j] = graph[sink[i]][j]
            elif j in source:
                new_graph[end_sink][start_source] = graph[sink[i]][j]

    for i in range(len(graph)):
        if i in source or i in sink:
            continue
        for j in range(len(graph)):
            if j not in source and j not in sink and graph[i][j] != 0:
                new_graph[i][j] = graph[i][j]
            elif j in source and graph[i][j] != 0:
                new_graph[i][start_source] = graph[i][j]
            elif j in sink and graph[i][j] != 0:
                new_graph[i][end_sink] = graph[i][j]

    max_flow = ford_fulkerson_algorithm(new_graph, start_source, end_sink)
    return max_flow
