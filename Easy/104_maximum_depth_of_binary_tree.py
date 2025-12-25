"""
LeetCode #104 - Maximum Depth of Binary Tree
Difficulty: Easy
Company: Google

Problem:
Given the root of a binary tree, return its maximum depth.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Time Complexity: O(n)
Space Complexity: O(h) where h is height
"""

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursive DFS approach
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return max(left_depth, right_depth) + 1
    
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS approach using queue
        """
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    assert solution.maxDepth(root) == 3
    
    # Test case 2: [1,null,2]
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    assert solution.maxDepth(root2) == 2
    
    print("All test cases passed!")
