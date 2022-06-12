# https://leetcode.com/contest/weekly-contest-297/problems/naming-a-company/
# 6094. Naming a Company
from typing import List
from collections import defaultdict


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        d = defaultdict(set)
        for w in ideas:
            d[ord(w[0]) - ord('a')].add(w[1:])

        cnt = 0
        keys = list(d.keys())
        for i, k1 in enumerate(keys):
            for k2 in keys[i + 1:]:
                intersect = len(d[k1] & d[k2])
                cnt += (len(d[k1]) - intersect) * (len(d[k2]) - intersect)
        return cnt * 2


# print(Solution().distinctNames(["coffee", "donuts", "time", "toffee"]))
# print(Solution().distinctNames(["lack", "back"]))
print(Solution().distinctNames(["aaa", "baa", "caa", "bbb", "cbb", "dbb"]))