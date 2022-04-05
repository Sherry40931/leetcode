from timer import timing


class Solution2:
    @timing
    def isUgly(self, n: int) -> bool:
        # (2 * 3 * 5)^30
        for _ in range(10000):
            ans = n > 0 and (30 ** 32) % n == 0
        return ans


class Solution:
    @timing
    def isUgly(self, n: int) -> bool:
        for _ in range(10000):
            if n == 0:
                return False
            for p in [2, 3, 5]:
                while n % p == 0:
                    n //= p

        return n == 1


Solution2().isUgly(6)
Solution().isUgly(6)
# print(Solution2().isUgly(1))
# print(Solution2().isUgly(14))