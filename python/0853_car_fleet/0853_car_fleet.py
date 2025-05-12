from typing import List


"""
LeetCode Car Fleet

Problem from LeetCode: https://leetcode.com/problems/car-fleet/

Description:
There are n cars going to the same destination along a one-lane road. The destination is target miles away.

You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same speed. Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting at 6. The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting at 6. The fleet moves at speed 1 until it reaches target.

Constraints:
n == position.length == speed.length
1 <= n <= 10^5
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 10^6
1 <= target <= 10^6
"""

class Solution:

    def car_fleet(self, target: int, position: List[int], speed: List[int]
        ) ->int:
        """
        Determine the number of car fleets that will arrive at the target.
        
        Args:
            target: The target destination (finish line)
            position: Position of each car on the road (0 is the start, target is the end)
            speed: Speed of each car in distance per hour
            
        Returns:
            int: The number of car fleets that will arrive at the target
        """
        n = len(position)
        cars = []
        for i in range(n):
            time_to_target = (target - position[i]) / speed[i]
            cars.append([position[i], time_to_target])
        cars.sort(reverse=True)
        fleets = 0
        current_max_time = 0
        for _, time in cars:
            if time > current_max_time:
                fleets += 1
                current_max_time = time
        return fleets

    def carFleet_stack(self, target: int, position: List[int], speed: List[int]
        ) ->int:
        """
        Determine the number of car fleets using a stack approach.
        
        Args:
            target: The target destination
            position: Position of each car
            speed: Speed of each car
            
        Returns:
            int: The number of car fleets
        """
        cars = sorted(zip(position, speed))
        times = [((target - p) / s) for p, s in cars]
        result = 0
        while times:
            current_time = times.pop()
            if not times or current_time > times[-1]:
                result += 1
        return result

    def carFleet_simplified(self, target: int, position: List[int], speed:
        List[int]) ->int:
        """
        Determine the number of car fleets with simplified code.
        
        Args:
            target: The target destination
            position: Position of each car
            speed: Speed of each car
            
        Returns:
            int: The number of car fleets
        """
        pairs = [(p, (target - p) / s) for p, s in zip(position, speed)]
        pairs.sort()
        fleets = 0
        current_time = 0
        for _, time in reversed(pairs):
            if time > current_time:
                fleets += 1
                current_time = time
        return fleets


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    target1 = 12
    position1 = [10, 8, 0, 5, 3]
    speed1 = [2, 4, 1, 1, 3]
    result1 = solution.car_fleet(target1, position1, speed1)
    print(f"Example 1: {result1}")  # Expected: 3
    
    # Example 2
    target2 = 10
    position2 = [3]
    speed2 = [3]
    result2 = solution.car_fleet(target2, position2, speed2)
    print(f"Example 2: {result2}")  # Expected: 1
    
    # Example 3
    target3 = 100
    position3 = [0, 2, 4]
    speed3 = [4, 2, 1]
    result3 = solution.car_fleet(target3, position3, speed3)
    print(f"Example 3: {result3}")  # Expected: 1
