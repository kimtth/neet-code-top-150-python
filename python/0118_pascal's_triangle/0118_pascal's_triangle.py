from typing import List, Optional

"""
LeetCode 118. Pascal's Triangle

Problem from LeetCode: https://leetcode.com/problems/pascals-triangle/

Description:
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
- 1 <= numRows <= 30
"""

class Solution:

    def generate(self, numRows):
        result = []
        if numRows >= 1:
            result.append([1])
        for row in range(1, numRows):
            current_row = [1]
            prev_row = result[row - 1]
            for j in range(1, row):
                current_row.append(prev_row[j - 1] + prev_row[j])
            current_row.append(1)
            result.append(current_row)
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    numRows = 5
    result = solution.generate(numRows)
    print(f"Input: numRows = {numRows}")
    print(f"Output: {result}")
    # Expected output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    
    # Example 2
    numRows = 1
    result = solution.generate(numRows)
    print(f"Input: numRows = {numRows}")
    print(f"Output: {result}")
    # Expected output: [[1]]
