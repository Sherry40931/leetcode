# https://leetcode.com/problems/climbing-stairs/
# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        pre = cur = 1
        for i in range(n - 1):
            pre, cur = cur, pre + cur
        return cur


print(Solution().climbStairs(2))  # 2
# 1, 1
# 2
print(Solution().climbStairs(3))  # 3
# 1, 1, 1
# 2, 1 -> 2
print(Solution().climbStairs(4))  # 5
# 1, 1, 1, 1 -> 1
# 2, 1, 1 -> 3
# 2, 2 -> 1
print(Solution().climbStairs(5))  # 8
# 1, 1, 1, 1, 1 -> 1
# 2, 1, 1, 1 -> 4
# 2, 2, 1 -> 3