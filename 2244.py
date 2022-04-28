# 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
from collections import defaultdict
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d = defaultdict(lambda: 0)
        for t in tasks:
            d[t] += 1

        ans = 0
        for v in d.values():
            if v < 2:
                return -1
            if v % 3 == 0:
                ans += v // 3
            elif v % 3 == 1:
                cnt_3 = (v // 3) - 1
                cnt_2 = (v - 3 * cnt_3) // 2
                ans += cnt_2 + cnt_3
            else:
                ans += v // 3 + 1
        return ans


class Solution2:
    '''
    If freq = 1, not possible, return -1
    If freq = 2, needs one 2-tasks
    If freq = 3, needs one 3-tasks
    If freq = 3k, freq = 3 * k, needs k batchs.
    If freq = 3k + 1, freq = 3 * (k - 1) + 2 + 2, needs k + 1 batchs.
    If freq = 3k + 2, freq = 3 * k + 2, needs k + 1 batchs.
    To summarize, needs (freq + 2) / 3 batch
    '''
    def minimumRounds(self, tasks: List[int]) -> int:
        d = defaultdict(lambda: 0)
        for t in tasks:
            d[t] += 1

        if 1 in d.values():
            ans = -1
        else:
            ans = sum([(v + 2) // 3 for v in d.values()])
        return ans


print(Solution2().minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
print(Solution2().minimumRounds([2, 3, 3]))
print(Solution2().minimumRounds([3, 3, 3, 3]))
print(Solution2().minimumRounds([3, 3, 3, 3, 3]))
print(Solution2().minimumRounds([3, 3, 3, 3, 3, 3]))


# 4 = 2 + 2
# 5 = 3 + 2
# 6 = 3 + 3
# 7 = 3 + 2 + 2
# 8 = 3 + 3 + 2
# 9 = 3 + 3 + 3