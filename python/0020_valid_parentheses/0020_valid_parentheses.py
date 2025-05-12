from typing import List

"""
LeetCode Valid Parentheses

Problem from LeetCode: https://leetcode.com/problems/valid-parentheses/

Description:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
"""

class Solution:
    def is_valid(self, s: str) -> bool:
        """
        Determine if a string of parentheses is valid.
        
        Args:
            s: String containing only parentheses characters
            
        Returns:
            bool: True if the string is valid, False otherwise
        """
        # Initialize a stack to keep track of opening brackets
        stack = []
        
        # Define a mapping of closing brackets to their corresponding opening brackets
        brackets_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        # Iterate through each character in the string
        for char in s:
            # If the character is a closing bracket
            if char in brackets_map:
                # Pop the top element from the stack if it's not empty, otherwise use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the corresponding opening bracket
                if brackets_map[char] != top_element:
                    return False
            # If the character is an opening bracket, push it onto the stack
            else:
                stack.append(char)
        
        # If the stack is empty, all brackets were matched
        return not stack
    
    def is_valid_alternative(self, s: str) -> bool:
        """
        Alternative implementation using a more direct approach.
        
        Args:
            s: String containing only parentheses characters
            
        Returns:
            bool: True if the string is valid, False otherwise
        """
        stack = []
        
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                
                if char == ')' and stack[-1] != '(':
                    return False
                if char == '}' and stack[-1] != '{':
                    return False
                if char == ']' and stack[-1] != '[':
                    return False
                
                stack.pop()
        
        return len(stack) == 0

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "()"
    result1 = solution.is_valid(s1)
    print(f"Example 1: '{s1}' -> {result1}")  # Expected output: True
    
    # Example 2
    s2 = "()[]{}"
    result2 = solution.is_valid(s2)
    print(f"Example 2: '{s2}' -> {result2}")  # Expected output: True
    
    # Example 3
    s3 = "(]"
    result3 = solution.is_valid(s3)
    print(f"Example 3: '{s3}' -> {result3}")  # Expected output: False
    
    # Example 4
    s4 = "([)]"
    result4 = solution.is_valid(s4)
    print(f"Example 4: '{s4}' -> {result4}")  # Expected output: False
    
    # Example 5
    s5 = "{[]}"
    result5 = solution.is_valid(s5)
    print(f"Example 5: '{s5}' -> {result5}")  # Expected output: True
    
    # Compare with alternative implementation
    print("\nUsing alternative implementation:")
    print(f"Example 1: '{s1}' -> {solution.is_valid_alternative(s1)}")
    print(f"Example 3: '{s3}' -> {solution.is_valid_alternative(s3)}")
