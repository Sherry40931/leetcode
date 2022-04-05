class Solution2:
    def isPowerOfFour(self, n: int) -> bool:
        # bin(1431655765) = '1010101010101010101010101010101'
        return n > 0 and n & (n - 1) == 0 and n & 1431655765 == n


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:  # important! will cause inifinite loop if miss
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1


print(Solution().isPowerOfFour(16))
print(Solution().isPowerOfFour(5))
print(Solution().isPowerOfFour(1))
print(Solution().isPowerOfFour(1431655764))
print(Solution().isPowerOfFour(0))