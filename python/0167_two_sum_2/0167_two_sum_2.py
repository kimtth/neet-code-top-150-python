from typing import List, Optional

"""
LeetCode Two Sum II - Input Array Is Sorted

Problem from LeetCode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Description:
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
"""

class Solution:

    def two_sum(self, numbers: list[int], target: int) ->list[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum > target:
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return None


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    numbers1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.two_sum(numbers1, target1)
    print(f"Example 1: {result1}")  # Expected output: [1, 2]
    
    # Example 2
    numbers2 = [2, 3, 4]
    target2 = 6
    result2 = solution.two_sum(numbers2, target2)
    print(f"Example 2: {result2}")  # Expected output: [1, 3]
    
    # Example 3
    numbers3 = [-1, 0]
    target3 = -1
    result3 = solution.two_sum(numbers3, target3)
    print(f"Example 3: {result3}")  # Expected output: [1, 2]
