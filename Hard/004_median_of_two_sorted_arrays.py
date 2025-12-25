"""
LeetCode #4 - Median of Two Sorted Arrays
Difficulty: Hard
Company: Google

Problem:
Given two sorted arrays nums1 and nums2, return the median of the two sorted arrays.

Example:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000

Time Complexity: O(log(min(m,n)))
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Binary search on the smaller array
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1
            
            # Handle edge cases
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]
            
            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]
            
            # Check if we found the correct partition
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                # Even total length
                if (m + n) % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                # Odd total length
                else:
                    return max(maxLeft1, maxLeft2)
            elif maxLeft1 > minRight2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        
        raise ValueError("Input arrays are not sorted")


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0
    
    # Test case 2
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    
    print("All test cases passed!")
