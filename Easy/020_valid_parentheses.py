"""
LeetCode #20 - Valid Parentheses
Difficulty: Easy
Company: Meta

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

Example:
Input: s = "()[]{}"
Output: true

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Using stack to match opening and closing brackets
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Mapping of closing to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # Pop from stack if not empty, else use dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the mapping matches
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push opening bracket to stack
                stack.append(char)
        
        # Valid if stack is empty
        return not stack


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    assert solution.isValid("()") == True
    
    # Test case 2
    assert solution.isValid("()[]{}") == True
    
    # Test case 3
    assert solution.isValid("(]") == False
    
    # Test case 4
    assert solution.isValid("([)]") == False
    
    # Test case 5
    assert solution.isValid("{[]}") == True
    
    print("All test cases passed!")
