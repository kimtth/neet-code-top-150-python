from collections import defaultdict


"""
LeetCode Longest Repeating Character Replacement

Problem from LeetCode: https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and 
change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
    The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
    1 <= s.length <= 10^5
    s consists of only uppercase English letters.
    0 <= k <= s.length
"""

class Solution:

    def character_replacement(self, s: str, k: int) ->int:
        """
        Find the length of the longest substring containing the same letter after 
        replacing at most k characters.
        
        Args:
            s: The input string
            k: The maximum number of characters to replace
            
        Returns:
            int: Length of the longest substring with same letter after replacements
        """
        occurrence = [0] * 26
        left = 0
        max_occurrence = 0
        max_length = 0
        for right in range(len(s)):
            char_index = ord(s[right]) - ord('A')
            occurrence[char_index] += 1
            max_occurrence = max(max_occurrence, occurrence[char_index])
            if right - left + 1 - max_occurrence > k:
                occurrence[ord(s[left]) - ord('A')] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

    def characterReplacement_dict(self, s: str, k: int) ->int:
        """
        Implementation using a defaultdict for character counting.
        
        Args:
            s: The input string
            k: The maximum number of characters to replace
            
        Returns:
            int: Length of the longest substring with same letter after replacements
        """
        char_counts = defaultdict(int)
        left = 0
        max_occurrence = 0
        max_length = 0
        for right in range(len(s)):
            char_counts[s[right]] += 1
            max_occurrence = max(max_occurrence, char_counts[s[right]])
            if right - left + 1 - max_occurrence > k:
                char_counts[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

    def characterReplacement_optimized(self, s: str, k: int) ->int:
        """
        Optimized implementation that avoids recalculating max each time.
        
        Args:
            s: The input string
            k: The maximum number of characters to replace
            
        Returns:
            int: Length of the longest substring with same letter after replacements
        """
        char_counts = defaultdict(int)
        left = 0
        max_occurrence = 0
        for right in range(len(s)):
            char_counts[s[right]] += 1
            max_occurrence = max(max_occurrence, char_counts[s[right]])
            window_size = right - left + 1
            if window_size - max_occurrence > k:
                char_counts[s[left]] -= 1
                left += 1
        return len(s) - left


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: s = "ABAB", k = 2
    print("Example 1:")
    result = solution.character_replacement("ABAB", 2)
    print(f"Output: {result}")  # Expected: 4
    
    # Example 2: s = "AABABBA", k = 1
    print("\nExample 2:")
    result = solution.character_replacement("AABABBA", 1)
    print(f"Output: {result}")  # Expected: 4
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("Dict approach:", solution.characterReplacement_dict("ABAB", 2))
    print("Optimized approach:", solution.characterReplacement_optimized("ABAB", 2))
