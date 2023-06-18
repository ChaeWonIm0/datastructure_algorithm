# 트리 세팅
# 이진 트리 세팅
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
tree.root.right.right = Node(value = 'F')
tree.root.left.left.left = Node(value = 'G')
tree.root.left.left.right = Node(value = 'H')

def dfs(tree_root):
    if tree_root is None:
        return
    dfs(tree_root.left)
    dfs(tree_root.right)
dfs(tree.root)
# root만 전달해도, root가 가리키고 있는 모든 노드에 접근합니다.
# 각 자식 노드도 서브트리로 인식하고 접근