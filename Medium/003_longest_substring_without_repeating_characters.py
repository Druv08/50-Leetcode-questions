"""
LeetCode #3 - Longest Substring Without Repeating Characters
Difficulty: Medium
Company: Google, Amazon

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Time Complexity: O(n)
Space Complexity: O(min(n, m)) where m is charset size
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window with hashmap
        """
        char_index = {}
        max_length = 0
        start = 0
        
        for end, char in enumerate(s):
            # If character is repeated and within current window
            if char in char_index and char_index[char] >= start:
                # Move start to right of last occurrence
                start = char_index[char] + 1
            
            # Update character's last seen index
            char_index[char] = end
            
            # Update max length
            max_length = max(max_length, end - start + 1)
        
        return max_length


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    
    # Test case 2
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    
    # Test case 3
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    
    # Test case 4
    assert solution.lengthOfLongestSubstring("") == 0
    
    print("All test cases passed!")
