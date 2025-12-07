# Given the root of a binary search tree, and a integer `k`, return the kth smallest value (1-indexed) of all the
# values of the nodes in the tree.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Perfrom an in-order traversal and stop when we reach the kth smallest element.
        Time Comlexity: O(H+k), where H is the height of the tree.
        Space Comlexity: O(H), due to recursion stack (H is the height of the tree).
        """
        # This variable will store the current kth smallest value found during in-order traversal
        self.k = k
        self.result = None

        # Helper function for in-order traversal
        def in_order(node):
            if not node:
                return
            # Traverse the left subtree first
            in_order(node.left)
            # Process the current node
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            # Traverse the right subtree if we haven't found the kth smallest yet
            in_order(node.right)

        # Start in-order traversal
        in_order(root)
        return self.result
