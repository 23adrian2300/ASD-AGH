from egzP6atesty import runtests


def sort_buck(bucket):
    def letters(passwd):  # 0(k)
        num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        count = 0
        for i in range(len(passwd)):
            if passwd[i] in num:
                count += 1
        return count

    if len(bucket) > 0:
        n = len(bucket[0])
        bb = []
        for i in range(n + 1):
            bb.append([])
        for i in range(len(bucket)):
            bb[letters(bucket[i])].append(bucket[i])
        new = []
        for i in range(n, -1, -1):
            if len(bb[i]) > 0:
                new = new + bb[i]
        return new
    return []


def google(H, s):
    n = len(H)
    maxi = 0
    for i in range(n):
        maxi = max(maxi, len(H[i]))

    bucket = []

    for i in range(maxi + 1):
        bucket.append([])

    for i in range(n):
        bucket[len(H[i])].append(H[i])

    looking = n - s
    no = 0
    number = 0
    flag = False
    for i in range(maxi + 1):
        if no < looking:
            no += len(bucket[i])
            number = i
        if no == looking:
            number += 1
            flag = True
            break

    index = len(bucket[number]) - (no - looking)

    if flag:
        index = 0

    if len(bucket[number]) == 0:
        while number < maxi + 1 and len(bucket[number]) == 0:
            number += 1

    bucket[number] = sort_buck(bucket[number])
    return bucket[number][index]


runtests(google, all_tests=True)
