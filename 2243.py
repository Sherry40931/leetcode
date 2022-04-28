# 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/


class Solution:
    def digitSum(self, array: str, k: int) -> str:
        while len(array) > k:
            array = [sum([int(v) for v in array[i:i + k]])
                     for i in range(0, len(array), k)]
            array = ''.join([str(v) for v in array])
        return array


print(Solution().digitSum('01234567890', 2))
print(Solution().digitSum('11111222223', 3))
print(Solution().digitSum('00000000', 3))