from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N, carry = len(digits), 0
        digits[-1] += 1
        for i in range(N - 1, -1, -1):
            digits[i] += carry
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
        if carry > 0:
            digits.insert(0, 1)
        return digits


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(d) for d in digits]))
        num = str(num + 1)
        return [int(s) for s in num]


print(Solution2().plusOne([1, 2, 3]))
print(Solution2().plusOne([4, 3, 2, 1]))
print(Solution2().plusOne([9]))
print(Solution2().plusOne([9, 8, 9]))