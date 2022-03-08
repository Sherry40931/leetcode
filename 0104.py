# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# DFS

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root, 0)

    def helper(self, node: Optional[TreeNode], depth: int):
        if node is None:
            return depth
        return max(self.helper(node.left, depth + 1),
                   self.helper(node.right, depth + 1))


class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)

    def helper(self, node: Optional[TreeNode]):
        if node is None:
            return 0
        return max(self.helper(node.left) + 1, self.helper(node.right) + 1)