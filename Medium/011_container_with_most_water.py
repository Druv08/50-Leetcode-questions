"""
LeetCode #11 - Container With Most Water
Difficulty: Medium
Company: Google

Problem:
Find two lines that together with the x-axis form a container that holds the most water.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointer approach from both ends
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # Update maximum area
            max_area = max(max_area, current_area)
            
            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    
    # Test case 2
    assert solution.maxArea([1, 1]) == 1
    
    # Test case 3
    assert solution.maxArea([4, 3, 2, 1, 4]) == 16
    
    print("All test cases passed!")
