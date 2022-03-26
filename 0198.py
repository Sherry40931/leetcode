# 198. House Robber
# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    # time: O(n)
    # space: O(n)
    def rob(self, nums: List[int]) -> int:
        money = [0] * (len(nums) + 1)

        for i, n in enumerate(nums[1:], start=2):
            # recursive relation
            # choice: rob ith house or don't rob
            # if rob: award = ith price + (i-2)th price
            # if not rob: award = (i-1)th price
            money[i] = max(money[i - 1], money[i - 2] + n)
        return money[-1]


class Solution2:
    # time: O(n)
    # space: O(1)
    def rob(self, nums: List[int]) -> int:
        prev = curr = 0
        for n in nums:
            # prev: nums[i-2]
            # curr: nums[i-1]
            prev, curr = curr, max(curr, prev + n)
            # prev: nums[i-1]
            # curr: nums[i]
        return curr


print(Solution2().rob([1, 2, 3, 1]))
print(Solution2().rob([2, 7, 9, 3, 1]))