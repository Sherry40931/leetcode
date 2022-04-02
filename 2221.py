# 2221. Find Triangular Sum of an Array
# https://leetcode.com/problems/find-triangular-sum-of-an-array/
from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        N = len(nums)
        new_nums = [nums[0]]
        for n in range(N - 1, 0, -1):
            new_nums = [0] * n
            for i in range(n):
                new_nums[i] = (nums[i] + nums[i + 1]) % 10
            nums = new_nums
            # print(new_nums)
        return new_nums[0]


print(Solution().triangularSum([1, 2, 3, 4, 5]))
print(Solution().triangularSum([5]))