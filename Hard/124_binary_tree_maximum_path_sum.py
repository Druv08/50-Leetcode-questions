"""
LeetCode #124 - Binary Tree Maximum Path Sum
Difficulty: Hard
Company: Amazon

Problem:
Find the maximum path sum of any non-empty path in a binary tree.

Example:
Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with sum 6.

Time Complexity: O(n)
Space Complexity: O(h) where h is tree height
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        DFS with global maximum tracking
        """
        self.max_sum = float('-inf')
        
        def max_gain(node):
            """Returns max path sum starting from node"""
            if not node:
                return 0
            
            # Recursively get max gain from left and right
            left_gain = max(max_gain(node.left), 0)  # Ignore negative paths
            right_gain = max(max_gain(node.right), 0)
            
            # Current path sum including node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return max gain if continuing path through this node
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,2,3]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert solution.maxPathSum(root) == 6
    
    # Test case 2: [-10,9,20,null,null,15,7]
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    assert solution.maxPathSum(root2) == 42
    
    print("All test cases passed!")
