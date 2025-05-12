from typing import List, Optional

"""
LeetCode 208. Implement Trie (Prefix Tree)

Problem from LeetCode: https://leetcode.com/problems/implement-trie-prefix-tree/

Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
- 1 <= word.length, prefix.length <= 2000
- word and prefix consist only of lowercase English letters.
- At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.
"""

class TrieNode:
    """
    A node in the Trie data structure.
    Each node contains links to its children and a flag indicating if it's the end of a word.
    """

    def __init__(self):
        """Initialize an empty TrieNode with 26 possible children (for lowercase letters a-z)."""
        self.links = [None] * 26
        self.is_end = False

    def contains_key(self, ch: str) ->bool:
        """
        Check if the node contains a link for the given character.
        
        Args:
            ch: A single character
            
        Returns:
            bool: True if the link exists, False otherwise
        """
        return self.links[ord(ch) - ord('a')] is not None

    def get(self, ch: str) ->'TrieNode':
        """
        Get the node linked to the given character.
        
        Args:
            ch: A single character
            
        Returns:
            TrieNode: The linked node for the character
        """
        return self.links[ord(ch) - ord('a')]

    def put(self, ch: str, node: 'TrieNode') ->None:
        """
        Create a link to a node for the given character.
        
        Args:
            ch: A single character
            node: The TrieNode to link to
        """
        self.links[ord(ch) - ord('a')] = node

    def set_end(self) ->None:
        """Mark the current node as the end of a word."""
        self.is_end = True

    def is_end_of_word(self) ->bool:
        """
        Check if the current node marks the end of a word.
        
        Returns:
            bool: True if this node marks the end of a word, False otherwise
        """
        return self.is_end


class Trie:
    """
    Trie data structure for efficient word storage and retrieval.
    Supports insertion, search, and prefix search operations.
    """

    def __init__(self):
        """Initialize an empty Trie with a root node."""
        self.root = TrieNode()

    def insert(self, word: str) ->None:
        """
        Insert a word into the trie.
        
        Args:
            word: The word to insert
        """
        node = self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch, TrieNode())
            node = node.get(ch)
        node.set_end()

    def search_prefix(self, word: str) ->TrieNode:
        """
        Search for a prefix in the trie.
        
        Args:
            word: The prefix to search for
            
        Returns:
            TrieNode: The node at the end of the prefix path, or None if prefix not found
        """
        node = self.root
        for ch in word:
            if node.contains_key(ch):
                node = node.get(ch)
            else:
                return None
        return node

    def search(self, word: str) ->bool:
        """
        Search for a complete word in the trie.
        
        Args:
            word: The word to search for
            
        Returns:
            bool: True if the word exists in the trie, False otherwise
        """
        node = self.search_prefix(word)
        return node is not None and node.is_end_of_word()

    def starts_with(self, prefix: str) ->bool:
        """
        Check if there is any word in the trie that starts with the given prefix.
        
        Args:
            prefix: The prefix to search for
            
        Returns:
            bool: True if at least one word with the prefix exists, False otherwise
        """
        node = self.search_prefix(prefix)
        return node is not None


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    print("Example 1:")
    print("Operations: [\"Trie\", \"insert\", \"search\", \"search\", \"startsWith\", \"insert\", \"search\"]")
    print("Values: [[], [\"apple\"], [\"apple\"], [\"app\"], [\"app\"], [\"app\"], [\"app\"]]")
    print("Output:")
    
    trie = Trie()  # null
    print("Trie() -> null")
    
    trie.insert("apple")  # null
    print("insert(\"apple\") -> null")
    
    result1 = trie.search("apple")
    print(f"search(\"apple\") -> {result1}")  # return True
    
    result2 = trie.search("app")
    print(f"search(\"app\") -> {result2}")  # return False
    
    result3 = trie.starts_with("app")
    print(f"startsWith(\"app\") -> {result3}")  # return True
    
    trie.insert("app")  # null
    print("insert(\"app\") -> null")
    
    result4 = trie.search("app")
    print(f"search(\"app\") -> {result4}")  # return True
