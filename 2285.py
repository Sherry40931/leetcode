# 2285. Maximum Total Importance of Roads
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = [0] * n
        for x, y in roads:
            cnt[x] += 1
            cnt[y] += 1

        sorted_nodes = sorted(range(n), key=lambda k: cnt[k])
        node_values = [0] * n
        for value, idx in enumerate(sorted_nodes):
            node_values[idx] = value + 1

        s = 0
        for x, y in roads:
            s += node_values[x] + node_values[y]

        return s


print(Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
print(Solution().maximumImportance(5, [[0, 3], [2, 4], [1, 3]]))