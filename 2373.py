# https://leetcode.com/problems/largest-local-values-in-a-matrix/
# 2373. Largest Local Values in a Matrix

from typing import List


def print_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        print(matrix[i])
    print('\n')


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for j in range(n):
            for i in range(n - 2):
                grid[j][i] = max(grid[j][i: i + 3])
        # print_matrix(grid)

        for j in range(n - 2):
            for i in range(n - 2):
                grid[i][j] = max([grid[i + k][j] for k in range(3)])
        # print_matrix(grid)

        return [grid[i][:n - 2] for i in range(n - 2)]


print(Solution().largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(Solution().largestLocal([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))