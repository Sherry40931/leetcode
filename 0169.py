# 169. Majority Element
# https://leetcode.com/problems/majority-element/
from typing import List
from timer import timing

from collections import defaultdict
from collections import Counter


class Solution:
    @timing
    def majorityElement(self, nums: List[int]) -> int:
        # time: O(n), space: O(n/2)
        cnt = defaultdict(lambda: 0)
        half = len(nums) // 2
        for n in nums:
            cnt[n] += 1
            if cnt[n] > half:
                return n
        return max(cnt.values(), key=cnt.keys())

    @timing
    def majorityElement2(self, nums: List[int]) -> int:
        # time: O(n), space: O(n/2)
        counts = Counter(nums)  # return a dict
        return max(counts.keys(), key=counts.get)

    @timing
    def majorityElement3(self, nums: List[int]) -> int:
        # time: O(n), space: O(1)
        # https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
        ans, cnt = nums[0], 0
        for n in nums:
            if cnt == 0:
                ans = n
                cnt += 1
            elif n == ans:
                cnt += 1
            else:
                cnt -= 1
        return ans


print(Solution().majorityElement([3, 2, 3]))
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement([1] * 10 ** 5 + [2] * 10 ** 3))
print(Solution().majorityElement2([3, 2, 3]))
print(Solution().majorityElement2([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement2([1] * 10 ** 5 + [2] * 10 ** 3))
print(Solution().majorityElement3([3, 2, 3]))
print(Solution().majorityElement3([2, 2, 1, 1, 1, 2, 2]))
print(Solution().majorityElement3([1] * 10 ** 5 + [2] * 10 ** 3))