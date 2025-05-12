from typing import List

"""
LeetCode Merge Intervals

Problem from LeetCode: https://leetcode.com/problems/merge-intervals/

Description:
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge all overlapping intervals.
        
        Args:
            intervals: Array of intervals where intervals[i] = [starti, endi]
            
        Returns:
            List[List[int]]: Array of merged non-overlapping intervals
        """
        if not intervals:
            return []
        
        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        result = [intervals[0]]  # Start with the first interval
        
        for i in range(1, len(intervals)):
            current = intervals[i]
            prev = result[-1]
            
            # If current interval overlaps with the last merged interval
            if current[0] <= prev[1]:
                # Merge the intervals by updating the end time
                prev[1] = max(prev[1], current[1])
            else:
                # No overlap, add the current interval to the result
                result.append(current)
        
        return result
    
    def merge_in_place(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge intervals with minimal additional space usage.
        
        Args:
            intervals: Array of intervals
            
        Returns:
            List[List[int]]: Array of merged intervals
        """
        if not intervals:
            return []
        
        # Sort by start time
        intervals.sort(key=lambda x: x[0])
        
        i = 0  # Index for the current merged interval
        
        for j in range(1, len(intervals)):
            # If current interval overlaps with the merged one
            if intervals[j][0] <= intervals[i][1]:
                # Merge by updating the end time
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
            else:
                # Move to the next position in the result and copy the current interval
                i += 1
                intervals[i] = intervals[j]
        
        # Return only the merged intervals (from 0 to i inclusive)
        return intervals[:i+1]

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result1 = solution.merge(intervals1)
    print(f"Example 1: {result1}")  # Expected output: [[1, 6], [8, 10], [15, 18]]
    
    # Example 2
    intervals2 = [[1, 4], [4, 5]]
    result2 = solution.merge(intervals2)
    print(f"Example 2: {result2}")  # Expected output: [[1, 5]]
    
    # Additional example
    intervals3 = [[1, 4], [0, 4]]
    result3 = solution.merge(intervals3)
    print(f"Example 3: {result3}")  # Expected output: [[0, 4]]
    
    # Compare with in-place implementation
    print("\nUsing in-place implementation:")
    intervals4 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    result4 = solution.merge_in_place(intervals4)
    print(f"Example 1: {result4}")
