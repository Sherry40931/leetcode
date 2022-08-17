# https://leetcode.com/problems/node-with-highest-edge-score/
# 2374. Node With Highest Edge Score
from typing import List
from collections import OrderedDict
from collections import defaultdict


class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        score = defaultdict(lambda: 0)
        for source, target, in enumerate(edges):
            score[target] += source

        score = OrderedDict(sorted(score.items(), key=lambda x: (-x[1], x[0])))
        return score.popitem(False)[0]


print(Solution().edgeScore([1, 0, 0, 0, 0, 7, 7, 5]))
print(Solution().edgeScore([2, 0, 0, 2]))