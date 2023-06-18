# complete binary tree 완전 이진 트리
class Node:
    def __init__(self, value = 0, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self, value=0):
        self.root = None
        self.value = value
tree = BinaryTree()
tree.root = Node(value='A')
tree.root.left = Node(value = 'B')
tree.root.right = Node(value = 'C')
tree.root.left.left = Node(value = 'D')
tree.root.left.right = Node(value = 'E')
tree.root.right.left = Node(value = 'F')
tree.root.right.right = Node(value = 'G')


from collections import deque
# 코드 구현 기본
def BFS(root):
    visited = [] # 방명록 (<-> 접근)
    q = deque()
    if root is None:
        return []
    q.append(root)
    while q:
        current_node = q.popleft()
        visited.append(current_node.value)
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)
    return visited
BFS(tree.root)