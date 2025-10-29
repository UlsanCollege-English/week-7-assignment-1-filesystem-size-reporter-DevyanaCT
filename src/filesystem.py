class Node:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size
        self.children = children or []


def total_size(node):
    if node is None:
        return 0
    if not node.children:  # file (leaf)
        return node.size
    return node.size + sum(total_size(child) for child in node.children)


def folder_sizes(root):
    if root is None:
        return {}

    result = {}

    def dfs(node):
        if node is None:
            return 0
        if not node.children:  # file
            return node.size
        s = node.size + sum(dfs(child) for child in node.children)
        result[node.name] = s  # only folders recorded
        return s

    dfs(root)
    return result


def level_order(root):
    if root is None:
        return []

    from collections import deque
    q = deque([root])
    levels = []

    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.name)
            for child in node.children:
                q.append(child)
        levels.append(level)

    return levels
