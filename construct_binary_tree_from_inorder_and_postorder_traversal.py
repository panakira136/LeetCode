# Given two integer arrays `inorder` and `postorder` where `inorder` is the inorder traversal of a binary tree and
# `postorder` is the postorder traversal of the same tree, construct and return the binary tree.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def build_tree(
        self, inorder: List[int], postorder: List[int]
    ) -> Optional[TreeNode]:
        """
        Approach:
        - The last element in postorder is the root of the current subtree.
        - Find the root index in inorder; left part = left subtree, right part = right subtree.
        - Recursively build right subtree first, then left subtree (because postorder is Left > Right > Root).
        - Time Complexity: O(N)
        - Space Complexity: O(N)
        """
        if not inorder:
            return
        # Map value -> ite index in inorder traversal for quick lookup
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        def helper(in_left: int, in_right: int) -> Optional[TreeNode]:
            # Base case: no elements to construct the subtree
            if in_left > in_right:
                return
            # Take the last value from postorder as root
            root_value = postorder.pop()
            root = TreeNode(root_value)
            # Root index in inorder traversal
            index = idx_map[root_value]
            # Build right subtree first because of postorder nature (L > R > Root)
            root.right = helper(index + 1, in_right)
            root.left = helper(in_left, index - 1)
            return root

        return helper(0, len(inorder) - 1)
