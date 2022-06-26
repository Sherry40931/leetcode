# https://leetcode.com/problems/maximum-score-of-spliced-array/
# 2321. Maximum Score Of Spliced Array
from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        ans = max(s1, s2)
        diff1 = diff2 = 0
        max_diff1 = max_diff2 = 0

        for n1, n2 in zip(nums1, nums2):
            diff1 = max(0, diff1 + n2 - n1)  # add to s1
            diff2 = max(0, diff2 + n1 - n2)  # add to s2
            max_diff1 = max(max_diff1, diff1)
            max_diff2 = max(max_diff2, diff2)

        return max(ans, s1 + max_diff1, s2 + max_diff2)


print(Solution().maximumsSplicedArray([60, 60, 60], [10, 90, 10]))
print(Solution().maximumsSplicedArray([20, 40, 20, 70, 30], [50, 20, 50, 40, 20]))
print(Solution().maximumsSplicedArray([7, 11, 13], [1, 1, 1]))