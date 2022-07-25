# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/
# 2335. Minimum Amount of Time to Fill Cups
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        cnt = 0

        while max(amount) > 0:
            min_idx = amount.index(min(amount))
            for i in range(3):
                if i != min_idx and amount[i] > 0:
                    amount[i] -= 1
            cnt += 1

        return cnt


print(Solution().fillCups([1, 4, 2]))
print(Solution().fillCups([5, 4, 4]))
print(Solution().fillCups([5, 0, 0]))
print(Solution().fillCups([5, 0, 7]))  # 7
print(Solution().fillCups([0, 0, 0]))  # 0
print(Solution().fillCups([0, 2, 2]))  # 2