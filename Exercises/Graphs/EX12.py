"""
Zad 1. Wieżchołki to miasta, krawędzi to drogi(skierowane) oraz poczatek i koniec
kazda krawdz ma wage
Alicja wybiera kto wsiada pierwszy, przesiadka co miasto

Zad 2. Malajęce krawędzie
Znalezc sciezke ktorej suma jest najmniejsza a kolejne krawedzi sa coraz mniejsze

Dijsktra z tym ze do kolejki wrzucamy je tylko jesli dlugość jest mniejsza

Zad 3. Domkniecie przechodnie
jesli w g' jest sciezka i --> j to G ma taką krawedz

Zad 4. Najlepszy korzeń - drzewo z wagami na gałęziach
Odległość do najbardziej odległego wierzchołka bedzie najwieksza

Zad. 5 Problem stacji benzynowych ale na grafie z wagami

Zad 6. Wymiana walut - tablica kursów k[i][j] po ile w walucie j moge jednostke waluty i ---- graf pełny
czy istnieje waluta tak ze majac walute z mozemy tak ja przechaldnlowac zeby uzyskac wiecej niz jedna sztuke waluty z
"""


# Dana jest tabela kursów walut. Dla każdych dwóch walut 'x' oraz 'y' wpis K[x][y] oznacza ile trzeba
# zapłacić waluty 'x' żeby otrzymać jednostkę waluty 'y'. Proszę zaproponować algorytm, który sprawdza
# czy istnieje taka waluta 'z', że za jednostkę 'z' można uzyskać więcej niż jednostkę 'z' przez serię
# wymian walut.

def currency_exchange(currencies):
    def relax(currencies, j):
        if cost[currencies[j][1]] < currencies[j][2] * cost[currencies[j][0]]:
            cost[currencies[j][1]] = currencies[j][2] * cost[currencies[j][0]]
            if currencies[j][0] == parent[currencies[j][1]]:
                parent[currencies[j][1]] = currencies[j][0]
                return True
            parent[currencies[j][1]] = currencies[j][0]

        return False

    max_vertex = 0

    for i in range(len(currencies)):
        max_vertex = max(max_vertex, currencies[i][0], currencies[i][1])

    E = len(currencies)
    cost = [0] * (max_vertex + 1)
    parent = [None] * (max_vertex + 1)
    cost[0] = 1

    for i in range(max_vertex - 1):
        for j in range(E):
            if i != 0:
                if relax(currencies, j):
                    return True
            else:
                relax(currencies, j)
    return False


currencies = [(0, 1, 4.5),
              (0, 2, 4),
              (2, 0, 0.25),
              (1, 2, 0.75),
              (3, 2, 100),
              (0, 3, 0.4),
              (1, 4, 6),
              (3, 4, 2)]
print(currency_exchange(currencies))


# Algocja leży na wielkiej pustyni i składa się z miast oraz oaz połączonych drogami. Każde miasto
# jest otoczone murem i ma tylko dwie bramy - północną i południową. Z każdej bramy prowadzi dokładnie
# jedna droga do jednej oazy (ale do danej oazy może dochodzić dowolnie wiele dróg; oazy mogą też być
# połączone drogami między sobą). Prawo Algocji wymaga, że jeśli ktoś wjechał do miasta jedną bramą,
# to musi go opuścić drugą. Szach Algocji postanowił wysłać gońca, który w każdym mieście kraju odczyta
# zakaz formułowania zadań “o szachownicy” (obraza majestatu). Szach chce, żeby goniec odwiedził każde
# miasto dokładnie raz (ale nie ma ograniczeń na to ile razy odwiedzi każdą z oaz). Goniec wyjeżdża ze
# stolicy Algocji, miasta x, i po odwiedzeniu wszystkich miast ma do niej wrócić. Proszę przedstawić
# algorytm, który stwierdza czy odpowiednia trasa gońca istnieje.


