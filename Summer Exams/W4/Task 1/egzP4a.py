from egzP4atesty import runtests


def ceilindex(A, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r


def lis(T):
    n = len(T)
    S = []

    S.append(T[0])
    for i in range(1, n):
        if T[i] >= S[len(S) - 1]:
            S.append(T[i])
        else:
            S[ceilindex(S, -1, len(S) - 1, T[i])] = T[i]

    return len(S)


def mosty(T):
    T.sort(key=lambda x: (x[0], x[1]))
    t2 = []
    for i in range(len(T)):
        t2.append(T[i][1])
    return lis(t2)


runtests(mosty, all_tests=True)
