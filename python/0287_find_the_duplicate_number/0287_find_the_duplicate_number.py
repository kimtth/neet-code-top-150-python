from typing import List


"""
LeetCode 287: Find the Duplicate Number

Problem from LeetCode: https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3

Constraints:
- 1 <= n <= 10^5
- nums.length == n + 1
- 1 <= nums[i] <= n
- All the integers in nums appear only once except for precisely one integer which appears two or more times.

Follow up:
- How can we prove that at least one duplicate number must exist in nums?
- Can you solve the problem in linear runtime complexity?
"""

class Solution:

    def find_duplicate(self, nums: List[int]) ->int:
        """
        Find the duplicate number in an array using Floyd's Tortoise and Hare (Cycle Detection).
        
        This algorithm uses O(1) extra space and doesn't modify the array.
        
        Args:
            nums: Array of integers where each integer is in the range [1, n] inclusive
            
        Returns:
            int: The duplicate number
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

    def find_duplicate_using_set(self, nums: List[int]) ->int:
        """
        Find the duplicate number using a set.
        
        This algorithm uses O(n) extra space.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: The duplicate number
        """
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

    def find_duplicate_using_binary_search(self, nums: List[int]) ->int:
        """
        Find the duplicate number using binary search.
        
        This algorithm uses O(1) extra space and doesn't modify the array.
        
        Args:
            nums: Array of integers
            
        Returns:
            int: The duplicate number
        """
        low = 1
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            if count > mid:
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums = [1, 3, 4, 2, 2]
    result = solution.find_duplicate(nums)
    print(f"Duplicate in {nums}: {result}")  # Output: 2
    
    # Example 2
    nums = [3, 1, 3, 4, 2]
    result = solution.find_duplicate(nums)
    print(f"Duplicate in {nums}: {result}")  # Output: 3
    
    # Test different methods
    nums = [2, 5, 9, 6, 9, 3, 8, 9, 7, 1]
    result1 = solution.find_duplicate(nums)
    result2 = solution.find_duplicate_using_set(nums)
    result3 = solution.find_duplicate_using_binary_search(nums)
    print(f"Duplicate using Floyd's cycle detection: {result1}")
    print(f"Duplicate using set: {result2}")
    print(f"Duplicate using binary search: {result3}")
