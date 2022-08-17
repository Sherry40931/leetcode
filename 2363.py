# https://leetcode.com/problems/merge-similar-items/
# 2363. Merge Similar Items
from typing import List
from collections import defaultdict


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        d = defaultdict(lambda: 0)
        for v, w in items1 + items2:
            d[v] += w

        return sorted([[k, v] for k, v in d.items()])


print(Solution().mergeSimilarItems([[1, 1], [4, 5], [3, 8]], [[3, 1], [1, 5]]))
print(Solution().mergeSimilarItems([[1, 1], [3, 2], [2, 3]], [[2, 1], [3, 2], [1, 3]]))
print(Solution().mergeSimilarItems([[1, 3], [2, 2]], [[7, 1], [2, 2], [1, 4]]))