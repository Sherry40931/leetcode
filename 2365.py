# https://leetcode.com/problems/task-scheduler-ii/
# 2365. Task Scheduler II
from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_task = {}
        now = 0

        for t in tasks:
            if t not in last_task:
                now += 1
            else:
                if now - last_task[t] < space:  # take break
                    now += space - (now - last_task[t]) + 1
                else:  # already satisfied
                    now += 1
            last_task[t] = now
        return now


print(Solution().taskSchedulerII([1, 2, 1, 2, 3, 1], 3))
print(Solution().taskSchedulerII([5, 8, 8, 5], 2))