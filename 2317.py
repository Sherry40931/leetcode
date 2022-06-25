# https://leetcode.com/problems/maximum-xor-after-operations/
# 2317. Maximum XOR After Operations
from typing import List


class Solution:
    '''
    nums[i] AND (nums[i] XOR x) = 拿掉 nums[i] 任意一個 1
    因為 nums[i] & (某值) 最大也是 nums[i]
    所以 maximum possible bitwise XOR of all elements of nums =
    or of all elements
    '''
    def maximumXOR(self, nums: List[int]) -> int:
        ans = nums[0]
        for n in nums[1:]:
            ans |= n
        return ans


print(Solution().maximumXOR([3, 2, 4, 6]))
print(Solution().maximumXOR([1, 2, 3, 9, 2]))

# 8 4 2 1
# 0 1 1 0 6
# 0 0 1 1 3
# 0 0 1 0 2
# 0 1 0 0 4
# 0 0 1 0 2