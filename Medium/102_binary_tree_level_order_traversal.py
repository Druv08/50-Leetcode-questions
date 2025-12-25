"""
LeetCode #102 - Binary Tree Level Order Traversal
Difficulty: Medium
Company: Meta, Amazon

Problem:
Given the root of a binary tree, return the level order traversal of its nodes' values.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        BFS using queue
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]
    
    print("All test cases passed!")
