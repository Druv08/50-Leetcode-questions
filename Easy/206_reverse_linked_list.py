"""
LeetCode #206 - Reverse Linked List
Difficulty: Easy
Company: Microsoft, Amazon

Problem:
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach using three pointers
        """
        prev = None
        current = head
        
        while current:
            # Store next node
            next_node = current.next
            
            # Reverse the link
            current.next = prev
            
            # Move pointers forward
            prev = current
            current = next_node
        
        return prev
    
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach
        """
        if not head or not head.next:
            return head
        
        # Reverse the rest of the list
        new_head = self.reverseListRecursive(head.next)
        
        # Reverse the current node
        head.next.next = head
        head.next = None
        
        return new_head


# Helper functions
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    head = create_linked_list([1, 2, 3, 4, 5])
    result = solution.reverseList(head)
    assert linked_list_to_array(result) == [5, 4, 3, 2, 1]
    
    # Test case 2
    head2 = create_linked_list([1, 2])
    result2 = solution.reverseList(head2)
    assert linked_list_to_array(result2) == [2, 1]
    
    print("All test cases passed!")
