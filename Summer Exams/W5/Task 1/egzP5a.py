from egzP5atesty import runtests


def inwestor(T):
    n = len(T)
    solution = 0
    stack = []
    for i in range(n):
        while stack and T[i] <= T[stack[-1]]:
            buying = T[stack.pop()]
            if not stack:
                farms = i
            else:
                farms = i - stack[-1] - 1
            solution = max(solution, buying * farms)
        stack.append(i)
    while stack:
        buying = T[stack.pop()]
        if not stack:
            farms = n
        else:
            farms = n - stack[-1] - 1
        solution = max(solution, buying * farms)

    return solution


runtests(inwestor, all_tests=True)
