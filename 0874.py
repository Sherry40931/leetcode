# https://leetcode.com/problems/walking-robot-simulation/
# 874. Walking Robot Simulation
from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = {(x, y) for x, y in obstacles}  # set of tuples

        x = y = max_d = 0
        move = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # N, W, S, E
        d = 0  # direction

        for c in commands:
            if c == -2:
                d = (d - 1) % 4
            elif c == -1:
                d = (d + 1) % 4
            else:
                # move one step and check if has obstacles
                i, j = move[d]
                for _ in range(c):
                    if (x + i, y + j) in obstacles:
                        break
                    x, y = x + i, y + j
            max_d = max(max_d, x ** 2 + y ** 2)
        return max_d


print(Solution().robotSim([4, -1, 3], []))
print(Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]]))
print(Solution().robotSim([6, -1, -1, 6], []))
print(Solution().robotSim(
    [-2, -1, 8, 9, 6],
    [[-1, 3], [0, 1], [-1, 5], [-2, -4], [5, 4], [-2, -3], [5, -1], [1, -1], [5, 5], [5, 2]]))
# 0, 1
