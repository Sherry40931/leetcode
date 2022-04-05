# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/


from typing import List


def call(nums: List[int]):
    Solution2().moveZeroes(nums)
    print(nums)


class Solution2:
    # Time: O(n) but less operations (?), not really
    # Space: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero = 0
        for i, n in enumerate(nums):
            if n == 0:
                continue
            print(nonzero, i)
            nums[i], nums[nonzero] = 0, n  # the order matters!
            nonzero += 1


class Solution:
    # Time: O(n)
    # Space: O(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonzero = 0
        N = len(nums)
        for i, n in enumerate(nums):
            if n == 0:
                continue
            nums[nonzero] = n
            nonzero += 1

        for i in range(nonzero, N):
            nums[i] = 0


call([0, 1, 0, 3, 12])
call([1])