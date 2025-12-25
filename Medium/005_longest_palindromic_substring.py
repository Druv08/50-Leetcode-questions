"""
LeetCode #5 - Longest Palindromic Substring
Difficulty: Medium
Company: Microsoft, Amazon

Problem:
Given a string s, return the longest palindromic substring in s.

Example:
Input: s = "babad"
Output: "bab" or "aba"

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Expand around center approach
        """
        if not s:
            return ""
        
        def expand_around_center(left, right):
            """Expand around center and return palindrome length"""
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        
        start = 0
        max_len = 0
        
        for i in range(len(s)):
            # Check for odd length palindromes (single center)
            len1 = expand_around_center(i, i)
            
            # Check for even length palindromes (two centers)
            len2 = expand_around_center(i, i + 1)
            
            # Get the maximum length
            current_len = max(len1, len2)
            
            if current_len > max_len:
                max_len = current_len
                # Calculate starting position
                start = i - (current_len - 1) // 2
        
        return s[start:start + max_len]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result = solution.longestPalindrome("babad")
    assert result in ["bab", "aba"]
    
    # Test case 2
    assert solution.longestPalindrome("cbbd") == "bb"
    
    # Test case 3
    assert solution.longestPalindrome("a") == "a"
    
    # Test case 4
    assert solution.longestPalindrome("racecar") == "racecar"
    
    print("All test cases passed!")
