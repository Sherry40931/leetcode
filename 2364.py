# https://leetcode.com/problems/count-number-of-bad-pairs/
# 2364. Count Number of Bad Pairs
from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        d = defaultdict(lambda: 0)
        cnt = 0
        for i, v in enumerate(nums):
            num = v - i
            cnt += d[num]
            d[num] += 1

        return n * (n - 1) // 2 - cnt

    def countBadPairs2(self, nums: List[int]) -> int:
        n, ans = len(nums), 0
        for i in range(n):
            for j in range(i + 1, n):
                if j - i != nums[j] - nums[i]:
                    ans += 1
        return ans


print(Solution().countBadPairs([4, 1, 3, 3]))  # 5
print(Solution().countBadPairs([1, 2, 3, 4, 5]))  # 0
print(Solution().countBadPairs([1, 2, 4, 4]))  # 3
print(Solution().countBadPairs([1, 2, 4, 4, 5]))  # 4
print(Solution().countBadPairs([1, 2, 4, 4, 6]))  # 6
print(Solution().countBadPairs([3, 2, 1]))  # 3
print(Solution().countBadPairs([5, 6, 7]))  # 3


# j - i == nums[j] - nums[i]
# nums[i] - i == nums[j] - j