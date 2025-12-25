"""
LeetCode #56 - Merge Intervals
Difficulty: Medium
Company: Meta, Amazon

Problem:
Given an array of intervals, merge all overlapping intervals.

Example:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Sort intervals and merge overlapping ones
        """
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            last_merged = merged[-1]
            
            # Check if current overlaps with last merged
            if current[0] <= last_merged[1]:
                # Merge by updating end time
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # No overlap, add new interval
                merged.append(current)
        
        return merged


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    
    # Test case 2
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    
    # Test case 3
    assert solution.merge([[1, 4], [0, 4]]) == [[0, 4]]
    
    print("All test cases passed!")
