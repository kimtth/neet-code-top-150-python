import heapq


"""
LeetCode Min Cost To Connect All Points

Problem from LeetCode: https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, 
where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

Example 1:
Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation: 
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:
Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
- 1 <= points.length <= 1000
- -10^6 <= xi, yi <= 10^6
- All pairs (xi, yi) are distinct.
"""

class Solution:

    def min_cost_connect_points(self, points: list[list[int]]) ->int:
        n = len(points)
        pq = [(0, 0)]
        in_mst = [False] * n
        min_cost = 0
        points_connected = 0
        while points_connected < n:
            distance, curr_index = heapq.heappop(pq)
            if in_mst[curr_index]:
                continue
            in_mst[curr_index] = True
            min_cost += distance
            points_connected += 1
            for next_index in range(n):
                if not in_mst[next_index]:
                    next_distance = abs(points[curr_index][0] - points[
                        next_index][0]) + abs(points[curr_index][1] -
                        points[next_index][1])
                    heapq.heappush(pq, (next_distance, next_index))
        return min_cost


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    result = solution.min_cost_connect_points(points)
    print(f"Example 1: {result}")  # Expected: 20
    
    # Example 2
    points = [[3,12],[-2,5],[-4,1]]
    result = solution.min_cost_connect_points(points)
    print(f"Example 2: {result}")  # Expected: 18
