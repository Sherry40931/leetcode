# https://leetcode.com/contest/biweekly-contest-111/problems/count-pairs-whose-sum-is-less-than-target/
# 6954. Count Pairs Whose Sum is Less than Target
from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        i = j = cnt = 0
        N = len(nums)
        for i in range(N):
            for j in range(i + 1, N):
                if nums[i] + nums[j] < target:
                    cnt += 1
        return cnt


print(Solution().countPairs([-1, 1, 2, 3, 1], 2))
print(Solution().countPairs([-6, 2, 5, -2, -7, -1, 3], -2))
