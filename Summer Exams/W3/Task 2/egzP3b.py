from egzP3btesty import runtests
from queue import PriorityQueue


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def adding_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result


def lufthansa(G):
    sol = 0
    B = []
    n = len(G)
    for i in range(n):
        for j in range(len(G[i])):
            if i < G[i][j][0]:
                sol += G[i][j][1]
                B.append((i, G[i][j][0], G[i][j][1]))
    B = sorted(B, key=lambda x: -x[2])
    graph = Graph(len(G))
    for i in B:
        graph.adding_edge(i[0], i[1], -i[2])
    mst_result = graph.kruskal_mst()
    for i in range(len(mst_result)):
        mst_result[i][2] = -mst_result[i][2]
    i = 0
    while i < len(mst_result):
        if B[i][2] == mst_result[i][2]:
            i += 1
        else:
            break
    j = i
    mst = 0
    for i in range(len(mst_result)):
        mst += mst_result[i][2]
    mst += B[j][2]

    return sol - mst


runtests(lufthansa, all_tests=True)
