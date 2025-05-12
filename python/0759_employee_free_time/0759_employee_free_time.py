from typing import List
import heapq


"""
LeetCode Employee Free Time

Problem from LeetCode: https://leetcode.com/problems/employee-free-time/

Description:
We are given a list schedule of employees, which represents the working time for each employee.
Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.
Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

Example 1:
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:
Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]

Constraints:
1 <= schedule.length <= 50
0 <= schedule[i].length <= 50
0 <= schedule[i][j].start < schedule[i][j].end <= 10^8
"""

class Interval:

    def __init__(self, start: int=None, end: int=None):
        self.start = start
        self.end = end


class Solution:

    def employee_free_time(self, schedule: List[List[Interval]]) ->List[
        Interval]:
        """
        Finds the free time intervals that are common to all employees.
        
        Args:
            schedule: A list where schedule[i] is a list of Interval objects for the ith employee
            
        Returns:
            List[Interval]: The common free time intervals for all employees
        """
        intervals = []
        for employee_schedule in schedule:
            for interval in employee_schedule:
                intervals.append(interval)
        intervals.sort(key=lambda x: x.start)
        result = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev.end < curr.start:
                result.append(Interval(prev.end, curr.start))
                prev = curr
            else:
                prev.end = max(prev.end, curr.end)
        return result

    def employeeFreeTime_priority_queue(self, schedule: List[List[Interval]]
        ) ->List[Interval]:
        """
        Uses a priority queue to efficiently find common free time intervals.
        
        Args:
            schedule: A list where schedule[i] is a list of Interval objects for the ith employee
            
        Returns:
            List[Interval]: The common free time intervals for all employees
        """
        all_intervals = []
        for employee in schedule:
            for interval in employee:
                all_intervals.append((interval.start, interval.end))
        if not all_intervals:
            return []
        heapq.heapify(all_intervals)
        result = []
        prev_start, prev_end = heapq.heappop(all_intervals)
        while all_intervals:
            curr_start, curr_end = heapq.heappop(all_intervals)
            if prev_end < curr_start:
                result.append(Interval(prev_end, curr_start))
                prev_start, prev_end = curr_start, curr_end
            else:
                prev_end = max(prev_end, curr_end)
        return result

    def employeeFreeTime_line_sweep(self, schedule: List[List[Interval]]
        ) ->List[Interval]:
        """
        Uses a line sweep algorithm to find common free time intervals.
        
        Args:
            schedule: A list where schedule[i] is a list of Interval objects for the ith employee
            
        Returns:
            List[Interval]: The common free time intervals for all employees
        """
        events = []
        for employee in schedule:
            for interval in employee:
                events.append((interval.start, 1))
                events.append((interval.end, -1))
        events.sort()
        result = []
        balance = 0
        prev_time = None
        for time, event_type in events:
            if balance == 0 and prev_time is not None:
                result.append(Interval(prev_time, time))
            balance += event_type
            prev_time = time
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    # Create intervals for each employee
    employee1 = [Interval(1, 2), Interval(5, 6)]
    employee2 = [Interval(1, 3)]
    employee3 = [Interval(4, 10)]
    schedule1 = [employee1, employee2, employee3]
    
    result1 = solution.employee_free_time(schedule1)
    print("Example 1 Free Time Intervals:")
    for interval in result1:
        print(f"[{interval.start}, {interval.end}]")  # Expected: [3, 4]
    
    # Example 2
    employee1 = [Interval(1, 3), Interval(6, 7)]
    employee2 = [Interval(2, 4)]
    employee3 = [Interval(2, 5), Interval(9, 12)]
    schedule2 = [employee1, employee2, employee3]
    
    result2 = solution.employee_free_time(schedule2)
    print("\nExample 2 Free Time Intervals:")
    for interval in result2:
        print(f"[{interval.start}, {interval.end}]")  # Expected: [5, 6], [7, 9]
