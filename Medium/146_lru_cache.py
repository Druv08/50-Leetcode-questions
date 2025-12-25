"""
LeetCode #146 - LRU Cache
Difficulty: Medium
Company: Amazon, Microsoft

Problem:
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Time Complexity: O(1) for get and put
Space Complexity: O(capacity)
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        """
        Using OrderedDict for O(1) operations
        """
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key: int) -> int:
        """
        Get value and mark as recently used
        """
        if key not in self.cache:
            return -1
        
        # Move to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair, evict LRU if needed
        """
        if key in self.cache:
            # Update existing key
            self.cache.move_to_end(key)
        
        self.cache[key] = value
        
        # Check capacity
        if len(self.cache) > self.capacity:
            # Remove least recently used (first item)
            self.cache.popitem(last=False)


# Alternative implementation using custom doubly linked list
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCacheManual:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Dummy head and tail nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        """Remove node from linked list"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    def _add_to_head(self, node):
        """Add node right after head"""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        # Move to head (most recently used)
        self._remove(node)
        self._add_to_head(node)
        return node.value
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update and move to head
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Create new node
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            
            # Check capacity
            if len(self.cache) > self.capacity:
                # Remove LRU (tail.prev)
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]


# Test cases
if __name__ == "__main__":
    # Test case 1
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1
    lru.put(3, 3)  # Evicts key 2
    assert lru.get(2) == -1
    lru.put(4, 4)  # Evicts key 1
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    
    print("All test cases passed!")
