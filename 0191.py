# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/
from timer import timing


class Solution:
    @timing
    def hammingWeight(self, n: int) -> int:
        return sum([v == '1' for v in bin(n)[2:]])


class Solution2:
    @timing
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans += n & 1
            n >>= 1
        return ans


class Solution3:
    @timing
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


print(Solution().hammingWeight(int('00000000000000000000000000001011', 2)))
print(Solution().hammingWeight(int('00000000000000000000000010000000', 2)))
print(Solution().hammingWeight(int('11111111111111111111111111111101', 2)))
print(Solution3().hammingWeight(int('00000000000000000000000000001011', 2)))
print(Solution3().hammingWeight(int('00000000000000000000000010000000', 2)))
print(Solution3().hammingWeight(int('11111111111111111111111111111101', 2)))