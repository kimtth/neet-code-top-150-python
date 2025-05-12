from typing import Dict
from collections import Counter


"""
LeetCode Minimum Window Substring

Problem from LeetCode: https://leetcode.com/problems/minimum-window-substring/

Description:
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window. Since the largest window of s only has one 'a', return empty string.
"""

class Solution:
    def min_window(self, s: str, t: str) -> str:
        """
        Find the minimum window substring of s that contains all characters from t.
        Uses sliding window technique with character frequency counting.
        
        Args:
            s: Source string
            t: Target string
            
        Returns:
            str: Minimum window substring, or empty string if none exists
        """
        if not s or not t:
            return ""
        
        # Count required characters in t
        required = Counter(t)
        required_count = len(required)
        
        # Initialize sliding window variables
        left = 0
        formed = 0  # Count of characters that have met the required frequency
        window_counts = {}
        
        # Initialize minimum window variables
        min_len = float('inf')
        min_window_start = 0
        
        # Iterate through the string with right pointer
        for right in range(len(s)):
            # Add current character to window count
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if the current character contributes to forming required characters
            if char in required and window_counts[char] == required[char]:
                formed += 1
            
            # Try to minimize the window by moving left pointer
            while left <= right and formed == required_count:
                char = s[left]
                
                # Update minimum window if current window is smaller
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    min_window_start = left
                
                # Remove the leftmost character from the window
                window_counts[char] -= 1
                
                # If removing this character breaks the required count
                if char in required and window_counts[char] < required[char]:
                    formed -= 1
                
                # Move left pointer to shrink the window
                left += 1
        
        # If no valid window found
        if min_len == float('inf'):
            return ""
        
        return s[min_window_start:min_window_start + min_len]
    
    def min_window_optimized(self, s: str, t: str) -> str:
        """
        Optimized version that only considers characters in t.
        
        Args:
            s: Source string
            t: Target string
            
        Returns:
            str: Minimum window substring, or empty string if none exists
        """
        if not s or not t:
            return ""
        
        # Dictionary to keep count of characters in t
        dict_t = Counter(t)
        
        # Number of unique characters in t
        required = len(dict_t)
        
        # Dictionary for window characters
        window_counts = {}
        
        # 'formed' keeps track of how many unique characters in t are satisfied
        formed = 0
        
        # Answer variables
        ans = float('inf'), -1, -1  # window_size, left, right
        
        # Initialize pointers
        left = right = 0
        
        while right < len(s):
            # Add the rightmost character to the window
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # Check if adding this character contributes to the required count
            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1
            
            # Try to contract the window
            while left <= right and formed == required:
                char = s[left]
                
                # Update the answer if this window is smaller
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove the leftmost character from the window
                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1, t1 = "ADOBECODEBANC", "ABC"
    result1 = solution.min_window(s1, t1)
    print(f"Example 1: s='{s1}', t='{t1}', result='{result1}'")  # Expected: "BANC"
    
    # Example 2
    s2, t2 = "a", "a"
    result2 = solution.min_window(s2, t2)
    print(f"Example 2: s='{s2}', t='{t2}', result='{result2}'")  # Expected: "a"
    
    # Example 3
    s3, t3 = "a", "aa"
    result3 = solution.min_window(s3, t3)
    print(f"Example 3: s='{s3}', t='{t3}', result='{result3}'")  # Expected: ""
    
    # Compare with optimized approach
    print("\nUsing optimized approach:")
    print(f"Example 1: '{solution.min_window_optimized(s1, t1)}'")  # Expected: "BANC"
    print(f"Example 2: '{solution.min_window_optimized(s2, t2)}'")  # Expected: "a"
    print(f"Example 3: '{solution.min_window_optimized(s3, t3)}'")  # Expected: ""
