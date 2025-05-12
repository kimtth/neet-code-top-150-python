from typing import List

"""
LeetCode Longest Common Prefix

Problem from LeetCode: https://leetcode.com/problems/longest-common-prefix/

Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        """
        Find the longest common prefix string amongst an array of strings.
        
        Args:
            strs: Array of strings
            
        Returns:
            str: Longest common prefix, or empty string if no common prefix exists
        """
        if not strs:
            return ""
            
        # Start with the first string as the prefix
        prefix = strs[0]
        
        # Compare prefix with each string in the array
        for i in range(1, len(strs)):
            # Keep reducing the prefix until it's a prefix of the current string
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                    
        return prefix
    
    def longest_common_prefix_vertical(self, strs: List[str]) -> str:
        """
        Find the longest common prefix using vertical scanning approach.
        
        Args:
            strs: Array of strings
            
        Returns:
            str: Longest common prefix
        """
        if not strs:
            return ""
            
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Compare the character at position i in all strings
            for j in range(1, len(strs)):
                # If we've reached the end of a string or characters don't match
                if i >= len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        # If we get here, the entire first string is a prefix
        return strs[0]
    
    def longest_common_prefix_divide_conquer(self, strs: List[str]) -> str:
        """
        Find the longest common prefix using divide and conquer approach.
        
        Args:
            strs: Array of strings
            
        Returns:
            str: Longest common prefix
        """
        if not strs:
            return ""
            
        def common_prefix(left: str, right: str) -> str:
            """Find common prefix of two strings."""
            min_len = min(len(left), len(right))
            for i in range(min_len):
                if left[i] != right[i]:
                    return left[:i]
            return left[:min_len]
            
        def divide_and_conquer(start: int, end: int) -> str:
            """Apply divide and conquer to find common prefix."""
            if start == end:
                return strs[start]
                
            mid = (start + end) // 2
            left_prefix = divide_and_conquer(start, mid)
            right_prefix = divide_and_conquer(mid + 1, end)
            
            return common_prefix(left_prefix, right_prefix)
            
        return divide_and_conquer(0, len(strs) - 1)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    strs1 = ["flower", "flow", "flight"]
    result1 = solution.longest_common_prefix(strs1)
    print(f"Example 1: {strs1} -> '{result1}'")  # Expected output: "fl"
    
    # Example 2
    strs2 = ["dog", "racecar", "car"]
    result2 = solution.longest_common_prefix(strs2)
    print(f"Example 2: {strs2} -> '{result2}'")  # Expected output: ""
    
    # Additional example
    strs3 = ["hello", "heaven", "heavy"]
    result3 = solution.longest_common_prefix(strs3)
    print(f"Example 3: {strs3} -> '{result3}'")  # Expected output: "he"
    
    # Compare approaches
    print("\nComparing different approaches:")
    print(f"Horizontal scanning: '{solution.longest_common_prefix(strs1)}'")
    print(f"Vertical scanning: '{solution.longest_common_prefix_vertical(strs1)}'")
    print(f"Divide and conquer: '{solution.longest_common_prefix_divide_conquer(strs1)}'")
