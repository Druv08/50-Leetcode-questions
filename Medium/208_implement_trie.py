"""
LeetCode #208 - Implement Trie (Prefix Tree)
Difficulty: Medium
Company: Microsoft, Google

Problem:
Implement a trie with insert, search, and startsWith methods.

Time Complexity: O(m) for all operations where m is key length
Space Complexity: O(n * m) where n is number of keys
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initialize the trie with root node
        """
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """
        Returns true if the word is in the trie
        """
        node = self.root
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_end_of_word
    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns true if there is any word in the trie that starts with the prefix
        """
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return True


# Test cases
if __name__ == "__main__":
    trie = Trie()
    
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    
    trie.insert("app")
    assert trie.search("app") == True
    
    print("All test cases passed!")
