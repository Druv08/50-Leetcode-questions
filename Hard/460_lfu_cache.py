"""
LeetCode #460 - LFU Cache
Difficulty: Hard
Company: Amazon

Problem:
Design and implement a Least Frequently Used (LFU) cache.

Time Complexity: O(1) for get and put
Space Complexity: O(capacity)
"""

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        """
        Initialize LFU cache with capacity
        """
        self.capacity = capacity
        self.min_freq = 0
        
        # key -> (value, frequency)
        self.key_value_freq = {}
        
        # frequency -> OrderedDict of keys (ordered by recency)
        self.freq_keys = defaultdict(OrderedDict)
    
    def _update_freq(self, key):
        """Update frequency of a key"""
        value, freq = self.key_value_freq[key]
        
        # Remove from current frequency bucket
        del self.freq_keys[freq][key]
        
        # Update minimum frequency if bucket is empty
        if not self.freq_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        
        # Add to new frequency bucket
        new_freq = freq + 1
        self.freq_keys[new_freq][key] = None
        self.key_value_freq[key] = (value, new_freq)
    
    def get(self, key: int) -> int:
        """
        Get value and update frequency
        """
        if key not in self.key_value_freq:
            return -1
        
        self._update_freq(key)
        return self.key_value_freq[key][0]
    
    def put(self, key: int, value: int) -> None:
        """
        Put key-value pair, evict LFU if needed
        """
        if self.capacity <= 0:
            return
        
        if key in self.key_value_freq:
            # Update existing key
            self.key_value_freq[key] = (value, self.key_value_freq[key][1])
            self._update_freq(key)
        else:
            # Check capacity
            if len(self.key_value_freq) >= self.capacity:
                # Evict LFU (and LRU if tie)
                evict_key, _ = self.freq_keys[self.min_freq].popitem(last=False)
                del self.key_value_freq[evict_key]
            
            # Add new key
            self.key_value_freq[key] = (value, 1)
            self.freq_keys[1][key] = None
            self.min_freq = 1


# Test cases
if __name__ == "__main__":
    # Test case 1
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    assert lfu.get(1) == 1
    lfu.put(3, 3)  # Evicts key 2
    assert lfu.get(2) == -1
    assert lfu.get(3) == 3
    lfu.put(4, 4)  # Evicts key 1
    assert lfu.get(1) == -1
    assert lfu.get(3) == 3
    assert lfu.get(4) == 4
    
    print("All test cases passed!")
