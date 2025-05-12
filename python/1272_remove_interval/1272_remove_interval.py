from typing import List

"""
LeetCode Remove Interval

Problem from LeetCode: https://leetcode.com/problems/remove-interval/

Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] 
represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

Example 1:
    Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
    Output: [[0,1],[6,7]]
    Explanation: After removing the intersection of [1,6] with the intervals, 
    we are left with [0,1] and [6,7].

Example 2:
    Input: intervals = [[0,5]], toBeRemoved = [2,3]
    Output: [[0,2],[3,5]]
    Explanation: After removing the intersection of [2,3] with the intervals, 
    we are left with [0,2] and [3,5].

Constraints:
    1 <= intervals.length <= 10^4
    -10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
    intervals[i][0] < intervals[i][1]
    intervals are pairwise disjoint.
    -10^9 <= toBeRemoved[0] < toBeRemoved[1] <= 10^9
"""

class Solution:
    def remove_interval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        result = []
        for interval in intervals:
            if interval[0] > toBeRemoved[1] or interval[1] < toBeRemoved[0]:
                result.append([interval[0], interval[1]])
            else:
                if interval[0] < toBeRemoved[0]:
                    result.append([interval[0], toBeRemoved[0]])
                if interval[1] > toBeRemoved[1]:
                    result.append([toBeRemoved[1], interval[1]])
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    intervals1 = [[0,2],[3,4],[5,7]]
    toBeRemoved1 = [1,6]
    result1 = solution.remove_interval(intervals1, toBeRemoved1)
    print(f"Example 1: {result1}")  # Output: [[0,1],[6,7]]
    
    # Example 2
    intervals2 = [[0,5]]
    toBeRemoved2 = [2,3]
    result2 = solution.remove_interval(intervals2, toBeRemoved2)
    print(f"Example 2: {result2}")  # Output: [[0,2],[3,5]]
