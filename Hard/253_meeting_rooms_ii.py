"""
LeetCode #253 - Meeting Rooms II
Difficulty: Hard
Company: Google, Amazon

Problem:
Find the minimum number of conference rooms required for meetings.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """
        Use min heap to track end times of meetings
        """
        if not intervals:
            return 0
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # Min heap to track end times
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        
        for i in range(1, len(intervals)):
            # If earliest ending meeting finishes before current starts
            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            
            # Add current meeting's end time
            heapq.heappush(rooms, intervals[i][1])
        
        return len(rooms)


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.minMeetingRooms([[0, 30], [5, 10], [15, 20]]) == 2
    
    # Test case 2
    assert solution.minMeetingRooms([[7, 10], [2, 4]]) == 1
    
    # Test case 3
    assert solution.minMeetingRooms([[1, 5], [8, 9], [8, 9]]) == 2
    
    print("All test cases passed!")
