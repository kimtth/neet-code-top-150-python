from typing import List, Optional

"""
LeetCode Longest Common Subsequence

Problem from LeetCode: https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence. 
A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
- 1 <= text1.length, text2.length <= 1000
- text1 and text2 consist of only lowercase English characters.
"""

class Solution:

    def longest_common_subsequence(self, text1, text2):
        matrix = [[(0) for _ in range(len(text2) + 1)] for _ in range(len(
            text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1 + matrix[i + 1][j + 1]
                else:
                    matrix[i][j] = max(matrix[i + 1][j], matrix[i][j + 1])
        return matrix[0][0]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    text1 = "abcde"
    text2 = "ace"
    result = solution.longest_common_subsequence(text1, text2)
    print(f"Example 1: {result}")  # Expected: 3
    
    # Example 2
    text1 = "abc"
    text2 = "abc"
    result = solution.longest_common_subsequence(text1, text2)
    print(f"Example 2: {result}")  # Expected: 3
    
    # Example 3
    text1 = "abc"
    text2 = "def"
    result = solution.longest_common_subsequence(text1, text2)
    print(f"Example 3: {result}")  # Expected: 0
