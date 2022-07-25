# 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i, n in enumerate(nums):
            if n in d and i - d[n] <= k:  # i must > d[n]
                return True
            d[n] = i
        return False


print(Solution().containsNearbyDuplicate([1, 2, 3, 1], 3))
print(Solution().containsNearbyDuplicate([1, 0, 1, 1], 1))
print(Solution().containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2))