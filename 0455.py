# https://leetcode.com/problems/assign-cookies/
# 455. Assign Cookies
import heapq
from typing import List


class Solution:
    def findContentChildren(self, greeds: List[int], cookies: List[int]) -> int:
        output = 0
        heapq._heapify_max(cookies)
        heapq._heapify_max(greeds)
        while len(cookies) and len(greeds):
            c = heapq._heappop_max(cookies)
            g = heapq._heappop_max(greeds)
            while len(greeds) and c < g:
                g = heapq._heappop_max(greeds)
            if c >= g:
                output += 1
        return output


class Solution2:
    def findContentChildren(self, greeds: List[int], cookies: List[int]) -> int:
        greeds.sort()
        cookies.sort()

        i = j = 0
        N, M = len(greeds), len(cookies)
        while i < N and j < M:
            if greeds[i] <= cookies[j]:
                i += 1
            j += 1
        return i


print(Solution2().findContentChildren([1, 2, 3], [1, 1]))
print(Solution2().findContentChildren([1, 2], [1, 2, 3]))
print(Solution2().findContentChildren([1, 2, 3], []))
print(Solution2().findContentChildren([], [1, 2, 3]))
print(Solution2().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))