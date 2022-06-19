# https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
# 2309. Greatest English Letter in Upper and Lower Case
from string import ascii_uppercase
from string import ascii_lowercase


class Solution:
    def greatestLetter(self, s: str) -> str:
        sets = set(s)
        for upper, lower in zip(reversed(ascii_uppercase),
                                reversed(ascii_lowercase)):
            if upper in sets and lower in sets:
                return upper
        return ''


print(Solution().greatestLetter('lEeTcOdE'))
print(Solution().greatestLetter('arRAzFif'))
print(Solution().greatestLetter('AbCdEfGhIjK'))
print(Solution().greatestLetter('nzmguNAEtJHkQaWDVSKxRCUivXpGLBcsjeobYPFwTZqrhlyOIfdM'))