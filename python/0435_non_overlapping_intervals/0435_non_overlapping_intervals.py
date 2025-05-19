from typing import List


"""
LeetCode Non-Overlapping Intervals

Problem from LeetCode: https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
    Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
    Output: 1
    Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
    Input: intervals = [[1,2],[1,2],[1,2]]
    Output: 2
    Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
    Input: intervals = [[1,2],[2,3]]
    Output: 0
    Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
    1 <= intervals.length <= 10^5
    intervals[i].length == 2
    -5 * 10^4 <= starti < endi <= 5 * 10^4
"""

class Solution:

    def erase_overlap_intervals(self, intervals: List[List[int]]) ->int:
        """
        Return the minimum number of intervals to remove to make the rest
        of the intervals non-overlapping.
        
        Args:
            intervals: A list of interval pairs where intervals[i] = [start_i, end_i]
            
        Returns:
            int: The minimum number of intervals you need to remove
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        prev = 0
        count = 0
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[prev][1] > intervals[i][1]:
                    prev = i
                count += 1
            else:
                prev = i
        return count

    def eraseOverlapIntervals_end_sort(self, intervals: List[List[int]]) ->int:
        """
        Alternative approach sorting by end time.
        
        Args:
            intervals: A list of interval pairs where intervals[i] = [start_i, end_i]
            
        Returns:
            int: The minimum number of intervals you need to remove
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        count = 0
        end = float('-inf')
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
                count += 1
        return len(intervals) - count

    def eraseOverlapIntervals_greedy(self, intervals: List[List[int]]) ->int:
        """
        Greedy approach removing minimum number of intervals.
        
        Args:
            intervals: A list of interval pairs where intervals[i] = [start_i, end_i]
            
        Returns:
            int: The minimum number of intervals you need to remove
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[1])
        non_overlap_count = 1
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                non_overlap_count += 1
                end = intervals[i][1]
        return len(intervals) - non_overlap_count


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1: intervals = [[1,2],[2,3],[3,4],[1,3]]
    print("Example 1:")
    result = solution.erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]])
    print(f"Output: {result}")  # Expected: 1
    
    # Example 2: intervals = [[1,2],[1,2],[1,2]]
    print("\nExample 2:")
    result = solution.erase_overlap_intervals([[1,2],[1,2],[1,2]])
    print(f"Output: {result}")  # Expected: 2
    
    # Example 3: intervals = [[1,2],[2,3]]
    print("\nExample 3:")
    result = solution.erase_overlap_intervals([[1,2],[2,3]])
    print(f"Output: {result}")  # Expected: 0
    
    # Test with alternative implementations
    print("\nAlternative implementations:")
    print("End sort approach:", solution.eraseOverlapIntervals_end_sort([[1,2],[2,3],[3,4],[1,3]]))
    print("Greedy approach:", solution.eraseOverlapIntervals_greedy([[1,2],[2,3],[3,4],[1,3]]))
