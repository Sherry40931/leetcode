from typing import List
from typing import Optional
from pdb import set_trace as bp


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(nums: List[int]):
    if len(nums) == 0:
        return None

    head = node = ListNode(nums[0])
    for n in nums[1:]:
        node.next = ListNode(n)
        node = node.next
    return head


def print_list(head: Optional[ListNode]):
    node = head
    while node:
        print(node.val, end=', ')
        node = node.next
    print()


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head

        while cur:
            nex = cur.next
            cur.next = pre
            pre, cur = cur, nex

        return pre


class Solution2:
    # don't need cur
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None

        while head:
            nex, head.next = head.next, pre
            pre, head = head, nex

        return pre


print_list(Solution2().reverseList(build_list([1, 2, 3, 4, 5])))
print_list(Solution2().reverseList(build_list([])))
print_list(Solution2().reverseList(build_list([1, 2])))