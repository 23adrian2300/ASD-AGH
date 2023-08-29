from egzP6btesty import runtests


def jump(M):
    dict = {'UL': (-1, 2), 'RD': (2, -1), 'LU': (-2, 1), 'LD': (-2, -1), 'UR': (1, 2), 'RU': (2, 1), 'DL': (-1, -2),
            'DR': (1, -2)}

    lights = {(0, 0): True}
    start = [0, 0]

    for i in range(len(M)):
        start[0] += dict[M[i]][0]
        start[1] += dict[M[i]][1]
        if (start[0], start[1]) in lights:
            if lights[(start[0], start[1])]:
                lights[(start[0], start[1])] = False
            else:
                lights[(start[0], start[1])] = True
        else:
            lights[(start[0], start[1])] = True

    count = 0
    start = [0,0]

    if (start[0], start[1]) in lights:
        if lights[(start[0], start[1])]:
            count += 1
            lights[(start[0], start[1])] = False

    for i in range(len(M)):
        start[0] += dict[M[i]][0]
        start[1] += dict[M[i]][1]
        if (start[0], start[1]) in lights:
            if lights[(start[0], start[1])]:
                count += 1
                lights[(start[0], start[1])] = False

    return count


runtests(jump, all_tests=True)
