from collections import Counter


"""
LeetCode 169. Majority Element

Problem from LeetCode: https://leetcode.com/problems/majority-element/

Description:
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

class Solution:

    def majority_element(self, nums: list[int]) ->int:
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        majority_entry = None
        for num, count in counts.items():
            if majority_entry is None or count > counts[majority_entry]:
                majority_entry = num
        return majority_entry

    def majorityElement_counter(self, nums: list[int]) ->int:
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement_boyer_moore(self, nums: list[int]) ->int:
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        return candidate


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [3,2,3]
    print(f"Input: nums = {nums1}")
    print(f"Output (basic): {solution.majority_element(nums1)}")  # Expected output: 3
    print(f"Output (Counter): {solution.majorityElement_counter(nums1)}")  # Expected output: 3
    print(f"Output (Boyer-Moore): {solution.majorityElement_boyer_moore(nums1)}")  # Expected output: 3
    
    # Example 2
    nums2 = [2,2,1,1,1,2,2]
    print(f"\nInput: nums = {nums2}")
    print(f"Output (basic): {solution.majority_element(nums2)}")  # Expected output: 2
    print(f"Output (Counter): {solution.majorityElement_counter(nums2)}")  # Expected output: 2
    print(f"Output (Boyer-Moore): {solution.majorityElement_boyer_moore(nums2)}")  # Expected output: 2
