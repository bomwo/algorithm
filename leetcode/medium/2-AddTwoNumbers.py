# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0)
        count = 0
        while l1 or l2 or count:
            if l1:
                count += l1.val
                l1 = l1.next
            if l2:
                count += l2.val
                l2 = l2.next
            cur.next = ListNode(count % 10)
            cur = cur.next
            count //= 10
        return dummy.next


if __name__ == "__main__":
    solution = Solution()
    solution.addTwoNumbers()