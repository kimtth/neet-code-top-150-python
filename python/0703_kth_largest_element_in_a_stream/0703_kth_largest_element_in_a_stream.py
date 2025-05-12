import heapq
from typing import List


"""
LeetCode Kth Largest Element In A Stream

Problem from LeetCode: https://leetcode.com/problems/kth-largest-element-in-a-stream/

Description:
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
- KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
- int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example 1:
Input:
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output:
[null, 4, 5, 5, 8, 8]

Explanation:
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

Constraints:
1 <= k <= 10^4
0 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
-10^4 <= val <= 10^4
At most 10^4 calls will be made to add.
It is guaranteed that there will be at least k elements in the array when you search for the kth element.
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Initialize the K-th largest element finder with the value k and initial elements.
        
        Args:
            k: The k value for finding the kth largest element
            nums: Array of initial numbers
        """
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)

    def add(self, val: int) ->int:
        """
        Add a new value to the stream and return the k-th largest.
        
        Args:
            val: The value to add to the stream
            
        Returns:
            int: The k-th largest element in the stream
        """
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif val > self.min_heap[0]:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0] if self.min_heap else None


class KthLargestAlternative:

    def __init__(self, k: int, nums: List[int]):
        """
        Alternative implementation using heapq.nlargest.
        
        Args:
            k: The k value for finding the kth largest element
            nums: Array of initial numbers
        """
        self.k = k
        self.heap = []
        self.nums = nums
        self.heap = heapq.nlargest(k, nums + [float('-inf')])
        heapq._heapify_max(self.heap)

    def add(self, val: int) ->int:
        """
        Add a new value to the stream and return the k-th largest.
        
        Args:
            val: The value to add to the stream
            
        Returns:
            int: The k-th largest element in the stream
        """
        self.nums.append(val)
        self.heap = heapq.nlargest(self.k, self.nums)
        return self.heap[-1] if len(self.heap) >= self.k else None


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    
    # Add elements and get the kth largest
    print(kthLargest.add(3))    # Expected: 4
    print(kthLargest.add(5))    # Expected: 5
    print(kthLargest.add(10))   # Expected: 5
    print(kthLargest.add(9))    # Expected: 8
    print(kthLargest.add(4))    # Expected: 8
    
    # Test the alternative implementation
    print("\nTesting alternative implementation:")
    kthLargestAlt = KthLargestAlternative(3, [4, 5, 8, 2])
    
    # Add elements and get the kth largest
    print(kthLargestAlt.add(3))    # Expected: 4
    print(kthLargestAlt.add(5))    # Expected: 5
    print(kthLargestAlt.add(10))   # Expected: 5
    print(kthLargestAlt.add(9))    # Expected: 8
    print(kthLargestAlt.add(4))    # Expected: 8
