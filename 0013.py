# https://leetcode.com/problems/roman-to-integer/
# 13. Roman to Integer


class Solution:
    def romanToInt(self, s: str) -> int:
        d1 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        d2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i, n = 0, len(s)
        ans = 0
        while i < n:
            if i + 2 <= n and s[i: i + 2] in d1:
                ans += d1[s[i: i + 2]]
                i += 2
            else:
                ans += d2[s[i]]
                i += 1
        return ans


class Solution2:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        s = s.replace('IV', 'IIII').replace('IX', 'VIIII')
        s = s.replace('XL', 'XXXX').replace('XC', 'LXXXX')
        s = s.replace('CD', 'CCCC').replace('CM', 'DCCCC')
        for c in s:
            ans += d[c]
        return ans


print(Solution2().romanToInt('III'))
print(Solution2().romanToInt('LVIII'))
print(Solution2().romanToInt('MCMXCIV'))