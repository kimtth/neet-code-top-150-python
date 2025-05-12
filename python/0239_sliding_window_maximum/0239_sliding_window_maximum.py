from typing import List
from collections import deque


"""
LeetCode 239: Sliding Window Maximum

Problem from LeetCode: https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums, there is a sliding window of size k which 
is moving from the very left of the array to the very right. You can only see the 
k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

class Solution:

    def max_sliding_window(self, nums: List[int], k: int) ->List[int]:
        """
        Return the maximum element in each sliding window of size k.
        
        Args:
            nums: Array of integers
            k: Size of the sliding window
            
        Returns:
            List[int]: Maximum elements in each sliding window
        """
        if not nums or k <= 0:
            return []
        n = len(nums)
        result = []
        dq = deque()
        for i in range(n):
            while dq and dq[0] < i - k + 1:
                dq.popleft()
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                result.append(nums[dq[0]])
        return result

    def max_sliding_window_naive(self, nums: List[int], k: int) ->List[int]:
        """
        Return the maximum element in each sliding window using a naive approach.
        Time complexity: O(n*k)
        
        Args:
            nums: Array of integers
            k: Size of the sliding window
            
        Returns:
            List[int]: Maximum elements in each sliding window
        """
        n = len(nums)
        if n == 0 or k <= 0:
            return []
        result = []
        for i in range(n - k + 1):
            max_val = max(nums[i:i + k])
            result.append(max_val)
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = solution.max_sliding_window(nums, k)
    print(result)  # Output: [3, 3, 5, 5, 6, 7]
    
    nums = [1]
    k = 1
    result = solution.max_sliding_window(nums, k)
    print(result)  # Output: [1]
