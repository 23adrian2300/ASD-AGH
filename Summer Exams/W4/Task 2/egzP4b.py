from egzP4btesty import runtests


def succerssor(root):
    if root.right:
        curr = root.right
        while curr:
            if not curr.left:
                break
            curr = curr.left
        return curr
    proot = root.parent
    while proot:
        if root != proot.right:
            break
        root = proot
        proot = proot.parent
    return proot


def predecessor(root):
    if root.left:
        curr = root.left
        while curr:
            if not curr.right:
                break
            curr = curr.right
        return curr
    proot = root.parent
    while proot:
        if root != proot.left:
            break
        root = proot
        proot = proot.parent
    return proot


def is_beauty(x, a, b):
    if a is not None and b is not None and a.key + b.key == 2 * x.key:
        return x.key
    else:
        return 0


def averagesum(root, T):
    sol = 0
    for x in T:
        a = predecessor(x)
        b = succerssor(x)
        sol += is_beauty(x, a, b)
    return sol


runtests(averagesum, all_tests=True)
