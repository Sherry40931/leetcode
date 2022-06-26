# https://leetcode.com/problems/count-number-of-ways-to-place-houses/
# 2320. Count Number of Ways to Place Houses
from functools import lru_cache


class Solution:
    # time: O(n), fibo sequence
    def countHousePlacements(self, n: int) -> int:
        ans = 0
        prev1 = prev2 = 1
        for i in range(n):
            ans = prev1 + prev2
            prev1, prev2 = prev2, ans
        return (ans ** 2) % (10 ** 9 + 7)


class Solution2:
    def countHousePlacements(self, n: int) -> int:
        @lru_cache(None)  # key
        def helper(i: int, k: int) -> int:
            # i: index of the house
            # k: state of last house, 1 = house, 0 = space
            if i >= n:
                return 1  # cnt
            if k == 0:  # adj is space
                # 可以放 house or spacce
                return helper(i + 1, 1) + helper(i + 1, 0)
            return helper(i + 1, 0)
        ans = helper(1, 0) + helper(1, 1)
        return (ans * ans) % (10 ** 9 + 7)


print(Solution2().countHousePlacements(1))
print(Solution2().countHousePlacements(2))
print(Solution2().countHousePlacements(3))
print(Solution2().countHousePlacements(4))
print(Solution().countHousePlacements(1000))