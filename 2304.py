# https://leetcode.com/contest/weekly-contest-297/problems/minimum-path-cost-in-a-grid/
# 5270. Minimum Path Cost in a Grid
from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        agg = [[0 for _ in range(n)] for _ in range(m)]
        agg[-1] = [v for v in grid[-1]]

        for i in range(m - 2, -1, -1):
            for j in range(n):
                c = grid[i][j]
                min_cost = min([v + moveCost[c][i] for i, v in enumerate(agg[i + 1])])
                agg[i][j] = c + min_cost
        return min(agg[0])


print(Solution().minPathCost([[5, 3], [4, 0], [2, 1]], [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]))
print(Solution().minPathCost([[5, 1, 2], [4, 0, 3]],
                             [[12, 10, 15], [20, 23, 8], [21, 7, 1], [8, 1, 13], [9, 10, 25], [5, 3, 2]]))