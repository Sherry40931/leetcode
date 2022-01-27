from typing import List


# brute-force O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] == target:
                    return [i, j]


# dict O(n)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            if n in diff:
                return [i, diff[n]]
            diff[target - n] = i


print(Solution2().twoSum([2, 7, 11, 15], 9))
print(Solution2().twoSum([3, 2, 4], 6))
print(Solution2().twoSum([3, 3], 6))