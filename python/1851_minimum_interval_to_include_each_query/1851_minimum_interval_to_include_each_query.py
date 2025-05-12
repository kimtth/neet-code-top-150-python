import heapq
from typing import List


"""
LeetCode Minimum Interval To Include Each Query

Problem from LeetCode: https://leetcode.com/problems/minimum-interval-to-include-each-query/

You are given a 2D integer array intervals, where intervals[i] = [lefti, righti] 
describes the ith interval starting at lefti and ending at righti (inclusive). 
The size of an interval is defined as the number of integers it contains, or more 
formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth query is the 
size of the smallest interval i such that lefti <= queries[j] <= righti. If no 
such interval exists, the answer is -1.

Return an array containing the answers to the queries.

Example 1:
    Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
    Output: [3,3,1,4]
    Explanation: The queries are processed as follows:
    - Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
    - Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
    - Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
    - Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.

Example 2:
    Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
    Output: [2,-1,4,6]
    Explanation: The queries are processed as follows:
    - Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
    - Query = 19: None of the intervals contain 19. The answer is -1.
    - Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
    - Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.

Constraints:
    1 <= intervals.length <= 10^5
    1 <= queries.length <= 10^5
    intervals[i].length == 2
    1 <= lefti <= righti <= 10^7
    1 <= queries[j] <= 10^7
"""

class Solution:
    def min_interval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(queries)
        result = [-1] * n
        query_indices = [(queries[i], i) for i in range(n)]
        query_indices.sort()
        intervals.sort()
        min_heap = []
        interval_idx = 0
        for query, original_idx in query_indices:
            while interval_idx < len(intervals) and intervals[interval_idx][0
                ] <= query:
                start, end = intervals[interval_idx]
                if end >= query:
                    heapq.heappush(min_heap, (end - start + 1, end))
                interval_idx += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)
            if min_heap:
                result[original_idx] = min_heap[0][0]
        return result


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    intervals1 = [[1,4],[2,4],[3,6],[4,4]]
    queries1 = [2,3,4,5]
    result1 = solution.min_interval(intervals1, queries1)
    print(f"Example 1: {result1}")  # Output: [3,3,1,4]
    
    # Example 2
    intervals2 = [[2,3],[2,5],[1,8],[20,25]]
    queries2 = [2,19,5,22]
    result2 = solution.min_interval(intervals2, queries2)
    print(f"Example 2: {result2}")  # Output: [2,-1,4,6]
