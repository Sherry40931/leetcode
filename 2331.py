# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# 2331. Evaluate Boolean Binary Tree
from typing import List
from typing import Optional


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(array: List[int]) -> Optional[TreeNode]:
    if len(array) == 0:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in array]
    n = len(array)
    for i, node in enumerate(nodes):
        if node is None:
            continue
        if i * 2 + 1 < n:
            node.left = nodes[i * 2 + 1]
        if i * 2 + 2 < n:
            node.right = nodes[i * 2 + 2]
    return nodes[0]


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def recursive(node: Optional[TreeNode]):
            if node.val < 2:
                return node.val
            if node.val == 2:
                return recursive(node.left) or recursive(node.right)
            if node.val == 3:
                return recursive(node.left) and recursive(node.right)
        return bool(recursive(root))


print(Solution().evaluateTree(build_tree([2, 1, 3, None, None, 0, 1])))
print(Solution().evaluateTree(build_tree([0])))