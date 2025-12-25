"""
LeetCode #121 - Best Time to Buy and Sell Stock
Difficulty: Easy
Company: Apple, Amazon

Problem:
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        One pass approach tracking minimum price and maximum profit
        """
        if not prices:
            return 0
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update minimum price seen so far
            min_price = min(min_price, price)
            
            # Calculate profit if we sell at current price
            profit = price - min_price
            
            # Update maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    
    # Test case 2
    assert solution.maxProfit([7, 6, 4, 3, 1]) == 0
    
    # Test case 3
    assert solution.maxProfit([2, 4, 1]) == 2
    
    # Test case 4
    assert solution.maxProfit([1, 2]) == 1
    
    print("All test cases passed!")
