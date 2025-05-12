from typing import List
from collections import defaultdict


"""
LeetCode Detect Squares

Problem from LeetCode: https://leetcode.com/problems/detect-squares/

You are given a stream of points on the X-Y plane. Design an algorithm that:

- Adds new points from the stream into a data structure. Duplicate points are allowed 
  and should be treated as different points.
- Given a query point, counts the number of ways to choose three points from the data 
  structure such that the three points and the query point form an axis-aligned square 
  with positive area.

An axis-aligned square is a square whose edges are all the same length and are either 
parallel or perpendicular to the x-axis and y-axis.

Implement the DetectSquares class:

- DetectSquares() Initializes the object with an empty data structure.
- void add(int[] point) Adds a new point point = [x, y] to the data structure.
- int count(int[] point) Counts the number of ways to form axis-aligned squares with 
  point point = [x, y] as described above.

Example:
    Input:
    ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
    [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    Output:
    [null, null, null, null, 1, 0, null, 2]

    Explanation:
    DetectSquares detectSquares = new DetectSquares();
    detectSquares.add([3, 10]);
    detectSquares.add([11, 2]);
    detectSquares.add([3, 2]);
    detectSquares.count([11, 10]); // return 1. You can choose:
                                   //   - The first, second, and third points
    detectSquares.count([14, 8]);  // return 0. The query point cannot form a square with any points in the data structure.
    detectSquares.add([11, 2]);    // Adding duplicate points is allowed.
    detectSquares.count([11, 10]); // return 2. You can choose:
                                   //   - The first, second, and third points
                                   //   - The first, third, and fourth points

Constraints:
    point.length == 2
    0 <= x, y <= 1000
    At most 3000 calls in total will be made to add and count.
"""

class DetectSquares:

    def __init__(self):
        """
        Initialize the DetectSquares data structure.
        Uses a defaultdict of defaultdicts to efficiently track point frequencies.
        """
        self.points_count = defaultdict(lambda : defaultdict(int))

    def add(self, point: List[int]) ->None:
        """
        Add a point to the data structure.
        
        Args:
            point: A point [x, y] to be added
        """
        x, y = point
        self.points_count[x][y] += 1

    def count(self, point: List[int]) ->int:
        """
        Count the number of squares that can be formed with this point as one corner.
        
        Args:
            point: A query point [x, y]
            
        Returns:
            int: The number of squares that can be formed
        """
        x1, y1 = point
        total_squares = 0
        if x1 not in self.points_count:
            return 0
        for y2, count_y2 in self.points_count[x1].items():
            if y2 == y1:
                continue
            side_length = abs(y2 - y1)
            total_squares += self._count_squares(x1, y1, x1 + side_length,
                y2, count_y2)
            total_squares += self._count_squares(x1, y1, x1 - side_length,
                y2, count_y2)
        return total_squares

    def _count_squares(self, x1: int, y1: int, x3: int, y2: int, count_y2: int
        ) ->int:
        """
        Helper function to count squares formed for the given coordinates.
        
        Args:
            x1, y1: Coordinates of the query point
            x3: x-coordinate of the possible diagonal point
            y2: y-coordinate of the second point sharing the x1 coordinate
            count_y2: Count of points at (x1, y2)
            
        Returns:
            int: Number of squares that can be formed
        """
        if x3 in self.points_count:
            return self.points_count[x3][y1] * self.points_count[x3][y2
                ] * count_y2
        return 0


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    print(detectSquares.count([11, 10]))  # Output: 1
    print(detectSquares.count([14, 8]))   # Output: 0
    detectSquares.add([11, 2])
    print(detectSquares.count([11, 10]))  # Output: 2
