# https://leetcode.com/problems/check-if-matrix-is-x-matrix/
# 2319. Check if Matrix Is X-Matrix
from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if (i == j or n - i - 1 == j) and grid[i][j] == 0:
                    return False
                elif (i != j and n - i - 1 != j) and grid[i][j] != 0:
                    return False
        return True


print(Solution().checkXMatrix([[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]]))
print(Solution().checkXMatrix([[5, 7, 0], [0, 3, 1], [0, 5, 0]]))