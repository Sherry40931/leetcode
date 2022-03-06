# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/

from typing import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left, right = [], []
        self.get_tree(root.left, left, 'left')
        self.get_tree(root.right, right, 'right')
        return left == right

    def get_tree(self, node: Optional[TreeNode], vals: List[int], direction: str):
        if node is None:
            vals.append(None)
            return
        vals.append(node.val)
        if direction == 'left':
            self.get_tree(node.left, vals, 'left')
            self.get_tree(node.right, vals, 'left')
        elif direction == 'right':
            self.get_tree(node.right, vals, 'right')
            self.get_tree(node.left, vals, 'right')


class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid(root.left, root.right)

    def is_valid(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left and right:
            a = (left.val == right.val)
            b = self.is_valid(left.right, right.left)
            c = self.is_valid(left.left, right.right)
            return a & b & c
        return left is None and right is None


def build_tree(array: List[int]) -> TreeNode:
    nodes = [TreeNode(a) for a in array]
    N = len(nodes)
    for i, node in enumerate(nodes):
        if i * 2 + 1 < N:
            node.left = nodes[i * 2 + 1]
        if i * 2 + 2 < N:
            node.right = nodes[i * 2 + 2]
    return nodes[0]


def print_tree(root: Optional[TreeNode]):
    Q = [root]
    while Q:
        node = Q.pop(0)
        if node is None:
            continue
        print(node.val)
        Q.append(node.left)
        Q.append(node.right)


print(Solution().isSymmetric(build_tree([1, 2, 2, 3, 4, 4, 3])))
print(Solution().isSymmetric(build_tree([1, 2, 2, None, 3, None, 3])))