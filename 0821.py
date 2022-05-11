# https://leetcode.com/problems/shortest-distance-to-a-character/
# 821. Shortest Distance to a Character
from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        ans = [0] * N

        indices = [i for i in range(N) if s[i] == c]

        M = len(indices)
        k = 0  # index of indices
        for i in range(N):
            if k + 1 < M and abs(i - indices[k + 1]) <= abs(i - indices[k]):
                k += 1
            ans[i] = abs(i - indices[k])
        return ans


class Solution2:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        N = len(s)
        ans = [0] * N
        pos = -N

        # left to right
        for i in range(N):
            if s[i] == c:
                pos = i
            ans[i] = abs(i - pos)

        # right to left
        for i in range(N - 1, -1, -1):
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i], abs(i - pos))
        return ans


print(Solution2().shortestToChar('loveleetcode', 'e'))
print(Solution2().shortestToChar('aaab', 'b'))