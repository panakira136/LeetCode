from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Perform level-order traversal Breadth First Search (BFS) of a binary tree.
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            current_level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level_values)
        return result
