# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/


from typing import List
from typing import Optional


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
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next

        node = head
        while node:
            next_node = node.next
            while next_node and next_node.val == val:
                next_node = next_node.next

            node.next = next_node
            node = next_node
        return head


class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # https://leetcode.com/problems/remove-linked-list-elements/discuss/158651/Simple-Python-solution-with-explanation-(single-pointer-dummy-head).
        dummy_head = ListNode(0, head)  # in case head.val == val, very smart
        node = dummy_head

        while node.next:
            if node.next.val == val:
                # node 沒有換, node.next 換了
                # 下一個 loop: if node.next.next.val == val
                node.next = node.next.next
            else:
                node = node.next  # node change, go to next node
        return dummy_head.next  # remember this


print_list(Solution2().removeElements(build_list([1, 2, 6, 3, 4, 5, 6]), 6))
print_list(Solution2().removeElements(build_list([]), 1))
print_list(Solution2().removeElements(build_list([7, 7, 7]), 7))