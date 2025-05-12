from typing import List, Optional

"""
LeetCode 242. Valid Anagram

Problem from LeetCode: https://leetcode.com/problems/valid-anagram/

Description:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class Solution:

    def is_anagram(self, s: str, t: str) ->bool:
        """
        Determine if t is an anagram of s (using character count approach).
        
        Args:
            s: First string
            t: Second string
            
        Returns:
            bool: True if t is an anagram of s, False otherwise
        """
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for i in range(26):
            if count[i] != 0:
                return False
        return True

    def is_anagram_with_counter(self, s: str, t: str) ->bool:
        """
        Determine if t is an anagram of s (using Counter).
        
        Args:
            s: First string
            t: Second string
            
        Returns:
            bool: True if t is an anagram of s, False otherwise
        """
        from collections import Counter
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)
        return s_counter == t_counter

    def is_anagram_with_sorting(self, s: str, t: str) ->bool:
        """
        Determine if t is an anagram of s (using sorting).
        
        Args:
            s: First string
            t: Second string
            
        Returns:
            bool: True if t is an anagram of s, False otherwise
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "anagram"
    t1 = "nagaram"
    print(f"Example 1: s = \"{s1}\", t = \"{t1}\"")
    print(f"Output (character count): {solution.is_anagram(s1, t1)}")  # Expected output: True
    print(f"Output (Counter): {solution.is_anagram_with_counter(s1, t1)}")  # Expected output: True
    print(f"Output (sorting): {solution.is_anagram_with_sorting(s1, t1)}")  # Expected output: True
    
    # Example 2
    s2 = "rat"
    t2 = "car"
    print(f"\nExample 2: s = \"{s2}\", t = \"{t2}\"")
    print(f"Output (character count): {solution.is_anagram(s2, t2)}")  # Expected output: False
    print(f"Output (Counter): {solution.is_anagram_with_counter(s2, t2)}")  # Expected output: False
    print(f"Output (sorting): {solution.is_anagram_with_sorting(s2, t2)}")  # Expected output: False
    
    # Additional example with Unicode (for follow-up)
    s3 = "café"
    t3 = "cafè"  # Different Unicode character
    print(f"\nUnicode example: s = \"{s3}\", t = \"{t3}\"")
    print(f"Output (sorting): {solution.is_anagram_with_sorting(s3, t3)}")  # Expected output: False
