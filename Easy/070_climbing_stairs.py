"""
LeetCode #70 - Climbing Stairs
Difficulty: Easy
Company: Microsoft

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Dynamic Programming approach (Fibonacci pattern)
        dp[i] = dp[i-1] + dp[i-2]
        """
        if n <= 2:
            return n
        
        # Only need to track last two values
        prev2 = 1  # n=1
        prev1 = 2  # n=2
        
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return prev1


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.climbStairs(2) == 2
    
    # Test case 2
    assert solution.climbStairs(3) == 3
    
    # Test case 3
    assert solution.climbStairs(5) == 8
    
    # Test case 4
    assert solution.climbStairs(10) == 89
    
    print("All test cases passed!")
