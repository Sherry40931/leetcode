# https://leetcode.com/contest/weekly-contest-297/problems/fair-distribution-of-cookies/
# 5289. Fair Distribution of Cookies
from typing import List


class Solution:
    # backtracking: https://haogroot.com/2020/09/21/backtracking-leetcode/
    # discuss: https://leetcode.com/problems/fair-distribution-of-cookies/discuss/2141069/Python-Easy-solution-or-Backtracking-or-Recursion-Branch-and-Bound
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        fair = [0] * k
        n = len(cookies)
        target = sum(cookies) / k

        def backtracking(i):
            nonlocal ans, fair
            # 終止條件
            if i == n:
                ans = min(ans, max(fair))
                return
            # prunning
            if ans <= max(fair) or ans == target:
                return
            # 選擇清單
            for j in range(k):
                fair[j] += cookies[i]  # 做選擇
                backtracking(i + 1)
                fair[j] -= cookies[i]  # 撤銷選擇 for the other choice
        backtracking(0)
        return ans


print(Solution().distributeCookies([8, 15, 10, 20, 8], 2))
print(Solution().distributeCookies([6, 1, 3, 2, 2, 4, 1, 2], 3))
print(Solution().distributeCookies([76265, 7826, 16834, 63341, 68901, 58882, 50651, 75609], 8))