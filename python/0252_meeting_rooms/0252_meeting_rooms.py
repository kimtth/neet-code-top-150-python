from typing import List


"""
LeetCode 252: Meeting Rooms

Problem description (premium problem):

Given an array of meeting time intervals where intervals[i] = [starti, endi], 
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
Explanation: The person cannot attend all meetings because there is an overlap between [0,30] and [5,10].

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: true
Explanation: The person can attend all meetings because they do not overlap.

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= starti < endi <= 10^6
"""

class Solution:

    def can_attend_meetings(self, intervals: List[List[int]]) ->bool:
        """
        Determine if a person could attend all meetings.
        
        Args:
            intervals: List of meeting intervals where intervals[i] = [start_i, end_i]
            
        Returns:
            bool: True if the person can attend all meetings without overlap, False otherwise
        """
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    intervals = [[0, 30], [5, 10], [15, 20]]
    result = solution.can_attend_meetings(intervals)
    print(f"Can attend all meetings in {intervals}: {result}")  # Output: False
    
    # Example 2
    intervals = [[7, 10], [2, 4]]
    result = solution.can_attend_meetings(intervals)
    print(f"Can attend all meetings in {intervals}: {result}")  # Output: True
    
    # Additional example
    intervals = [[1, 3], [3, 6], [6, 8]]
    result = solution.can_attend_meetings(intervals)
    print(f"Can attend all meetings in {intervals}: {result}")  # Output: True
