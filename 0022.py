# https://leetcode.com/problems/generate-parentheses/
# 22. Generate Parentheses
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(string: str, left: int, right: int):
            print(string)
            if right == 0:
                ans.append(string)
                return
            if left > 0:
                backtracking(string + '(', left - 1, right)
            if right > left:
                backtracking(string + ')', left, right - 1)
        backtracking('(', n - 1, n)
        return ans


print(Solution().generateParenthesis(3))
print(Solution().generateParenthesis(1))