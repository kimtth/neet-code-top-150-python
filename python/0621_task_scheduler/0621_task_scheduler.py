from typing import List
import heapq
from collections import Counter


"""
LeetCode Task Scheduler

Problem from LeetCode: https://leetcode.com/problems/task-scheduler/

Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. 
For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks 
(the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of time that the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.

Example 2:
Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.

Example 3:
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A

Constraints:
- 1 <= task.length <= 10^4
- tasks[i] is upper-case English letter.
- The integer n is in the range [0, 100].
"""

class Solution:

    def least_interval(self, tasks: List[str], n: int) ->int:
        """
        Find the least number of units of time needed to complete all tasks.
        
        Args:
            tasks: List of tasks where each capital letter represents a different task
            n: Minimum units of time between two same tasks
            
        Returns:
            int: The least units of time needed to complete all tasks
        """
        task_counts = Counter(tasks)
        max_heap = [(-count) for count in task_counts.values()]
        heapq.heapify(max_heap)
        time = 0
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    freq = heapq.heappop(max_heap)
                    freq += 1
                    if freq < 0:
                        temp.append(freq)
                else:
                    break
            for freq in temp:
                heapq.heappush(max_heap, freq)
            if max_heap:
                time += n + 1
            else:
                time += len(temp)
        return time

    def leastInterval_math(self, tasks: List[str], n: int) ->int:
        """
        Uses a mathematical formula to calculate the minimum time.
        
        Args:
            tasks: List of tasks represented as capital letters
            n: Minimum units of time between two same tasks
            
        Returns:
            int: The least units of time needed to complete all tasks
        """
        counts = list(Counter(tasks).values())
        max_count = max(counts)
        max_count_occurrences = counts.count(max_count)
        time = (max_count - 1) * (n + 1) + max_count_occurrences
        return max(time, len(tasks))

    def leastInterval_queue(self, tasks: List[str], n: int) ->int:
        """
        Implementation using a queue to track when tasks become available again.
        
        Args:
            tasks: List of tasks represented as capital letters
            n: Minimum units of time between two same tasks
            
        Returns:
            int: The least units of time needed to complete all tasks
        """
        from collections import deque
        frequencies = Counter(tasks)
        sorted_freqs = sorted(frequencies.values(), reverse=True)
        queue = deque([(0, count) for count in sorted_freqs])
        current_time = 0
        while queue:
            next_time, count = queue.popleft()
            current_time = max(current_time, next_time)
            count -= 1
            current_time += 1
            if count > 0:
                queue.append((current_time + n, count))
                queue = deque(sorted(queue, key=lambda x: (x[0], -x[1])))
        return current_time


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    tasks = ["A","A","A","B","B","B"]
    n = 2
    result = solution.least_interval(tasks, n)
    print(f"Example 1: {result}")  # Expected: 8
    
    # Example 2
    tasks = ["A","A","A","B","B","B"]
    n = 0
    result = solution.least_interval(tasks, n)
    print(f"Example 2: {result}")  # Expected: 6
    
    # Example 3
    tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
    n = 2
    result = solution.least_interval(tasks, n)
    print(f"Example 3: {result}")  # Expected: 16
