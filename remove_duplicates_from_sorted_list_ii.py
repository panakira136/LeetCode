from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Approach:
        1. Use a dummy node to handle edge cases where head might be removed
        2. Iterate through the list with a current pointer starting at dummy
        3. Compare next two nodes(where available) to detect duplicated
        4. When duplicates found, store the duplicate value and skip all nodes with that value
        5. When no duplicates, move to pointer forward normally
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                x = cur.next.val
                while cur.next and cur.next.val == x:
                    cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next
