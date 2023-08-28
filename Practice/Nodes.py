class BST_node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


def find(root, key):
    while root is not None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def maximum(root):
    while root.right is not None:
        root = root.right
    return root.key


def minimum(root):
    while root.left is not None:
        root = root.left
    return root.key


def predecessor(root, actual_root_value):
    actual_root = find(root, actual_root_value)
    value = actual_root.key
    if actual_root.left is not None:
        return maximum(actual_root.left)
    while actual_root.parent is not None and actual_root.parent.key > actual_root.key:
        actual_root = actual_root.parent
    if actual_root.parent is not None:
        if actual_root.parent.key > value:
            return None
        return actual_root.parent.key
    if actual_root.key > value:
        return None


def successor(root, actual_root_value):
    actual_root = find(root, actual_root_value)
    value = actual_root.key
    if actual_root.right is not None:
        return minimum(actual_root.right)
    while actual_root.parent is not None and actual_root.parent.key < actual_root.key:
        actual_root = actual_root.parent
    if actual_root.parent is not None:
        if actual_root.parent.key < value:
            return None
        return actual_root.parent.key
    if actual_root.key < value:
        return None


def insert(root, key):
    previous = None
    while root is not None:
        if root.key > key:
            previous = root
            root = root.left
        else:
            previous = root
            root = root.right
    if key < previous.key:
        previous.left = BST_node(key)
        previous.left.parent = previous
    else:
        previous.right = BST_node(key)
        previous.right.parent = previous


def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root

    elif (key > root.key):
        root.right = deleteNode(root.right, key)
        return root


    if root.left is None and root.right is None:
        return None


    if root.left is None:
        temp = root.right
        root = None
        return temp

    elif root.right is None:
        temp = root.left
        root = None
        return temp


    succParent = root


    succ = root.right

    while succ.left != None:
        succParent = succ
        succ = succ.left

    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right

    root.key = succ.key

    return root
