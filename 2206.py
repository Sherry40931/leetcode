# 6020. Divide Array Into Equal Pairs
# https://leetcode.com/contest/biweekly-contest-74/problems/divide-array-into-equal-pairs/
from typing import List
from collections import defaultdict


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d = defaultdict(lambda: 0)
        for n in nums:
            d[n] += 1

        for k, v in d.items():
            if v % 2 != 0:
                return False
        return True


print(Solution().divideArray([3, 2, 3, 2, 2, 2]))
print(Solution().divideArray([1, 2, 3, 4, 5]))