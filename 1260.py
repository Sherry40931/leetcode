# https://leetcode.com/problems/shift-2d-grid/
# 1260. Shift 2D Grid
from collections import deque
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])
        array = deque([v for row in grid for v in row])
        array.rotate(k)
        for i in range(M):
            for j in range(N):
                grid[i][j] = array[i * N + j]
        return grid


class Solution2:
    '''
    Space Complexity: O(10)
    reverse the whole array
    reverse the first k elements
    reverse the remaing m * n - k element.
    1 2 3 4 5 6
    6 5 4 3 2 1
    4 5 6 1 2 3
    '''

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        M, N = len(grid), len(grid[0])

        def reverse(left: int, right: int) -> None:
            while left < right:
                r, c = left // N, left % N
                i, j = right // N, right % N
                grid[r][c], grid[i][j] = grid[i][j], grid[r][c]  # swap
                left, right = left + 1, right - 1

        S = M * N
        k %= S
        reverse(0, S - 1)
        reverse(0, k - 1)
        reverse(k, S - 1)

        return grid


print(Solution2().shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(Solution2().shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
print(Solution2().shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9))
print(Solution2().shiftGrid([[1], [2], [3], [4], [7], [6], [5]], 23))