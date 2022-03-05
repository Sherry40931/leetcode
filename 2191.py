from typing import List


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        new_nums = [self.map_value(v, mapping) for v in nums]
        nums = [x for _, x in sorted(zip(new_nums, nums), key=lambda p: p[0])]
        return nums

    def map_value(self, num: int, mapping: List[int]) -> int:
        num_list = [int(v) for v in str(num)]
        new_num_string = ''.join([str(mapping[v]) for v in num_list])
        return int(new_num_string)


print(Solution().sortJumbled([8, 9, 4, 0, 2, 1, 3, 5, 7, 6], [991, 338, 38]))
print(Solution().sortJumbled([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [789, 456, 123]))