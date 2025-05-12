from typing import List
import heapq
from collections import Counter


"""
LeetCode Top K Frequent Elements

Problem from LeetCode: https://leetcode.com/problems/top-k-frequent-elements/

Description:
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution:

    def top_k_frequent(self, nums: List[int], k: int) ->List[int]:
        """
        Find the k most frequent elements in the array.
        
        Args:
            nums: Array of integers
            k: Number of most frequent elements to return
            
        Returns:
            List[int]: The k most frequent elements
        """
        if k == len(nums):
            return nums
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result[::-1]

    def topKFrequent_counter(self, nums: List[int], k: int) ->List[int]:
        """
        Find the k most frequent elements using Counter's most_common method.
        
        Args:
            nums: Array of integers
            k: Number of most frequent elements to return
            
        Returns:
            List[int]: The k most frequent elements
        """
        count = Counter(nums)
        return [num for num, _ in count.most_common(k)]

    def topKFrequent_bucket_sort(self, nums: List[int], k: int) ->List[int]:
        """
        Find the k most frequent elements using bucket sort approach.
        
        Args:
            nums: Array of integers
            k: Number of most frequent elements to return
            
        Returns:
            List[int]: The k most frequent elements
        """
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        freq = [[] for _ in range(len(nums) + 1)]
        for num, count in count.items():
            freq[count].append(num)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return []


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1 = solution.top_k_frequent(nums1, k1)
    print(f"Example 1: {result1}")  # Expected output: [1, 2]
    
    # Example 2
    nums2 = [1]
    k2 = 1
    result2 = solution.top_k_frequent(nums2, k2)
    print(f"Example 2: {result2}")  # Expected output: [1]
    
    # Additional example
    nums3 = [4, 1, 4, 2, 2, 4, 3, 1, 4, 2]
    k3 = 3
    result3 = solution.top_k_frequent(nums3, k3)
    print(f"Example 3: {result3}")  # Expected output: [4, 2, 1]
    
    # Testing different implementations
    print("\nUsing Counter:")
    result4 = solution.topKFrequent_counter(nums1, k1)
    print(f"Example 1: {result4}")  # Expected output: [1, 2]
    
    print("\nUsing Bucket Sort:")
    result5 = solution.topKFrequent_bucket_sort(nums1, k1)
    print(f"Example 1: {result5}")  # Expected output: [1, 2]
