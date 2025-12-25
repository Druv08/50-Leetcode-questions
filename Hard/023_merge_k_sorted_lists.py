"""
LeetCode #23 - Merge K Sorted Lists
Difficulty: Hard
Company: Amazon, Google

Problem:
Merge k sorted linked lists and return it as one sorted list.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Time Complexity: O(N log k) where N is total nodes, k is number of lists
Space Complexity: O(k) for heap
"""

from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Use min heap to efficiently merge k lists
        """
        if not lists:
            return None
        
        # Initialize heap with first node from each list
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            # Add next node from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next


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
    lists = [
        create_linked_list([1, 4, 5]),
        create_linked_list([1, 3, 4]),
        create_linked_list([2, 6])
    ]
    result = solution.mergeKLists(lists)
    assert linked_list_to_array(result) == [1, 1, 2, 3, 4, 4, 5, 6]
    
    print("All test cases passed!")
