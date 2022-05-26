# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# 19. Remove Nth Node From End of List
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


def print_list(node: ListNode):
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    print(ans)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = j = dummy = ListNode(-1, head)
        n += 1
        while i:
            if n > 0:
                n -= 1
            else:
                j = j.next
            i = i.next

        j.next = j.next.next
        return dummy.next


print_list(Solution().removeNthFromEnd(create_list([1, 2, 3, 4, 5]), 1))
print_list(Solution().removeNthFromEnd(create_list([1, 2, 3, 4, 5]), 2))
print_list(Solution().removeNthFromEnd(create_list([1, 2, 3, 4, 5]), 3))
print_list(Solution().removeNthFromEnd(create_list([1]), 1))
print_list(Solution().removeNthFromEnd(create_list([1, 2]), 1))
print_list(Solution().removeNthFromEnd(create_list([1, 2]), 2))