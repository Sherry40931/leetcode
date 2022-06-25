# https://leetcode.com/problems/count-asterisks/
# 2315. Count Asterisks

class Solution:
    def countAsterisks(self, s: str) -> int:
        cnt = 0
        pair = False
        for c in s:
            if c == '|':
                pair = ~pair
            elif c == '*' and not pair:
                cnt += 1

        return cnt


print(Solution().countAsterisks('l|*e*et|c**o|*de|'))
print(Solution().countAsterisks('iamprogrammer'))
print(Solution().countAsterisks('yo|uar|e**|b|e***au|tifu|l'))