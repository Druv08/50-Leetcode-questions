"""
LeetCode #680 - Valid Palindrome II
Difficulty: Easy
Company: Meta

Problem:
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Two pointer approach with one deletion allowed
        """
        def is_palindrome(left, right):
            """Helper function to check if substring is palindrome"""
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                # Try skipping either left or right character
                return (is_palindrome(left + 1, right) or 
                        is_palindrome(left, right - 1))
            left += 1
            right -= 1
        
        return True


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.validPalindrome("aba") == True
    
    # Test case 2
    assert solution.validPalindrome("abca") == True
    
    # Test case 3
    assert solution.validPalindrome("abc") == False
    
    # Test case 4
    assert solution.validPalindrome("racecar") == True
    
    # Test case 5
    assert solution.validPalindrome("deeee") == True
    
    print("All test cases passed!")
