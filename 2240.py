# 6061. Number of Ways to Buy Pens and Pencils
# https://leetcode.com/contest/biweekly-contest-76/problems/number-of-ways-to-buy-pens-and-pencils/
class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        cnt = 0
        for i in range(0, total + 1, cost1):
            cnt += (total - i) // cost2 + 1
        return cnt


print(Solution().waysToBuyPensPencils(20, 10, 5))
print(Solution().waysToBuyPensPencils(5, 10, 10))