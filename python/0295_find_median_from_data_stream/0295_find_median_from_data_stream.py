import heapq


"""
LeetCode 295: Find Median from Data Stream

Problem from LeetCode: https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of the list is even, 
there is no middle value, and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be accepted.

Example 1:
Input:
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output:
[null, null, null, 1.5, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr = [1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
- -10^5 <= num <= 10^5
- There will be at least one element in the data structure before calling findMedian.
- At most 5 * 10^4 calls will be made to addNum and findMedian.

Follow up:
- If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
- If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""

class MedianFinder:
    """
    A class that finds the median of a data stream.
    
    Uses two heaps:
    - A max heap for the lower half of the numbers
    - A min heap for the upper half of the numbers
    """

    def __init__(self):
        """
        Initialize data structure.
        """
        self.lo = []
        self.hi = []

    def add_num(self, num: int) ->None:
        """
        Adds a number to the data structure.
        
        Args:
            num: The number to add
        """
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def find_median(self) ->float:
        """
        Returns the median of the current data stream.
        
        Returns:
            float: The median value
        """
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        else:
            return (-self.lo[0] + self.hi[0]) / 2


class MedianFinderSorted:
    """
    Alternative implementation using SortedList.
    More straightforward but less efficient than the heap implementation.
    """

    def __init__(self):
        """
        Initialize data structure.
        """
        from sortedcontainers import SortedList
        self.data = SortedList()

    def add_num(self, num: int) ->None:
        """
        Adds a number to the data structure.
        
        Args:
            num: The number to add
        """
        self.data.add(num)

    def find_median(self) ->float:
        """
        Returns the median of the current data stream.
        
        Returns:
            float: The median value
        """
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            return (self.data[n // 2 - 1] + self.data[n // 2]) / 2


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    medianFinder = MedianFinder()
    medianFinder.add_num(1)
    medianFinder.add_num(2)
    print(medianFinder.find_median())  # Output: 1.5
    medianFinder.add_num(3)
    print(medianFinder.find_median())  # Output: 2.0
    
    # Additional test case
    print("\nTesting with more numbers:")
    medianFinder = MedianFinder()
    for num in [5, 15, 1, 3, 2, 8, 7, 9]:
        medianFinder.add_num(num)
        print(f"After adding {num}, median is {medianFinder.find_median()}")
