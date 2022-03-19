# 6022. Minimum Operations to Halve Array Sum
# https://leetcode.com/contest/biweekly-contest-74/problems/minimum-operations-to-halve-array-sum/

from typing import List
from pdb import set_trace as bp
import heapq


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = sum(nums) / 2
        s, op = 0, 0

        nums = [-v for v in nums]
        heapq.heapify(nums)

        while s < half:
            cur_max = heapq.heappop(nums)
            cur_half = cur_max / 2
            heapq.heappush(nums, cur_half)
            s += -cur_half
            op += 1
        return op


print(Solution().halveArray([5, 19, 8, 1]))
print(Solution().halveArray([3, 8, 20]))