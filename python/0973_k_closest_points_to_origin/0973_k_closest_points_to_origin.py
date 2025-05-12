import heapq
from typing import List


"""
LeetCode K Closest Points To Origin

Problem from LeetCode: https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)² + (y1 - y2)²).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

Example 1:
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4
"""

class Solution:

    def k_closest(self, points: List[List[int]], k: int) ->List[List[int]]:
        """
        Find the k closest points to the origin (0, 0).
        
        Args:
            points: A list of points on the plane
            k: The number of closest points to return
            
        Returns:
            List[List[int]]: The k closest points to the origin
        """
        max_heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(max_heap, (-dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return [point for _, point in max_heap]

    def kClosest_min_heap(self, points: List[List[int]], k: int) ->List[List[int]]:
        """
        Find the k closest points using a min-heap approach.
        
        Args:
            points: A list of points on the plane
            k: The number of closest points to return
            
        Returns:
            List[List[int]]: The k closest points to the origin
        """
        min_heap = [(point[0] ** 2 + point[1] ** 2, point) for point in points]
        heapq.heapify(min_heap)
        return [heapq.heappop(min_heap)[1] for _ in range(k)]

    def kClosest_sorting(self, points: List[List[int]], k: int) ->List[List[int]]:
        """
        Find the k closest points using a sorting approach.
        
        Args:
            points: A list of points on the plane
            k: The number of closest points to return
            
        Returns:
            List[List[int]]: The k closest points to the origin
        """
        points.sort(key=lambda p: p[0] ** 2 + p[1] ** 2)
        return points[:k]

    def kClosest_quickselect(self, points: List[List[int]], k: int) ->List[List[int]]:
        """
        Find the k closest points using quickselect algorithm (O(n) average time).
        
        Args:
            points: A list of points on the plane
            k: The number of closest points to return
            
        Returns:
            List[List[int]]: The k closest points to the origin
        """
        distances = [(point[0] ** 2 + point[1] ** 2, point) for point in points]

        def quickselect(left, right, k_smallest):
            if left == right:
                return
            pivot_idx = partition(left, right)
            if pivot_idx == k_smallest:
                return
            elif pivot_idx < k_smallest:
                quickselect(pivot_idx + 1, right, k_smallest)
            else:
                quickselect(left, pivot_idx - 1, k_smallest)

        def partition(left, right):
            pivot = distances[right][0]
            i = left
            for j in range(left, right):
                if distances[j][0] <= pivot:
                    distances[i], distances[j] = distances[j], distances[i]
                    i += 1
            distances[i], distances[right] = distances[right], distances[i]
            return i
        quickselect(0, len(distances) - 1, k - 1)
        return [point for _, point in distances[:k]]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    points = [[1,3],[-2,2]]
    k = 1
    result = solution.k_closest(points, k)
    print(f"Example 1: {result}")  # Expected: [[-2,2]]
    
    # Example 2
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    result = solution.k_closest(points, k)
    print(f"Example 2: {result}")  # Expected: [[3,3],[-2,4]] or [[-2,4],[3,3]]
