from typing import List
import heapq


"""
LeetCode Meeting Rooms II

Problem from LeetCode: https://leetcode.com/problems/meeting-rooms-ii/

Description:
Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: 1
"""

class Solution:

    def min_meeting_rooms(self, intervals: List[List[int]]) ->int:
        """
        Find the minimum number of meeting rooms required.
        
        Args:
            intervals: List of meeting intervals where intervals[i] = [start_i, end_i]
            
        Returns:
            int: Minimum number of meeting rooms required
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= rooms[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)

    def min_meeting_rooms_two_pointer(self, intervals: List[List[int]]) ->int:
        """
        Find the minimum number of meeting rooms required using two pointers.
        
        Args:
            intervals: List of meeting intervals where intervals[i] = [start_i, end_i]
            
        Returns:
            int: Minimum number of meeting rooms required
        """
        if not intervals:
            return 0
        start_times = [interval[0] for interval in intervals]
        end_times = [interval[1] for interval in intervals]
        start_times.sort()
        end_times.sort()
        start_ptr = 0
        end_ptr = 0
        result = 0
        while start_ptr < len(start_times):
            if start_times[start_ptr] >= end_times[end_ptr]:
                result -= 1
                end_ptr += 1
            result += 1
            start_ptr += 1
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    result1 = solution.min_meeting_rooms(intervals1)
    print(f"Example 1: {result1}")  # Expected output: 2
    
    # Example 2
    intervals2 = [[7, 10], [2, 4]]
    result2 = solution.min_meeting_rooms(intervals2)
    print(f"Example 2: {result2}")  # Expected output: 1
