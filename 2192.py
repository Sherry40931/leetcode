from typing import List
from collections import defaultdict


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        neighbors = defaultdict(set)
        for f, t in edges:
            neighbors[t].add(f)

        ans = []
        for i in range(n):
            ancestors = set()
            Q = neighbors[i].copy()
            while Q:
                j = Q.pop()
                ancestors.add(j)
                ancestors = ancestors.union(neighbors[j])
                Q = Q.union(neighbors[j])
            ans.append(sorted(list(ancestors)))
        return ans


e = [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]
print(Solution().getAncestors(8, e))
e = [[0, 1], [0, 2], [0, 3], [0, 4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(Solution().getAncestors(5, e))
e = [[0, 7], [7, 6], [0, 3], [6, 3], [5, 4], [1, 5], [2, 7], [3, 5], [3, 1], [0, 5], [7, 5], [2, 1], [1, 4], [6, 1]]
print(Solution().getAncestors(8, e))