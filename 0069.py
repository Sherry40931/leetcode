# https://leetcode.com/problems/sqrtx/
# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        # binary search
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif mid ** 2 < x:
                low = mid + 1
            else:
                high = mid
        return mid


print(Solution().mySqrt(0))
print(Solution().mySqrt(1))
print(Solution().mySqrt(4))
print(Solution().mySqrt(8))