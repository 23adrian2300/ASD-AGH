# Adrian Żerebiec
# Tworzymy klase Graph w której tworzymy strukturę grafu, dodajemy krawędzi, sortujemy oraz szukamy naszego rozwiazania.
# Funckja how_long oblicza potrzebną ilość dni, w głownej funkcji dodajemy także krawędzi do grafu.
# Funckja searching_sol wykonuje pętle for tyle razy ile mamy krawędzi. Początkowo wypełniamy tablice parent i rank, odpowiednio
# numerami wierzchołków oraz zerami. Następnie wykorzystujemy pętle while to stworzenia tablic z możliwymi wartościami przejscia
# Po wszytskich wierzchołkach. W niej szukamy funkcja find rodziców w drzewie dla wierzchołków tej samej krawędzi a poźniej
# wykorzytsjąc tablice rank i parent w momencie gdy x != y szukamy częsci wspólnej. Dodajemy days do tablicy z wynikami
# i szukamy tego który daje najmneijszą różnice
from zad8testy import runtests


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


class Graph:
    def __init__(self, v):
        self.graph = []
        self.vertex = v

    def edges(self, i, j, days):
        self.graph.append([i, j, days])

    def sorted_graph(self):
        self.graph = sorted(self.graph, key=lambda elem: elem[2], reverse=True)

    def searching_sol(self, n):
        gleng = len(self.graph)
        minimum = float("inf")
        self.sorted_graph()
        for i in range(gleng):
            e = 0
            pos_solution = []
            parent = []
            rank = []
            for link in range(self.vertex):
                parent.append(link)
                rank.append(0)
            while i < gleng and e < self.vertex - 1:
                x, y, days = self.graph[i]
                x = find(parent, x)
                y = find(parent, y)
                if y != x:
                    if rank[x] > rank[y]:
                        parent[y] = x
                    elif rank[x] < rank[y]:
                        parent[x] = y
                    else:
                        parent[y] = x
                        rank[x] += 1
                    pos_solution.append(days)
                    e += 1
                i += 1

            potential = max(pos_solution) - min(pos_solution)
            if len(pos_solution) == n - 1 and minimum > potential:
                minimum = potential
                if minimum == 0:
                    return minimum

        return minimum


def highway(A):
    n = len(A)
    graph = Graph(n)
    checking = []

    def ceil(res):
        return -(-int(res))

    def how_long(a, b):
        return ceil((((a[0] - b[0]) * (a[0] - b[0])) + ((a[1] - b[1]) * (a[1] - b[1]))) ** (1 / 2))

    if len(A) == 1 or len(A) == 0:
        return 0

    for i in range(n - 1):
        for j in range(i + 1, n):
            if (A[i], A[j]) or (A[j], A[i]) not in checking:
                graph.edges(i, j, how_long(A[i], A[j]))
                checking.append((A[i], A[j]))

    return graph.searching_sol(n)


runtests(highway, all_tests=True)
