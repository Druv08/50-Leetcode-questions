"""
LeetCode #1 - Two Sum
Difficulty: Easy
Company: Amazon, Microsoft

Problem:
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Using HashMap approach for O(n) time complexity
        """
        # Dictionary to store number and its index
        num_map = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if complement exists in map
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store current number and index
            num_map[num] = i
        
        return []  # No solution found


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    
    # Test case 2
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    
    # Test case 3
    assert solution.twoSum([3, 3], 6) == [0, 1]
    
    print("All test cases passed!")
