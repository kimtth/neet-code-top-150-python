from collections import deque


"""
LeetCode Moving Average From Data Stream

Problem from LeetCode: https://leetcode.com/problems/moving-average-from-data-stream/

Description:
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the MovingAverage class:
- MovingAverage(int size) Initializes the object with the size of the window size.
- double next(int val) Returns the moving average of the last size values of the stream.

Example:
Input:
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
Output:
[null, 1.0, 5.5, 4.66667, 6.0]

Explanation:
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3

Constraints:
1 <= size <= 1000
-10^5 <= val <= 10^5
At most 10^4 calls will be made to next.
"""

class MovingAverage:
    """
    Calculate the moving average of a data stream with a fixed window size.
    """

    def __init__(self, size: int):
        """
        Initialize the MovingAverage with a window size.
        
        Args:
            size: The size of the window for calculating the moving average
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) ->float:
        """
        Calculate the moving average including the new value.
        
        Args:
            val: The new value from the data stream
            
        Returns:
            float: The moving average of the last up to 'size' elements
        """
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0
        self.window_sum = self.window_sum - tail + val
        return self.window_sum / min(self.size, self.count)

    def next_using_list(self, val: int) ->float:
        """
        Alternative implementation using a fixed-size list instead of a deque.
        
        Args:
            val: The new value from the data stream
            
        Returns:
            float: The moving average of the last up to 'size' elements
        """
        if not hasattr(self, 'window'):
            self.window = [0] * self.size
            self.index = 0
            self.sum = 0
            self.count = 0
        self.sum -= self.window[self.index]
        self.window[self.index] = val
        self.sum += val
        self.index = (self.index + 1) % self.size
        self.count = min(self.count + 1, self.size)
        return self.sum / self.count


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    moving_avg = MovingAverage(3)
    
    # Test the deque implementation
    print("Testing deque implementation:")
    print(moving_avg.next(1))    # return 1.0 = 1/1
    print(moving_avg.next(10))   # return 5.5 = (1+10)/2
    print(moving_avg.next(3))    # return 4.66667 = (1+10+3)/3
    print(moving_avg.next(5))    # return 6.0 = (10+3+5)/3
    
    # Test the list implementation
    print("\nTesting list implementation:")
    moving_avg_list = MovingAverage(3)
    print(moving_avg_list.next_using_list(1))    # return 1.0
    print(moving_avg_list.next_using_list(10))   # return 5.5
    print(moving_avg_list.next_using_list(3))    # return 4.66667
    print(moving_avg_list.next_using_list(5))    # return 6.0
