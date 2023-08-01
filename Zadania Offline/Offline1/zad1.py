# Adrian Żerebiec
# Opis algorytmu: do rozwiązania problemu wykorzystujemy selected sorta. Przesuwamy wskaźnik r w pętli while, lecz z ograniczeniem do licz=k, bo wiemy że wartość której szukamy dalej niż k pozycji od poprawnego miejsca nie będzie. Następnie podmieniamy odpowiednie wartości i przesuwamy wskaźnik tmp z pierwszej pętli while o jedno miejsce. Pow wykonaiu pierwszego while'a zwracamy wskaźnik p.
# Złożonośc: n*k   k = 0(1) -> 0(n), k = 0(logn) -> O(nlogn), k = 0(n) -> O(n^2)

from zad1testy import Node, runtests


def SortH(p, k):
    tmp = p
    while tmp is not None:
        mini = tmp
        r = tmp.next
        licz = k
        while r is not None and licz != 0:
            if mini.val > r.val:
                mini = r
            r = r.next
            licz -= 1
        x = tmp.val
        tmp.val = mini.val
        mini.val = x
        tmp = tmp.next
    return p


runtests(SortH)
