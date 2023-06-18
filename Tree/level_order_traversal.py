# 해결방식
from collections import deque
def maxDepth(self, root):
    q = deque()
    max_depth=0
    if root is None:
        return max_depth
    depth = 1
    q.append((root, depth))
    while q:
        node, depth = q.popleft()
        max_depth = max(max_depth, depth)
        if node.left:
            q.append((node.left, depth+1))
        if node.right:
            q.append((node.right, depth+1))
    return max_depth
root = [3,9,20,None,None,15,7]

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

root = TreeNode(value = 3)
root.left = TreeNode(value=9)
root.right = TreeNode(value=20)
root.right.left = TreeNode(value=15)
root.right.right = TreeNode(value=7)

print(maxDepth(maxDepth, root= root))