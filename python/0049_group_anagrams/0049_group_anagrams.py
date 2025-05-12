from typing import List
from collections import defaultdict

"""
LeetCode Group Anagrams

Problem from LeetCode: https://leetcode.com/problems/group-anagrams/

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""

class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams together from an array of strings.
        Uses sorted strings as keys for grouping.
        
        Args:
            strs: Array of strings
            
        Returns:
            List[List[str]]: Grouped anagrams
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Sort the string to use as a key
            sorted_s = ''.join(sorted(s))
            anagram_map[sorted_s].append(s)
            
        # Return the values (groups of anagrams)
        return list(anagram_map.values())
    
    def group_anagrams_count(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams using character counts instead of sorting.
        More efficient for strings with a known character set.
        
        Args:
            strs: Array of strings
            
        Returns:
            List[List[str]]: Grouped anagrams
        """
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Count occurrences of each character (assuming lowercase English letters)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            # Use tuple of counts as key (lists are not hashable)
            anagram_map[tuple(count)].append(s)
            
        return list(anagram_map.values())
    
    def group_anagrams_prime(self, strs: List[str]) -> List[List[str]]:
        """
        Group anagrams using prime number multiplication.
        Each letter is assigned a prime number, and the product is the key.
        Note: This can lead to integer overflow for long strings.
        
        Args:
            strs: Array of strings
            
        Returns:
            List[List[str]]: Grouped anagrams
        """
        # Map each character to a prime number
        char_to_prime = {
            'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19,
            'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53,
            'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89,
            'y': 97, 'z': 101
        }
        
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Calculate the product of prime numbers
            product = 1
            for c in s:
                product *= char_to_prime[c]
                
            anagram_map[product].append(s)
            
        return list(anagram_map.values())

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result1 = solution.group_anagrams(strs1)
    print(f"Example 1: {result1}")
    # Expected output: [["eat","tea","ate"],["tan","nat"],["bat"]]
    
    # Example 2
    strs2 = [""]
    result2 = solution.group_anagrams(strs2)
    print(f"Example 2: {result2}")
    # Expected output: [[""]]
    
    # Example 3
    strs3 = ["a"]
    result3 = solution.group_anagrams(strs3)
    print(f"Example 3: {result3}")
    # Expected output: [["a"]]
    
    # Compare with other implementations
    print("\nUsing character count approach:")
    print(f"Example 1: {solution.group_anagrams_count(strs1)}")
    
    print("\nUsing prime number approach:")
    print(f"Example 1: {solution.group_anagrams_prime(strs1)}")
