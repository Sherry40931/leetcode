# https://leetcode.com/contest/biweekly-contest-111/problems/make-string-a-subsequence-using-cyclic-increments/
# 8014. Make String a Subsequence Using Cyclic Increments

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = j = 0
        N, M = len(str1), len(str2)
        success = 0

        while i < N and j < M:
            diff = (ord(str2[j]) - ord(str1[i])) % 26
            if diff <= 1:
                i += 1
                j += 1
                success += 1
            else:
                i += 1

        return success == M


print(Solution().canMakeSubsequence('abc', 'ad'))
print(Solution().canMakeSubsequence('zc', 'ad'))
print(Solution().canMakeSubsequence('ab', 'd'))