def check_and_bishop(graph, oasis):
    changed_graph = []

    for i in range(len(graph)):
        if i not in oasis:
            changed_graph.append([graph[i][0], graph[i][1], 0])
        else:
            for j in range(len(graph[i])):
                if graph[i][j] in oasis:
                    if [graph[i][j], i, 1] not in changed_graph:
                        changed_graph.append([i, graph[i][j], 1])
    count = 0
    vertices = []

    for i in range(len(changed_graph)):
        if changed_graph[i][2] == 1:
            vertices.append((changed_graph[i][0], changed_graph[i][1]))
            count += 1

    for i in range(len(vertices)):
        for j in range(len(changed_graph)):
            if changed_graph[j][0] in vertices[i]:
                changed_graph[j][0] = min(vertices[i])
            if changed_graph[j][1] in vertices[i]:
                changed_graph[j][1] = min(vertices[i])
    i = 0

    while i < len(changed_graph):
        j = i + 1
        while j < len(changed_graph):
            if changed_graph[i][0] == changed_graph[j][0] and changed_graph[i][1] == changed_graph[j][1] and \
                    changed_graph[i][2] == 1:
                changed_graph.remove(changed_graph[i])
            elif changed_graph[i][0] == changed_graph[j][0] and changed_graph[i][1] == changed_graph[j][1] and \
                    changed_graph[j][2] == 1:
                changed_graph.remove(changed_graph[j])
            j += 1
        i += 1

    new_graph = []

    for i in range(len(changed_graph)):
        if changed_graph[i][0] not in new_graph:
            new_graph.append(changed_graph[i][0])
        if changed_graph[i][1] not in new_graph:
            new_graph.append(changed_graph[i][1])

    for i in range(len(new_graph)):
        new_graph[i] = [new_graph[i], 0]

    for i in range(len(new_graph)):
        for j in range(len(changed_graph)):
            if new_graph[i][0] == changed_graph[j][0]:
                new_graph[i][1] += 1
            if new_graph[i][0] == changed_graph[j][1]:
                new_graph[i][1] += 1

    for i in range(len(new_graph)):
        if new_graph[i][1] % 2 == 1:
            return False

    return True


oasis = [2, 4, 5, 7, 9]
graph = [[2, 4], [2, 9], [0, 4, 3], [2, 5], [0, 2, 6], [3, 7, 8], [4, 7], [5, 6, 8], [5, 7], [1]]
print(check_and_bishop(graph, oasis))

# W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć miasta siecią autostrad, tak
# aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na którym leży państwo
# jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii prostej pomiędzy
# miastami liczona w kilometrach wyraża się wzorem len = sqrt((x1-x2)**2 + (y1-y2)**2). Z uwagi na
# oszczędność materiałów autostrada łączy dwa miasta w linii prostej. Ponieważ zbliżają się wybory
# prezydenckie, wszystkie autostrady zaczęto budować równocześnie i jako cel postanowiono zminimalizować
# czas pomiędzy otwarciem pierwszej i ostatniej autostrady. Czas budowy autostrady wyrażony w dniach
# wynosi ceil(len) (sufit z długości autostrady wyrażonej w km). Proszę zaimplementować algorytm
# wyznaczający minimalną liczbę dni dzielącą otwarcie pierwszej i ostatniej autostrady.
from math import inf


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


def kruskal_algorithm(graph, source, vertices):
    V = []

    for i in range(vertices):
        V.append(make_set(i))

    visited = [False for _ in range(vertices)]
    start_day = end_day = 0

    for i in range(source, len(graph)):
        if start_day == 0:
            start_day = graph[i][2]
        u = graph[i][0]
        v = graph[i][1]
        if find(V[u]) != find(V[v]):
            end_day = graph[i][2]
            visited[u] = True
            visited[v] = True
            union(V[u], V[v])

    for i in range(vertices):
        if not visited[i]:
            return inf

    return end_day - start_day


