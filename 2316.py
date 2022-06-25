# https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/
# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph
from typing import List
from collections import defaultdict


class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        neigh = defaultdict(list)
        for n1, n2 in edges:
            neigh[n1].append(n2)
            neigh[n2].append(n1)

        visited = set()

        def dfs(node, visited):
            if node in visited:
                return 0
            visited.add(node)
            cnt = 1
            for n in neigh[node]:
                cnt += dfs(n, visited)
            return cnt

        ans = n * (n - 1) // 2
        for i in range(n):
            if i in visited:
                continue
            m = dfs(i, visited)
            ans -= m * (m - 1) // 2

        return ans


# 6 + 5 + 4 + 3 + 2 + 1
# (6 + 1) * 6 / 2 = 21
# 21 - 7 = 14

print(Solution().countPairs(3, [[0, 1], [0, 2], [1, 2]]))
print(Solution().countPairs(7, [[0, 2], [0, 5], [2, 4], [1, 6], [5, 4]]))
print(Solution().countPairs(5, [[1, 0], [3, 1], [0, 4], [2, 1]]))
print(Solution().countPairs(
    11, [[5, 0], [1, 0], [10, 7], [9, 8], [7, 2], [1, 3], [0, 2], [8, 5], [4, 6], [4, 2]]))