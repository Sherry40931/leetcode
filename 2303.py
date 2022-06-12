# https://leetcode.com/contest/weekly-contest-297/problems/calculate-amount-paid-in-taxes/
# 5259. Calculate Amount Paid in Taxes
from typing import List


class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = last_upper = 0
        for upper, percent in brackets:
            ans += (min(income, upper) - last_upper) * percent
            last_upper = upper
            if income < upper:
                break
        return ans / 100


print(Solution().calculateTax([[3, 50], [7, 10], [12, 25]], 10))
print(Solution().calculateTax([[3, 50], [7, 10], [12, 25]], 2))
print(Solution().calculateTax([[1, 0], [4, 25], [5, 50]], 2))
print(Solution().calculateTax([[2, 50]], 0))