# https://leetcode.com/contest/biweekly-contest-80/problems/match-substring-after-replacement/
# 6097. Match Substring After Replacement
from typing import List
from collections import defaultdict


class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        d = defaultdict(set)
        for k, v in mappings:
            d[k].add(v)

        m, n = len(s), len(sub)
        for i in range(m - n + 1):
            match = True
            for c1, c2 in zip(s[i: i + n], sub):
                if c1 == c2 or c1 in d[c2]:
                    continue
                match = False
                break
            if match:
                return True
        return False


print(Solution().matchReplacement('fool3e7bar', 'leet', [["e", "3"], ["t", "7"], ["t", "8"]]))
print(Solution().matchReplacement('fooleetbar', 'f00l', [["o", "0"]]))
print(Solution().matchReplacement('Fool33tbaR', 'leetd', [["e", "3"], ["t", "7"], ["t", "8"], ["d", "b"], ["p", "b"]]))