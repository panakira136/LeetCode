from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        """
        Deep first search recursive solution
        Time Complexity: O(N) where N is number of nodes
        Space Complexity: O(H) where H is tree height
        """

        def dfs(node: Optional[TreeNode], current_sum: int) -> int:
            if node is None:
                return 0
            current_sum = current_sum * 10 + node.val
            if (node.left or node.right) is None:
                return current_sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)
