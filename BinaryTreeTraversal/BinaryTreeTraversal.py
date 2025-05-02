'''first task'''

class Node:
    '''class for tree'''
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)

# Pre-order traversal
def pre_order(node):
    '''pre order'''
    if not node:
        return []
    order = []
    stack = [node]
    while stack:
        current = stack.pop()
        order.append(current.data)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return order

# In-order traversal
def in_order(node):
    '''in order'''
    if not node:
        return []
    order = []
    stack = []
    current = node
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack:
            current = stack.pop()
            order.append(current.data)
            current = current.right
        else:
            break
    return order

# Post-order traversal
def post_order(node):
    '''post order'''
    if not node:
        return []
    order = []
    stack1 = [node]
    stack2 = []
    while stack1:
        current = stack1.pop()
        stack2.append(current)
        if current.left:
            stack1.append(current.left)
        if current.right:
            stack1.append(current.right)
    while stack2:
        order.append(stack2.pop().data)
    return order