def highway(graph):
    vertices = len(graph)
    edges = convert_to_edges(graph)
    edges.sort(key=lambda x: x[2])
    best_result = inf

    for i in range(vertices):
        result = kruskal_algorithm(edges, i, vertices)
        best_result = min(best_result, result)
    return best_result


graph = [[(1, 2), (2, 5)],
         [(0, 2), (3, 4), (6, 6)],
         [(0, 5), (3, 4), (4, 3)],
         [(1, 4), (2, 4), (5, 1)],
         [(2, 3), (5, 2)],
         [(3, 1), (4, 2), (7, 7)],
         [(1, 6), (7, 1)],
         [(5, 7), (6, 1)]]
print(highway(graph))

# Dana jest mapa kraju w postaci grafu G = (V, E), gdzie wierzchołki to miasta a krawędzie to drogi
# łączące miasta. Dla każdej drogi znana jest jej długość (wyrażona w kilometrach jako liczba naturalna).
# Alicja i Bob prowadzą (na zmianę) autobus z miasta x ∈ V do miasta y ∈ V, zamieniając się za kierownicą
# w każdym kolejnym mieście. Alicja wybiera trasę oraz decyduje, kto prowadzi pierwszy. Proszę zapropnować
# algorytm, który wskazuje taką trasę (oraz osobę, która ma prowadzić pierwsza), żeby Alicja przejechała
# jak najmniej kilometrów.
from math import inf
from queue import PriorityQueue


def shortest_path(graph, start, finish):
    def relax(new_graph, vertex, u, idx, new_idx):
        if new_graph[vertex][idx] > new_graph[u][idx] + dist and idx == 0:
            new_graph[vertex][idx] = new_graph[u][idx] + dist
            new_graph[vertex][new_idx] = new_graph[u][new_idx]
            parent[vertex] = u
            return True
        elif idx == 1:
            new_graph[vertex][idx] = new_graph[u][idx] + dist
            new_graph[vertex][new_idx] = new_graph[u][new_idx]
            parent[vertex] = u
            return True
        return False

    def dijkstra_algorithm(graph, first, start, finish):
        queue = PriorityQueue()
        new_graph[0][0] = 0
        new_graph[0][1] = 0
        visited = [False] * len(graph)
        parent = [None] * len(graph)
        queue.put((0, first, start))

        while not queue.empty():
            distance, idx, u = queue.get()
            for v in graph[u]:
                vertex, dist = v
                if not visited[vertex]:
                    if idx == 0:
                        new_idx = 1
                    else:
                        new_idx = 0
                    if relax(new_graph, vertex, u, idx, new_idx):
                        queue.put((new_graph[vertex][0], new_idx, vertex))
            visited[u] = True

        return new_graph[finish][0], parent

    new_graph = [[inf] * 2 for _ in range(len(graph))]
    result_1, parent_1 = dijkstra_algorithm(graph, 0, start, finish)

    for i in range(len(new_graph)):
        new_graph[i][0], new_graph[i][1] = inf, inf

    result_2, parent_2 = dijkstra_algorithm(graph, 1, start, finish)
    tour = []

    if result_1 < result_2:
        while finish != parent_1[start]:
            tour.append(finish)
            finish = parent_1[finish]
        tour.reverse()
    else:
        while finish != parent_2[start]:
            tour.append(finish)
            finish = parent_2[finish]
        tour.reverse()
    return tour


graph = [[(1, 4), (2, 1), (3, 5)],
         [(0, 1), (4, 2)],
         [(0, 1), (5, 8), (6, 7)],
         [(0, 5), (5, 7)],
         [(1, 2), (7, 10)],
         [(2, 8), (3, 7), (8, 3)],
         [(2, 7), (7, 6)],
         [(4, 10), (6, 6), (9, 11)],
         [(5, 3), (9, 9)],
         [(7, 11), (8, 9)]]

start = 0
finish = len(graph) - 1
print(shortest_path(graph, start, finish))
