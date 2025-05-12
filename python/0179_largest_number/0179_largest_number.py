from functools import cmp_to_key


"""
LeetCode 179. Largest Number

Problem from LeetCode: https://leetcode.com/problems/largest-number/

Description:
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 10^9
"""

class Solution:

    def largest_number(self, nums: list[int]) ->str:
        nums_as_strs = [str(num) for num in nums]

        def compare(a, b):
            order1 = a + b
            order2 = b + a
            if order2 > order1:
                return 1
            elif order2 < order1:
                return -1
            else:
                return 0
        nums_as_strs.sort(key=cmp_to_key(compare))
        if nums_as_strs[0] == '0':
            return '0'
        return ''.join(nums_as_strs)


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [10, 2]
    result1 = solution.largest_number(nums1)
    print(f"Input: nums = {nums1}")
    print(f"Output: \"{result1}\"")  # Expected output: "210"
    
    # Example 2
    nums2 = [3, 30, 34, 5, 9]
    result2 = solution.largest_number(nums2)
    print(f"Input: nums = {nums2}")
    print(f"Output: \"{result2}\"")  # Expected output: "9534330"
