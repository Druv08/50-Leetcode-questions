"""
LeetCode #94 - Binary Tree Inorder Traversal
Difficulty: Easy
Company: Apple

Problem:
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example:
Input: root = [1,null,2,3]
Output: [1,3,2]

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Recursive approach: Left -> Root -> Right
        """
        result = []
        
        def inorder(node):
            if not node:
                return
            
            # Traverse left subtree
            inorder(node.left)
            
            # Visit root
            result.append(node.val)
            
            # Traverse right subtree
            inorder(node.right)
        
        inorder(root)
        return result
    
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative approach using stack
        """
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process node
            current = stack.pop()
            result.append(current.val)
            
            # Move to right subtree
            current = current.right
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: [1,null,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    assert solution.inorderTraversal(root) == [1, 3, 2]
    
    # Test case 2: Empty tree
    assert solution.inorderTraversal(None) == []
    
    # Test case 3: Single node
    assert solution.inorderTraversal(TreeNode(1)) == [1]
    
    print("All test cases passed!")
