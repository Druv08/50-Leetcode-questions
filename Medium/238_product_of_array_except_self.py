"""
LeetCode #238 - Product of Array Except Self
Difficulty: Medium
Company: Meta, Amazon

Problem:
Given an integer array nums, return an array answer such that answer[i] is equal to 
the product of all the elements of nums except nums[i].

Example:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Time Complexity: O(n)
Space Complexity: O(1) excluding output array
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Two pass approach: left products and right products
        """
        n = len(nums)
        result = [1] * n
        
        # First pass: calculate left products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Second pass: calculate right products and multiply
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    
    # Test case 2
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    
    print("All test cases passed!")
