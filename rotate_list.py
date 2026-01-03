from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        # 1. Handle Edge Cases
        if not head or not head.next or k == 0:
            return head
        # 2. Calculate Length $ Form a Ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        # Connect old tail to head to make it a circle
        old_tail.next = head
        # 3. Calculate Effective Rotation
        k = k % n
        steps_to_new_tail = n - 1 - k
        # 4. Find the New Tail and Break the Ring
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head
