from typing import List

"""
LeetCode Zigzag Conversion

Problem from LeetCode: https://leetcode.com/problems/zigzag-conversion/

Description:
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows.

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Convert a string into a zigzag pattern and return the result read line by line.
        
        Args:
            s: Input string
            numRows: Number of rows for the zigzag pattern
            
        Returns:
            str: Zigzag converted string
        """
        # Handle edge cases
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Initialize rows
        rows = [''] * numRows
        
        # Variables to track current direction and row
        index = 0
        step = 1
        
        # Traverse through the string
        for char in s:
            # Add current character to the current row
            rows[index] += char
            
            # Change direction if we reach the first or last row
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
                
            # Move to the next row
            index += step
            
        # Combine all rows into a single string
        return ''.join(rows)

    def convert_simulation(self, s: str, numRows: int) -> str:
        """
        Alternative implementation that uses a more visual approach.
        
        Args:
            s: Input string
            numRows: Number of rows for the zigzag pattern
            
        Returns:
            str: Zigzag converted string
        """
        if numRows == 1 or numRows >= len(s):
            return s
        
        # Calculate the cycle length
        cycle_len = 2 * numRows - 2
        result = []
        
        for i in range(numRows):
            for j in range(i, len(s), cycle_len):
                # Add the character at the current position
                result.append(s[j])
                
                # Add the character at the corresponding position in the same cycle
                # This is only applicable for rows other than the first and last
                if i != 0 and i != numRows - 1 and j + cycle_len - 2 * i < len(s):
                    result.append(s[j + cycle_len - 2 * i])
                    
        return ''.join(result)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    result1 = solution.convert(s1, numRows1)
    print(f"Example 1: '{s1}' with {numRows1} rows -> '{result1}'")  # Expected: "PAHNAPLSIIGYIR"
    
    # Example 2
    s2 = "PAYPALISHIRING"
    numRows2 = 4
    result2 = solution.convert(s2, numRows2)
    print(f"Example 2: '{s2}' with {numRows2} rows -> '{result2}'")  # Expected: "PINALSIGYAHRPI"
    
    # Example 3
    s3 = "A"
    numRows3 = 1
    result3 = solution.convert(s3, numRows3)
    print(f"Example 3: '{s3}' with {numRows3} rows -> '{result3}'")  # Expected: "A"
