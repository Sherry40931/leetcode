# https://leetcode.com/contest/biweekly-contest-80/problems/successful-pairs-of-spells-and-potions/
# 6096. Successful Pairs of Spells and Potions
from typing import List
from bisect import bisect


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        smallest_spells = [0] * len(potions)
        for i, p in enumerate(potions):
            smallest_spells[i] = success / p
        smallest_spells.sort()  # O(nlogn)

        ans = []
        for s in spells:
            ans.append(bisect(smallest_spells, s))
        return ans


print(Solution().successfulPairs([5, 1, 3], [1, 2, 3, 4, 5], 7))
print(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16))