# 6060. Find Closest Number to Zero
# https://leetcode.com/contest/biweekly-contest-76/problems/find-closest-number-to-zero/
from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_pos = min([v for v in nums if v >= 0], default=10 ** 5 + 1)
        max_neg = max([v for v in nums if v < 0], default=-10 ** 5 - 1)
        return min_pos if min_pos <= abs(max_neg) else max_neg


print(Solution().findClosestNumber([-4, -2, 1, 4, 8]))
print(Solution().findClosestNumber([2, -1, 1]))
print(Solution().findClosestNumber([-100000, -100000]))