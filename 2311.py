# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
# 2311. Longest Binary Subsequence Less Than or Equal to K


class Solution:
    # time: O(n)
    # greedy: 保留所有的 0, 從最後開始拿 1 直到大於 k
    def longestSubsequence(self, s: str, k: int) -> int:
        i, n = 0, len(s)
        while i < n and int(s[n - i - 1: n], 2) <= k:
            i += 1

        leading_zeros = sum([1 for c in s[:n - i] if c == '0'])
        return leading_zeros + i


print(Solution().longestSubsequence('1001010', 5))
print(Solution().longestSubsequence('00101001', 1))