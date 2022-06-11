# https://leetcode.com/contest/biweekly-contest-80/problems/strong-password-checker-ii/
# 6095. Strong Password Checker II
import re


class Solution:
    def strongPasswordCheckerII(self, pwd: str) -> bool:
        n = len(pwd)
        if n < 8:
            return False
        if re.search('[a-z]', pwd) is None:
            return False
        if re.search('[A-Z]', pwd) is None:
            return False
        if re.search('[0-9]', pwd) is None:
            return False
        if re.search('[!@#$%^\&*()\-+]', pwd) is None:
            return False
        for i in range(n - 1):
            if pwd[i] == pwd[i + 1]:
                return False
        return True


# print(Solution().strongPasswordCheckerII('IloveLe3tcode!'))
# print(Solution().strongPasswordCheckerII('Me+You--IsMyDream'))
# print(Solution().strongPasswordCheckerII('1aB!'))
# print(Solution().strongPasswordCheckerII('IloveLe3tcodde!'))
print(Solution().strongPasswordCheckerII('-Aa1a1a1'))
print(Solution().strongPasswordCheckerII('&Aa1a1a1'))