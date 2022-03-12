# 136. Single Number
from typing import List


class Solution:
    '''
    XOR
    a | b | a ^ b
    --|---|------
    0 | 0 | 0
    0 | 1 | 1
    1 | 0 | 1
    1 | 1 | 0

    1 ^ 1 == 0 because the same numbers have same bits.
    0^single_number = single_number.
    Time: O(n)
    Space: O(1)
    '''
    def singleNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for n in nums[1:]:
            ans ^= n
            print(ans)
        return ans


print(Solution().singleNumber([2, 2, 1]))
print('==')
print(Solution().singleNumber([4, 1, 2, 1, 2]))