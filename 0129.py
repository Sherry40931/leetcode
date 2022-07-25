# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# 129. Sum Root to Leaf Numbers
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        ans = 0
        queue = [(0, root)]  # cur number, node
        while queue:
            num, node = queue.pop()
            num = num * 10 + node.val
            if node.right:
                queue.append((num, node.right))
            if node.left:
                queue.append((num, node.left))
            if node.right is None and node.left is None:  # leaf
                ans += num
        return ans


print(Solution().sumNumbers(build_tree([1, 2, 3])))
print(Solution().sumNumbers(build_tree([4, 9, 0, 5, 1])))