from typing import List

"""
LeetCode Palindrome Partitioning

Problem from LeetCode: https://leetcode.com/problems/palindrome-partitioning/

Description:
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Partition a string such that every substring is a palindrome.
        
        Args:
            s: Input string
            
        Returns:
            List[List[str]]: All possible palindrome partitioning of s
        """
        result = []
        self.backtrack(result, [], s, 0)
        return result

    def backtrack(self, result: List[List[str]], current: List[str], s: str, start: int) -> None:
        """
        Backtracking helper function to generate all palindrome partitions.
        
        Args:
            result: List to collect all valid partitions
            current: Current partition being built
            s: Input string
            start: Starting index for the current substring
        """
        # If we reached the end of the string, we have a valid partition
        if start == len(s):
            result.append(current[:])
            return
            
        # Try all possible substrings starting from the current position
        for end in range(start, len(s)):
            # If the substring is a palindrome
            if self.is_palindrome(s, start, end):
                # Add the palindrome to the current partition
                current.append(s[start:end + 1])
                # Recursively partition the rest of the string
                self.backtrack(result, current, s, end + 1)
                # Backtrack by removing the last added substring
                current.pop()

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        """
        Check if a substring is a palindrome.
        
        Args:
            s: Input string
            start: Start index of the substring
            end: End index of the substring
            
        Returns:
            bool: True if the substring is a palindrome, False otherwise
        """
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def partition_dp(self, s: str) -> List[List[str]]:
        """
        Partition a string using dynamic programming for palindrome checks.
        
        Args:
            s: Input string
            
        Returns:
            List[List[str]]: All possible palindrome partitioning of s
        """
        n = len(s)
        # dp[i][j] = True if s[i:j+1] is a palindrome
        dp = [[False for _ in range(n)] for _ in range(n)]
        
        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True
            
        # Check for palindromes of length 2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                
        # Check for palindromes of length > 2
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i + length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
        
        # Use the precomputed palindrome information for backtracking
        result = []
        self.backtrack_with_dp(result, [], s, 0, dp)
        return result
    
    def backtrack_with_dp(self, result, current, s, start, dp):
        """Helper function for DP-based backtracking."""
        if start == len(s):
            result.append(current[:])
            return
            
        for end in range(start, len(s)):
            if dp[start][end]:
                current.append(s[start:end+1])
                self.backtrack_with_dp(result, current, s, end+1, dp)
                current.pop()


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "aab"
    result1 = solution.partition(s1)
    print(f"Example 1: Partitioning of '{s1}' = {result1}")  # Expected output: [["a","a","b"],["aa","b"]]
    
    # Example 2
    s2 = "a"
    result2 = solution.partition(s2)
    print(f"Example 2: Partitioning of '{s2}' = {result2}")  # Expected output: [["a"]]
    
    # Additional example
    s3 = "abc"
    result3 = solution.partition(s3)
    print(f"Example 3: Partitioning of '{s3}' = {result3}")  # Expected output: [["a","b","c"]]
    
    # Compare with DP approach
    print("\nUsing DP approach:")
    print(f"Example 1: {solution.partition_dp(s1)}")
