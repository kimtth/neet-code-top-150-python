from typing import List

"""
LeetCode String to Integer (atoi)

Problem from LeetCode: https://leetcode.com/problems/string-to-integer-atoi/

Description:
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:
1. Read in and ignore any leading whitespace.
2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
6. Return the integer as the final result.

Example 1:
Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
Step 2: "42" (no characters read because there is neither a '-' nor '+')
Step 3: "42" ("42" is read in)
The parsed integer is 42.
Since 42 is in the range [-2^31, 2^31 - 1], the final result is 42.

Example 2:
Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
Step 2: "   -42" ('-' is read, so the result should be negative)
Step 3: "   -42" ("42" is read in)
The parsed integer is -42.
Since -42 is in the range [-2^31, 2^31 - 1], the final result is -42.

Example 3:
Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
The parsed integer is 4193.
Since 4193 is in the range [-2^31, 2^31 - 1], the final result is 4193.
"""

class Solution:
    def my_atoi(self, s: str) -> int:
        """
        Convert string to integer according to the atoi algorithm.
        
        Args:
            s: Input string
            
        Returns:
            int: Converted integer clamped to 32-bit signed integer range
        """
        if not s:
            return 0
            
        # Step 1: Read in and ignore any leading whitespace
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
            
        if i == len(s):
            return 0
            
        # Step 2: Check for sign
        sign = 1
        if s[i] == '-' or s[i] == '+':
            sign = -1 if s[i] == '-' else 1
            i += 1
            
        # Step 3 & 4: Read digits and convert to number
        result = 0
        while i < len(s) and s[i].isdigit():
            digit = int(s[i])
            
            # Check for overflow before appending digit
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and digit > 7):
                return 2**31 - 1 if sign == 1 else -2**31
                
            result = result * 10 + digit
            i += 1
            
        # Apply sign and check range
        result *= sign
        
        # Step 5: Clamp the result
        if result < -2**31:
            return -2**31
        if result > 2**31 - 1:
            return 2**31 - 1
            
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "42"
    result1 = solution.my_atoi(s1)
    print(f"Example 1: '{s1}' -> {result1}")  # Expected output: 42
    
    # Example 2
    s2 = "   -42"
    result2 = solution.my_atoi(s2)
    print(f"Example 2: '{s2}' -> {result2}")  # Expected output: -42
    
    # Example 3
    s3 = "4193 with words"
    result3 = solution.my_atoi(s3)
    print(f"Example 3: '{s3}' -> {result3}")  # Expected output: 4193
    
    # Additional examples
    s4 = "words and 987"
    result4 = solution.my_atoi(s4)
    print(f"Example 4: '{s4}' -> {result4}")  # Expected output: 0
    
    s5 = "-91283472332"
    result5 = solution.my_atoi(s5)
    print(f"Example 5: '{s5}' -> {result5}")  # Expected output: -2147483648
