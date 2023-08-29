from egzP3atesty import runtests
from math import inf


class Node:
    def __init__(self, wyborcy, koszt, fundusze):
        self.next = None
        self.wyborcy = wyborcy
        self.koszt = koszt
        self.fundusze = fundusze
        self.x = None


def decyzje(W, P, B):
    n = len(W)
    F = [[0 for b in range(B + 1)] for i in range(n)]
    for b in range(W[0], B + 1):
        F[0][b] = P[0]
    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])
    return F[n - 1][B]


def wybory(T):
    maxi = 0
    for i in range(len(T)):
        P = []
        W = []
        B = 0
        while T[i] is not None:
            P.append(T[i].wyborcy)
            W.append(T[i].koszt)
            B = T[i].fundusze
            T[i] = T[i].next
        maxi += decyzje(W, P, B)
    # tutaj proszę wpisać własną implementację
    return maxi


runtests(wybory, all_tests=True)
