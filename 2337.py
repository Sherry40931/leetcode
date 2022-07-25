# https://leetcode.com/problems/move-pieces-to-obtain-a-string/
# 2337. Move Pieces to Obtain a String
from collections import deque


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        q = deque()

        for i, c in enumerate(start):
            if c == '_':
                continue
            q.append((i, c))

        for i1, c1 in enumerate(target):
            if c1 == '_':
                continue
            if not q:
                return False
            i2, c2 = q.popleft()  # O(1)
            if c1 != c2 or (c1 == 'R' and i1 < i2) or (c1 == 'L' and i1 > i2):
                return False

        return not q  # not empty


print(Solution().canChange('_L__R__R_', 'L______RR'))
print(Solution().canChange('_R_R_L_', 'R_R___L'))
print(Solution().canChange('_R_R_L_', '_RRL___'))
print(Solution().canChange('R_RL___', 'R_R__L_'))
print(Solution().canChange('R_L_', '__LR'))
print(Solution().canChange('_R', 'R_'))