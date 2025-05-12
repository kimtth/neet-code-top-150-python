from typing import List


"""
LeetCode Insert Interval

Problem from LeetCode: https://leetcode.com/problems/insert-interval/

Description:
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]
        ) ->List[List[int]]:
        """
        Insert a new interval into a sorted list of non-overlapping intervals, 
        merging overlapping intervals if needed.
        
        Args:
            intervals: A sorted list of non-overlapping intervals
            newInterval: A new interval to be inserted
            
        Returns:
            A new sorted list of non-overlapping intervals
        """
        if not intervals:
            return [newInterval]
        new_start, new_end = newInterval
        result = []
        i = 0
        n = len(intervals)
        while i < n and new_start > intervals[i][0]:
            result.append(intervals[i])
            i += 1
        if not result or result[-1][1] < new_start:
            result.append(newInterval)
        else:
            result[-1][1] = max(result[-1][1], new_end)
        while i < n:
            interval = intervals[i]
            start, end = interval
            i += 1
            if result[-1][1] < start:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], end)
        return result

    def insert_cleaner(self, intervals: List[List[int]], newInterval: List[int]
        ) ->List[List[int]]:
        """
        Alternative implementation with a cleaner approach.
        
        Args:
            intervals: A sorted list of non-overlapping intervals
            newInterval: A new interval to be inserted
            
        Returns:
            A new sorted list of non-overlapping intervals
        """
        result = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        result.append(newInterval)
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    result1 = solution.insert(intervals1, newInterval1)
    print(f"Example 1: {result1}")  # Expected output: [[1, 5], [6, 9]]
    
    # Example 2
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    result2 = solution.insert(intervals2, newInterval2)
    print(f"Example 2: {result2}")  # Expected output: [[1, 2], [3, 10], [12, 16]]
    
    # Additional examples
    intervals3 = []
    newInterval3 = [5, 7]
    result3 = solution.insert(intervals3, newInterval3)
    print(f"Empty intervals test: {result3}")  # Expected output: [[5, 7]]
    
    intervals4 = [[1, 5]]
    newInterval4 = [0, 3]
    result4 = solution.insert(intervals4, newInterval4)
    print(f"Overlap at start: {result4}")  # Expected output: [[0, 5]]
    
    # Compare with cleaner implementation
    print("\nUsing cleaner implementation:")
    print(f"Example 1: {solution.insert_cleaner(intervals1, newInterval1)}")
    print(f"Example 2: {solution.insert_cleaner(intervals2, newInterval2)}")
