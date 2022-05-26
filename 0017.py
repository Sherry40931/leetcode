# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number
from typing import List
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mapping = {}
        k = 0
        for d in range(2, 10):
            step = 4 if d == 7 or d == 9 else 3
            mapping[str(d)] = ''.join([chr(ord('a') + v) for v in range(k, k + step)])
            k += step

        return [''.join(v) for v in product(*[mapping[d] for d in digits])]


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        return [''.join(v) for v in product(*[mapping[d] for d in digits])]


class Solution3:
    # recursive
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        N = len(digits)

        def dfs(i: int, words: str):
            if i >= N:
                result.append(words)
                return
            for c in mapping[digits[i]]:
                dfs(i + 1, words + c)

        dfs(0, '')
        return result


print(Solution3().letterCombinations('23'))
print(Solution3().letterCombinations(''))
print(Solution3().letterCombinations('2'))