from typing import List, Optional

"""
LeetCode Longest Substring Without Repeating Characters

Problem from LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Description:
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

class Solution:

    def length_of_longest_substring(self, s: str) ->int:
        if s is None or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        left = 0
        right = 0
        ans = 0
        char_set = set()
        while right < len(s):
            c = s[right]
            while c in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(c)
            ans = max(ans, right - left + 1)
            right += 1
        return ans


if __name__ == '__main__':
    # Example usage based on LeetCode samples
    solution = Solution()
    
    # Example 1
    s1 = "abcabcbb"
    result1 = solution.length_of_longest_substring(s1)
    print(f"Example 1: \"{s1}\" -> {result1}")  # Expected output: 3
    
    # Example 2
    s2 = "bbbbb"
    result2 = solution.length_of_longest_substring(s2)
    print(f"Example 2: \"{s2}\" -> {result2}")  # Expected output: 1
    
    # Example 3
    s3 = "pwwkew"
    result3 = solution.length_of_longest_substring(s3)
    print(f"Example 3: \"{s3}\" -> {result3}")  # Expected output: 3
