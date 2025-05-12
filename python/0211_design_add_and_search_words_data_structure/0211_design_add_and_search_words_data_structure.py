from typing import List, Optional

"""
LeetCode 211: Design Add and Search Words Data Structure

Problem from LeetCode: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:
- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. 
  word may contain dots '.' where dots can be matched with any letter.

Example:
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:
[null,null,null,null,false,true,true,true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- There will be at most 3 dots in word for search queries.
- At most 10^4 calls will be made to addWord and search.
"""

class TrieNode:
    """Node class for the Trie data structure."""

    def __init__(self):
        """Initialize a TrieNode with empty children map and word flag."""
        self.children = {}
        self.is_word = False


class WordDictionary:
    """
    Data structure that supports adding new words and searching if a string matches any previously added string.
    Special character '.' can match any letter in search pattern.
    """

    def __init__(self):
        """Initialize the WordDictionary with an empty trie."""
        self.root = TrieNode()

    def add_word(self, word: str) ->None:
        """
        Add a word into the data structure.
        
        Args:
            word: The word to add
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) ->bool:
        """
        Return True if the word is in the data structure, including support for '.' wildcard.
        
        Args:
            word: The word to search, possibly containing '.' to match any letter
            
        Returns:
            bool: True if the word is found, False otherwise
        """
        return self._search_in_node(word, 0, self.root)

    def _search_in_node(self, word: str, index: int, node: TrieNode) ->bool:
        """
        Helper method to search for a word starting from the given index and node.
        
        Args:
            word: The word to search
            index: Current position in the word
            node: Current node in the trie
            
        Returns:
            bool: True if the word is found, False otherwise
        """
        if index == len(word):
            return node.is_word
        ch = word[index]
        if ch == '.':
            for child_ch in node.children:
                if self._search_in_node(word, index + 1, node.children[
                    child_ch]):
                    return True
            return False
        if ch in node.children:
            return self._search_in_node(word, index + 1, node.children[ch])
        return False


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    wordDictionary = WordDictionary()
    wordDictionary.add_word("bad")
    wordDictionary.add_word("dad")
    wordDictionary.add_word("mad")
    
    # Search operations
    print(wordDictionary.search("pad"))  # Output: False
    print(wordDictionary.search("bad"))  # Output: True
    print(wordDictionary.search(".ad"))  # Output: True
    print(wordDictionary.search("b.."))  # Output: True
    
    # Additional test cases
    print(wordDictionary.search("..."))   # Output: True
    print(wordDictionary.search("...."))  # Output: False
    
    wordDictionary.add_word("body")
    print(wordDictionary.search("b.dy"))  # Output: True
