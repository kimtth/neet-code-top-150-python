from typing import List
from collections import Counter


"""
LeetCode Permutation In String

Problem from LeetCode: https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: false

Constraints:
    1 <= s1.length, s2.length <= 10^4
    s1 and s2 consist of lowercase English letters.
"""

class Solution:

    def check_inclusion(self, s1: str, s2: str) ->bool:
        """
        Check if s2 contains a permutation of s1.
        
        Args:
            s1: First string
            s2: Second string
            
        Returns:
            bool: True if s2 contains a permutation of s1, False otherwise
        """
        if len(s1) > len(s2):
            return False
        s1_map = [0] * 26
        s2_map = [0] * 26
        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] += 1
        for i in range(len(s2) - len(s1)):
            if self._matches(s1_map, s2_map):
                return True
            s2_map[ord(s2[i + len(s1)]) - ord('a')] += 1
            s2_map[ord(s2[i]) - ord('a')] -= 1
        return self._matches(s1_map, s2_map)

    def _matches(self, s1_map: List[int], s2_map: List[int]) ->bool:
        """
        Check if two frequency maps match.
        
        Args:
            s1_map: Frequency map for s1
            s2_map: Frequency map for s2
            
        Returns:
            bool: True if the maps match, False otherwise
        """
        for i in range(26):
            if s1_map[i] != s2_map[i]:
                return False
        return True

    def checkInclusion_counter(self, s1: str, s2: str) ->bool:
        """
        Check if s2 contains a permutation of s1 using Counter.
        
        Args:
            s1: First string
            s2: Second string
            
        Returns:
            bool: True if s2 contains a permutation of s1, False otherwise
        """
        if len(s1) > len(s2):
            return False
        s1_counter = Counter(s1)
        window_size = len(s1)
        window_counter = Counter(s2[:window_size])
        if window_counter == s1_counter:
            return True
        for i in range(len(s2) - window_size):
            window_counter[s2[i]] -= 1
            if window_counter[s2[i]] == 0:
                del window_counter[s2[i]]
            window_counter[s2[i + window_size]] += 1
            if window_counter == s1_counter:
                return True
        return False

    def checkInclusion_optimized(self, s1: str, s2: str) ->bool:
        """
        Optimized sliding window approach with a single comparison.
        
        Args:
            s1: First string
            s2: Second string
            
        Returns:
            bool: True if s2 contains a permutation of s1, False otherwise
        """
        if len(s1) > len(s2):
            return False
        counter = Counter(s1)
        matches = 0
        required = len(counter)
        for i in range(len(s1)):
            char = s2[i]
            if char in counter:
                counter[char] -= 1
                if counter[char] == 0:
                    matches += 1
        if matches == required:
            return True
        for i in range(len(s1), len(s2)):
            add_char = s2[i]
            if add_char in counter:
                counter[add_char] -= 1
                if counter[add_char] == 0:
                    matches += 1
            remove_char = s2[i - len(s1)]
            if remove_char in counter:
                if counter[remove_char] == 0:
                    matches -= 1
                counter[remove_char] += 1
            if matches == required:
                return True
        return False


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: s1 = "ab", s2 = "eidbaooo"
    print("Example 1:")
    result = solution.check_inclusion("ab", "eidbaooo")
    print(f"Output: {result}")  # Expected: True
    
    # Example 2: s1 = "ab", s2 = "eidboaoo"
    print("\nExample 2:")
    result = solution.check_inclusion("ab", "eidboaoo")
    print(f"Output: {result}")  # Expected: False
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("Counter approach:", solution.checkInclusion_counter("ab", "eidbaooo"))
    print("Optimized approach:", solution.checkInclusion_optimized("ab", "eidbaooo"))
