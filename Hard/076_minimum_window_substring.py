"""
LeetCode #76 - Minimum Window Substring
Difficulty: Hard
Company: Google, Meta

Problem:
Find the minimum window substring of s which contains all characters in t.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Time Complexity: O(|S| + |T|)
Space Complexity: O(|S| + |T|)
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Sliding window with character frequency map
        """
        if not s or not t:
            return ""
        
        # Character frequency map for t
        target_count = Counter(t)
        required = len(target_count)
        
        # Sliding window pointers
        left, right = 0, 0
        formed = 0
        
        # Window character count
        window_count = {}
        
        # Result (length, left, right)
        result = float('inf'), None, None
        
        while right < len(s):
            # Add character from right
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if frequency matches
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1
            
            # Try to contract window
            while left <= right and formed == required:
                char = s[left]
                
                # Update result if smaller window found
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove from left
                window_count[char] -= 1
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    
    # Test case 2
    assert solution.minWindow("a", "a") == "a"
    
    # Test case 3
    assert solution.minWindow("a", "aa") == ""
    
    print("All test cases passed!")
