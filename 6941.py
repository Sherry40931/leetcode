# https://leetcode.com/contest/biweekly-contest-111/problems/sorting-three-groups/
# 6941. Sorting Three Groups

from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d1, d2, d3 = 0, 0, 0
        for n in nums:
            d1, d2, d3 = d1, min(d1, d2), min(d1, d2, d3)
            if n == 1:
                d2, d3 = d2+1, d3+1
            elif n == 2:
                d1, d3 = d1+1, d3+1
            else:
                d1, d2 = d1+1, d2+1
            print(d1, d2, d3)
        return min(d1, d2, d3)

print(Solution().minimumOperations([2, 1, 3, 2, 1]))
print(Solution().minimumOperations([1, 3, 2, 1, 3, 3]))
print(Solution().minimumOperations([2, 2, 2, 2, 3, 3]))
print(Solution().minimumOperations([2, 3, 1, 2]))  # 2
print(Solution().minimumOperations([3, 3, 2]))  # 1
print(Solution().minimumOperations([3, 3, 1, 2]))  # 2
print(Solution().minimumOperations([3, 1, 2]))  # 1
print(Solution().minimumOperations([3, 2, 2, 1, 2]))  # 2
