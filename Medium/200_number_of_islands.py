"""
LeetCode #200 - Number of Islands
Difficulty: Medium
Company: Amazon, Google

Problem:
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

Example:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Time Complexity: O(m * n)
Space Complexity: O(m * n) for recursion stack
"""

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        DFS approach to mark visited islands
        """
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            """Mark all connected land cells as visited"""
            # Boundary and water checks
            if (r < 0 or r >= rows or c < 0 or c >= cols or 
                grid[r][c] == '0'):
                return
            
            # Mark as visited
            grid[r][c] = '0'
            
            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Iterate through grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c)  # Mark entire island
        
        return island_count


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    grid1 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert solution.numIslands(grid1) == 3
    
    # Test case 2
    grid2 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert solution.numIslands(grid2) == 1
    
    print("All test cases passed!")
