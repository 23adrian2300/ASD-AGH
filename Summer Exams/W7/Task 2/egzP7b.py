from egzP7btesty import runtests


def ogrod( S, V ):
    n = len(S)
    m = len(V)
    sol = 0
    for i in range(n):
        S[i] -= 1
    for i in range(n):
        taken = [0 for _ in range(m)] # 0 - not taken, 1 - taken, inf - taken and not returned
        tmp = 0
        for j in range(i, n):
            if taken[S[j]] == 0:
                taken[S[j]] = 1
                tmp += V[S[j]]
            elif taken[S[j]] == 1:
                sol = max(sol, tmp)
                tmp -= V[S[j]]
                taken[S[j]] = float('inf')
            elif taken[S[j]] == float('inf'):
                pass

        sol = max(sol, tmp)
    return sol # 5/10 tests

runtests(ogrod, all_tests = True)