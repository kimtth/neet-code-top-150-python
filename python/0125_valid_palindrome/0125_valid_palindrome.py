from typing import List

"""
LeetCode Valid Palindrome

Problem from LeetCode: https://leetcode.com/problems/valid-palindrome/

Description:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

class Solution:
    def is_palindrome(self, s: str) -> bool:
        """
        Determine if a string is a palindrome after cleaning.
        
        Args:
            s: Input string
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        # Convert to lowercase and filter out non-alphanumeric characters
        filtered = [c.lower() for c in s if c.isalnum()]
        
        # Check if the filtered string is a palindrome
        left, right = 0, len(filtered) - 1
        
        while left < right:
            if filtered[left] != filtered[right]:
                return False
            left += 1
            right -= 1
            
        return True
    
    def is_palindrome_pythonic(self, s: str) -> bool:
        """
        More concise implementation using Python's built-in methods.
        
        Args:
            s: Input string
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        # Filter out non-alphanumeric characters and convert to lowercase
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        
        # Check if the string is equal to its reverse
        return filtered == filtered[::-1]
    
    def is_palindrome_two_pointers(self, s: str) -> bool:
        """
        Implementation using two pointers without creating a new string.
        More memory efficient.
        
        Args:
            s: Input string
            
        Returns:
            bool: True if the string is a palindrome, False otherwise
        """
        left, right = 0, len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1
                
            # Skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare characters (case-insensitive)
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "A man, a plan, a canal: Panama"
    result1 = solution.is_palindrome(s1)
    print(f"Example 1: '{s1}' -> {result1}")  # Expected output: True
    
    # Example 2
    s2 = "race a car"
    result2 = solution.is_palindrome(s2)
    print(f"Example 2: '{s2}' -> {result2}")  # Expected output: False
    
    # Example 3
    s3 = " "
    result3 = solution.is_palindrome(s3)
    print(f"Example 3: '{s3}' -> {result3}")  # Expected output: True
    
    # Compare implementations
    print("\nComparing different implementations:")
    print(f"Pythonic approach: '{s1}' -> {solution.is_palindrome_pythonic(s1)}")
    print(f"Two-pointer approach: '{s1}' -> {solution.is_palindrome_two_pointers(s1)}")
