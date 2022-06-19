# https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
# 2310. Sum of Numbers With Units Digit K
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0

        for i in range(1, 11):
            if (k * i) % 10 == num % 10 and k * i <= num:
                return i
        return -1


print(Solution().minimumNumbers(58, 9))
print(Solution().minimumNumbers(37, 2))
print(Solution().minimumNumbers(0, 7))
print(Solution().minimumNumbers(10, 8))
print(Solution().minimumNumbers(10, 1))
print(Solution().minimumNumbers(11, 1))