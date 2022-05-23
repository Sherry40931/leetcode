# https://leetcode.com/problems/remove-palindromic-subsequences/
# 1332. Remove Palindromic Subsequences
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        i, j = 0, N - 1
        while i < j:
            if s[i] != s[j]:
                return 2
            i, j = i + 1, j - 1
        return 1


class Solution2:
    def removePalindromeSub(self, s: str) -> int:
        if len(s) == 0:
            return 0
        return (s != s[::-1]) + 1


print(Solution2().removePalindromeSub('ababa'))
print(Solution2().removePalindromeSub('abb'))
print(Solution2().removePalindromeSub('baabb'))