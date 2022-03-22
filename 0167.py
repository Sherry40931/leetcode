# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while nums[i] + nums[j] != target:
            if nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1
        return i + 1, j + 1


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([2, 7, 11, 15], 22))
print(Solution().twoSum([2, 3, 4], 6))
print(Solution().twoSum([-1, 0], -1))
print(Solution().twoSum([5, 25, 75], 100))