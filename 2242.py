# 6063. Maximum Score of a Node Sequence
# https://leetcode.com/contest/biweekly-contest-76/problems/maximum-score-of-a-node-sequence/


from collections import defaultdict
from typing import List


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        # get top 4 scores
        for k, v in adj.items():
            adj[k] = sorted(v, key=lambda x: scores[x], reverse=True)[:4]

        ans = -1
        for i, j in edges:
            for i_adj in adj[i]:
                if i_adj == j:
                    continue
                for j_adj in adj[j]:
                    if j_adj != i and j_adj != i_adj:
                        s = scores[i] + scores[j] + scores[i_adj] + scores[j_adj]
                        ans = max(ans, s)
        return ans



print(Solution().maximumScore([5, 2, 9, 8, 4], [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
print(Solution().maximumScore([9, 20, 6, 4, 11, 12], [[0, 3], [5, 3], [2, 4], [1, 3]]))