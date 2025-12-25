"""
LeetCode #49 - Group Anagrams
Difficulty: Medium
Company: Google, Amazon

Problem:
Given an array of strings strs, group the anagrams together.

Example:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Time Complexity: O(n * k log k) where k is max length of string
Space Complexity: O(n * k)
"""

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Use sorted string as key in hashmap
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to create key
            key = ''.join(sorted(s))
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
    
    def groupAnagramsOptimized(self, strs: List[str]) -> List[List[str]]:
        """
        Use character count as key (better for long strings)
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Count characters
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use tuple of counts as key
            key = tuple(count)
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort for comparison
    result_sorted = [sorted(group) for group in result]
    expected = [sorted(group) for group in [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]]
    assert sorted(result_sorted) == sorted(expected)
    
    print("All test cases passed!")
