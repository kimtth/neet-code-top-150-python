from typing import List, Optional

"""
LeetCode Word Break

Problem from LeetCode: https://leetcode.com/problems/word-break/

Description:
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
"""

class Solution:
    def word_break(self, s: str, wordDict: List[str]) -> bool:
        """
        Determine if a string can be segmented into words from the dictionary.
        Uses dynamic programming approach.
        
        Args:
            s: String to break
            wordDict: Dictionary of valid words
            
        Returns:
            bool: True if s can be broken into words from wordDict, False otherwise
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        word_set = set(wordDict)
        for i in range(1, len(s) + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]
    
    def word_break_recursive(self, s: str, wordDict: List[str]) -> bool:
        """
        Recursive solution with memoization.
        
        Args:
            s: String to break
            wordDict: Dictionary of valid words
            
        Returns:
            bool: True if s can be broken into words from wordDict, False otherwise
        """
        word_set = set(wordDict)
        memo = {}
        
        def can_break(start):
            if start == len(s):
                return True
                
            if start in memo:
                return memo[start]
                
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set and can_break(end):
                    memo[start] = True
                    return True
                    
            memo[start] = False
            return False
            
        return can_break(0)
    
    def word_break_bfs(self, s: str, wordDict: List[str]) -> bool:
        """
        BFS approach to check if the string can be segmented.
        
        Args:
            s: String to break
            wordDict: Dictionary of valid words
            
        Returns:
            bool: True if s can be broken into words from wordDict, False otherwise
        """
        word_set = set(wordDict)
        queue = [0]
        visited = set()
        
        while queue:
            start = queue.pop(0)
            if start in visited:
                continue
                
            visited.add(start)
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in word_set:
                    if end == len(s):
                        return True
                    queue.append(end)
                    
        return False


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    result1 = solution.word_break(s1, wordDict1)
    print(f"Example 1: s='{s1}', wordDict={wordDict1} -> {result1}")  # Expected output: True
    
    # Example 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    result2 = solution.word_break(s2, wordDict2)
    print(f"Example 2: s='{s2}', wordDict={wordDict2} -> {result2}")  # Expected output: True
    
    # Example 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    result3 = solution.word_break(s3, wordDict3)
    print(f"Example 3: s='{s3}', wordDict={wordDict3} -> {result3}")  # Expected output: False
    
    # Compare with recursive approach
    print("\nUsing recursive approach:")
    print(f"Example 1: {solution.word_break_recursive(s1, wordDict1)}")
    print(f"Example 2: {solution.word_break_recursive(s2, wordDict2)}")
    print(f"Example 3: {solution.word_break_recursive(s3, wordDict3)}")
    
    # Compare with BFS approach
    print("\nUsing BFS approach:")
    print(f"Example 1: {solution.word_break_bfs(s1, wordDict1)}")
    print(f"Example 2: {solution.word_break_bfs(s2, wordDict2)}")
    print(f"Example 3: {solution.word_break_bfs(s3, wordDict3)}")
