from typing import List, Optional

"""
LeetCode 115. Distinct Subsequences

Problem from LeetCode: https://leetcode.com/problems/distinct-subsequences/

Description:
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
There are 3 ways to get "rabbit" from "rabbbit":
"ra_bbit" -> "rabbit"
"rab_bit" -> "rabbit"
"rabb_it" -> "rabbit"

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
There are 5 ways to get "bag" from "babgbag":
"ba_g___" -> "bag"
"ba__g__" -> "bag"
"b__ag__" -> "bag"
"__bag__" -> "bag"
"____bag" -> "bag"

Constraints:
- 1 <= s.length, t.length <= 1000
- s and t consist of lowercase English letters.
"""

class Solution:

    def num_distinct(self, s, t):
        m = len(s)
        n = len(t)
        dp = [[(0) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][n]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "rabbbit"
    t1 = "rabbit"
    result1 = solution.num_distinct(s1, t1)
    print(f"Input: s = \"{s1}\", t = \"{t1}\"")
    print(f"Output: {result1}")  # Expected output: 3
    
    # Example 2
    s2 = "babgbag"
    t2 = "bag"
    result2 = solution.num_distinct(s2, t2)
    print(f"Input: s = \"{s2}\", t = \"{t2}\"")
    print(f"Output: {result2}")  # Expected output: 5
