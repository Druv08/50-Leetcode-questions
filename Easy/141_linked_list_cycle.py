"""
LeetCode #141 - Linked List Cycle
Difficulty: Easy
Company: Microsoft

Problem:
Given head, the head of a linked list, determine if the linked list has a cycle in it.

Example:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's Cycle Detection Algorithm (Tortoise and Hare)
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # Cycle detected
            if slow == fast:
                return True
        
        return False


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1: Cycle exists
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create cycle
    assert solution.hasCycle(head) == True
    
    # Test case 2: No cycle
    head2 = ListNode(1)
    head2.next = ListNode(2)
    assert solution.hasCycle(head2) == False
    
    # Test case 3: Single node, no cycle
    head3 = ListNode(1)
    assert solution.hasCycle(head3) == False
    
    print("All test cases passed!")
