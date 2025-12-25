"""
LeetCode #17 - Letter Combinations of a Phone Number
Difficulty: Medium
Company: Google, Amazon

Problem:
Given a string containing digits from 2-9, return all possible letter combinations.

Example:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Time Complexity: O(4^n) where n is length of digits
Space Complexity: O(4^n)
"""

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Backtracking approach
        """
        if not digits:
            return []
        
        # Digit to letters mapping
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, current):
            # Base case: completed combination
            if index == len(digits):
                result.append(current)
                return
            
            # Get letters for current digit
            letters = phone[digits[index]]
            
            # Try each letter
            for letter in letters:
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result = solution.letterCombinations("23")
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert sorted(result) == sorted(expected)
    
    # Test case 2
    assert solution.letterCombinations("") == []
    
    # Test case 3
    assert solution.letterCombinations("2") == ["a", "b", "c"]
    
    print("All test cases passed!")
