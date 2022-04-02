# 2220. Minimum Bit Flips to Convert Number
# https://leetcode.com/problems/minimum-bit-flips-to-convert-number/


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a = bin(start)[2:]
        b = bin(goal)[2:]
        n = max(len(a), len(b))
        a = a.zfill(n)
        b = b.zfill(n)
        return sum([i != j for i, j in zip(a, b)])


print(Solution().minBitFlips(10, 7))
print(Solution().minBitFlips(3, 4))