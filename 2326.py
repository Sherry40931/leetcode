# https://leetcode.com/problems/spiral-matrix-iv/
# 2326. Spiral Matrix IV
from typing import List
from typing import Optional


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(array: List[int]) -> ListNode:
    nodes = [ListNode(v) for v in array]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    return nodes[0]


def print_matrix(matrix: List[List[int]]):
    m, n = len(matrix), len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=', ')
        print('')
    print('==')


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        direction = {'r': (0, 1), 'd': (1, 0), 'l': (0, -1), 'u': (-1, 0)}
        nex = {'r': 'd', 'd': 'l', 'l': 'u', 'u': 'r'}
        pre = {v: k for k, v in nex.items()}
        bound = {'r': n, 'd': m, 'l': 0, 'u': 0}
        cur = 'r'
        matrix = [[-1] * n for _ in range(m)]
        i = j = 0

        while head:
            matrix[i][j] = head.val
            dir_x, dir_y = direction[cur][0], direction[cur][1]
            if i + dir_x >= bound['d'] or j + dir_y >= bound['r'] or \
               i + dir_x < bound['u'] or j + dir_y < bound['l']:
                bound[pre[cur]] -= sum(direction[pre[cur]])
                cur = nex[cur]
            i += direction[cur][0]
            j += direction[cur][1]
            head = head.next

        return matrix


class Solution2:
    # https://leetcode.com/problems/spiral-matrix-iv/discuss/2229918/Python-Easy-to-Understand
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        x = y = 0
        dx, dy = 0, 1

        while head:
            matrix[x][y] = head.val
            if x + dx < 0 or x + dx >= m or \
               y + dy < 0 or y + dy >= n or \
               matrix[x + dx][y + dy] != -1:  # already used
                dx, dy = dy, -dx  # good trick of clock-wise turn
            x, y = x + dx, y + dy
            head = head.next
        return matrix


print(Solution2().spiralMatrix(3, 5, create_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0])))
print(Solution2().spiralMatrix(3, 5, create_list([3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0, 1, 2])))
print(Solution2().spiralMatrix(1, 4, create_list([0, 1, 2])))