from typing import List
from collections import defaultdict


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        cnt = defaultdict(lambda: 0)
        max_cnt, ans = 0, 0
        for i, n in enumerate(nums[:-1]):
            if n != key:
                continue
            target = nums[i + 1]
            cnt[target] += 1
            if cnt[target] > max_cnt:
                max_cnt = cnt[target]
                ans = target
        return ans


print(Solution().mostFrequent([1, 100, 200, 1, 100], 1))
print(Solution().mostFrequent([2, 2, 2, 2, 3], 2))