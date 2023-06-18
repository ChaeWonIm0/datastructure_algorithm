
from collections import deque


class TreeNode():
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def array2tree(arr):
    q = deque()
    root = TreeNode(arr[0])
    q.append(root)

    idx = 1
    while idx < len(arr):
        cur_node = q.popleft()

        # left Node
        if arr[idx] != None:
            cur_node.left = TreeNode(arr[idx])
            q.append(cur_node.left)
        idx += 1

        # right Node
        if arr[idx] != None:
            cur_node.right = TreeNode(arr[idx])
            q.append(cur_node.right)
        idx += 1
    return root
root = array2tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])

def LCA(root, p, q):
    if root == None:
        return None
    left = LCA(root.left, p, q)
    right = LCA(root.right, q, q)
    if root == p or root == q :
        return root
    elif left and right:
        return root
    elif left:
        return left
    elif right:
        return right

LCA(array2tree([3,5,1,6,2,0,8,None, None, 7,4]), 6, 4)