from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last_idx, n = 0, len(nums)
        for i in range(n):
            if nums[last_idx] != nums[i]:
                nums[last_idx + 1] = nums[i]
                last_idx += 1
        return last_idx + 1