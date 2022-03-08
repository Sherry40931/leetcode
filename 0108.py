# 108. Convert Sorted Array to Binary Search Tree
# DFS, BST
# Time: O(n)
# Space: O(log N) -> amount of stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums: List[int], start: int, end: int):
        if start > end:
            return None
        mid = (start + end) // 2
        return TreeNode(nums[mid],
                        self.helper(nums, start, mid - 1),  # mid already used in root
                        self.helper(nums, mid + 1, end))  # mid already used in root


# slicing the array is expensive.
# It is better to pass the left and right bounds into recursive calls instead.
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35224/Python-optimal-solution
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def helper(start: int, end: int):
            if start > end:
                return None
            mid = (start + end) // 2
            return TreeNode(nums[mid], helper(start, mid - 1), helper(mid + 1, end))
        return helper(0, len(nums) - 1)