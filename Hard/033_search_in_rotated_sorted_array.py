"""
LeetCode #33 - Search in Rotated Sorted Array
Difficulty: Hard
Company: Microsoft, Amazon

Problem:
Search for a target value in a rotated sorted array in O(log n) time.

Example:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Modified binary search
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which half is sorted
            if nums[left] <= nums[mid]:
                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    
    # Test case 2
    assert solution.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    
    # Test case 3
    assert solution.search([1], 0) == -1
    
    print("All test cases passed!")
