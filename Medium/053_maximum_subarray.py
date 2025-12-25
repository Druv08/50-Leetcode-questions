"""
LeetCode #53 - Maximum Subarray
Difficulty: Medium
Company: Microsoft, Amazon

Problem:
Find the contiguous subarray with the largest sum.

Example:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's Algorithm
        """
        if not nums:
            return 0
        
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            # Either extend current subarray or start new one
            current_sum = max(num, current_sum + num)
            
            # Update maximum sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    
    # Test case 2
    assert solution.maxSubArray([1]) == 1
    
    # Test case 3
    assert solution.maxSubArray([5, 4, -1, 7, 8]) == 23
    
    # Test case 4
    assert solution.maxSubArray([-1]) == -1
    
    print("All test cases passed!")
