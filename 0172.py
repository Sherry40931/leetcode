# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_2 = cnt_5 = 0
        for i in range(2, n + 1):
            tmp = i
            while tmp % 2 == 0:
                tmp /= 2
                cnt_2 += 1

            tmp = i
            while tmp % 5 == 0:
                tmp /= 5
                cnt_5 += 1
        # print(cnt_2, cnt_5)
        return min(cnt_2, cnt_5)

    def trailingZeroes2(self, n: int) -> int:
        # Since multiple of 2 is more than multiple of 5,
        # the number of zeros is dominant by the number of 5.
        cnt_5 = 0
        for i in range(5, n + 1, 5):
            tmp = i
            while tmp % 5 == 0:
                tmp /= 5
                cnt_5 += 1
        # print(cnt_2, cnt_5)
        return cnt_5

    def trailingZeroes3(self, n: int) -> int:
        # Multiple of 5 provides one 5, multiple of 25 provides two 5 and so on.
        # Note the duplication: multiple of 25 is also multiple of 5,
        # so multiple of 25 only provides one extra 5.
        cnt = 0
        while n > 0:
            n //= 5
            cnt += n
        return cnt


print(Solution().trailingZeroes3(3))
print(Solution().trailingZeroes3(5))
print(Solution().trailingZeroes3(0))
print(Solution().trailingZeroes3(10))