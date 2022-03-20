# 6028. Count Collisions on a Road
# https://leetcode.com/contest/weekly-contest-285/problems/count-collisions-on-a-road/
from pdb import set_trace as bp


class Solution:
    def countCollisions(self, directions: str) -> int:
        N = len(directions)
        pos = [0] * N
        ans = 0
        string_dict = {'RL': 2, 'RS': 1, 'SL': 1}

        for i, d in enumerate(directions[:-1]):
            string = ''.join(d + directions[i + 1])
            if string in string_dict:
                ans += string_dict[string]
                pos[i] = 1
                pos[i + 1] = 1

        for i in range(N):
            if pos[i] == 1:
                continue
            if directions[i] == 'L' and i - 1 > 0 and pos[i - 1] == 1:
                pos[i] = 1
                ans += 1

        for i in range(N - 1, -1, -1):
            if pos[i] == 1:
                continue
            if directions[i] == 'R' and i + 1 < N and pos[i + 1] == 1:
                pos[i] = 1
                ans += 1

        return ans

# RL, 2
# RS, 1
# SL, 1


class Solution2:
    def countCollisions(self, directions: str) -> int:
        ans = x = y = 0
        for d in directions:
            if d == 'L':
                ans += x  # 如果前面都是 L, x = 0, no collision
            else:
                x = 1  # 只要前面出現 R or S, 就會連環撞, 所以每次 ans += 1

        for d in directions[-1::-1]:  # reverse, same logic below
            if d == 'R':
                ans += y
            else:
                y = 1
        return ans


class Solution3:
    def countCollisions(self, directions: str) -> int:
        # All the cars that move to the middle will eventually collide
        return sum(d != 'S' for d in directions.lstrip('L').rstrip('R'))


print(Solution3().countCollisions('RLRSLL'))
print(Solution3().countCollisions('LLRR'))
print(Solution3().countCollisions('LLSRR'))
print(Solution3().countCollisions('L'))
print(Solution3().countCollisions('R'))
print(Solution3().countCollisions('SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR'))