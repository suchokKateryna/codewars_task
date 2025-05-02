'''second task'''

from collections import deque

class Node:
    '''node class'''
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    '''tree by levels'''
    if not node:
        return []

    result = []
    queue = deque([node])

    while queue:
        current_node = queue.popleft()
        result.append(current_node.value)
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

    return result
