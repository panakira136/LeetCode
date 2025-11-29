# give you a listnode, delete last n node of listnode, and return the head node of listnode.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


class Solution1:
    def remove_nth_from_end(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        Approach 1: Use extra list storage.
        - Traverse the linked list and store each node in an array.
        - Find the (n + 1)-th node from the end and set its `next` pointer to skip the n-th node from the end.
        - Time Complexity: O(N)
        - Space Complexity: O(N)
        """
        node = head
        nodes = []
        while node:
            nodes.append(node)
            node = node.next
        # If the node to remove is the head
        if n == len(nodes):
            return head.next
        # Link the (n + 1)-th node from the end to the (n - 1)-th node
        nodes[-(n + 1)].next = nodes[-n].next
        return head


class Solution2:
    def remove_nth_from_end(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        Approach 2: Two-pointer technique (fast & slow pointers).
        - Initial two pointers: `fast` and `slow`.
        - Move `fast` pointer n steps ahead.
        - Then move both pointer until `fast` reaches the end.
        - At this point, `slow` is positioned right before the node to remove.
        - Adjust `slow.next` to skip the target node.
        - Time Complexity: O(N)
        - Space Complexity: O(1)
        """
        dummy = ListNode(0, head)
        fast = head
        slow = dummy
        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next
        # Move both pointers until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next
        # Remove the target node
        slow.next = slow.next.next
        return dummy.next
