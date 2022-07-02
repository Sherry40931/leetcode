# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# 103. Binary Tree Zigzag Level Order Traversal
from typing import List
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
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
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans, level = [], [root]
        turn = 1
        while root and level:
            ans.append([n.val for n in level[::turn]])
            level = [child for node in level for child in (node.left, node.right) if child]
            turn = -turn
        return ans


print(Solution().zigzagLevelOrder(build_tree([3, 9, 20, None, None, 15, 7])))
print(Solution().zigzagLevelOrder(build_tree([1, 2, 3, 4, None, None, 5])))
print(Solution().zigzagLevelOrder(build_tree([1])))
print(Solution().zigzagLevelOrder(build_tree([])))