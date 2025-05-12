from typing import List


"""
LeetCode Verifying An Alien Dictionary

Problem from LeetCode: https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) 
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character 
which is less than any other character.

Constraints:
- 1 <= words.length <= 100
- 1 <= words[i].length <= 20
- order.length == 26
- All characters in words[i] and order are English lowercase letters.
"""

class Solution:

    def is_alien_sorted(self, words: List[str], order: str) ->bool:
        """
        Check if the words are sorted lexicographically by the alien language order.
        
        Args:
            words: List of words to check
            order: The alien language alphabet order
            
        Returns:
            bool: True if the words are sorted according to the alien order, False otherwise
        """
        order_map = {char: i for i, char in enumerate(order)}
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for j in range(len(word1)):
                if j >= len(word2):
                    return False
                if word1[j] != word2[j]:
                    if order_map[word2[j]] < order_map[word1[j]]:
                        return False
                    break
        return True

    def isAlienSorted_alt(self, words: List[str], order: str) ->bool:
        """
        Alternative implementation using a key function for comparisons.
        
        Args:
            words: List of words to check
            order: The alien language alphabet order
            
        Returns:
            bool: True if the words are sorted, False otherwise
        """
        order_map = {char: i for i, char in enumerate(order)}
        for w1, w2 in zip(words, words[1:]):
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return False
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if order_map[c1] > order_map[c2]:
                        return False
                    break
        return True


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    result = solution.is_alien_sorted(words, order)
    print(f"Example 1: {result}")  # Expected: True
    
    # Example 2
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    result = solution.is_alien_sorted(words, order)
    print(f"Example 2: {result}")  # Expected: False
    
    # Example 3
    words = ["apple","app"]
    order = "abcdefghijklmnopqrstuvwxyz"
    result = solution.is_alien_sorted(words, order)
    print(f"Example 3: {result}")  # Expected: False
