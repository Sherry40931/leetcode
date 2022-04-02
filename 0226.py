# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.insert(data)

    def __str__(self):
        left = self.left.data if self.left else 'None'
        right = self.right.data if self.right else 'None'
        return f'{self.data}, {left}, {right}'


def build_tree(nums: List[int]):
    root = TreeNode(nums[0])
    for i, n in enumerate(nums[1:], start=1):
        root.insert(n)
    return root


def print_tree(root: Optional[TreeNode]):
    q = [root]
    while len(q) > 0:
        node = q.pop(0)
        print(node.data, end=',')
        # print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print()


class Solution:
    # BFS, iterative
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        q = [root]
        while len(q) > 0:
            node = q.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root


class Solution2:
    # BFS, recursive
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root


print_tree(Solution2().invertTree(build_tree([4, 2, 7, 1, 3, 6, 9])))
# [4,7,2,9,6,3,1]
print_tree(Solution2().invertTree(build_tree([2, 1, 3])))