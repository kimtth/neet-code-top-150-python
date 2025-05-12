from typing import List, Optional

"""
LeetCode Merge Triplets To Form Target Triplet

Problem from LeetCode: https://leetcode.com/problems/merge-triplets-to-form-target-triplet/

A triplet is an array of three integers. You are given a 2D integer array triplets, where triplets[i] = [ai, bi, ci] 
describes the ith triplet. You are also given an integer array target = [x, y, z] that describes the triplet you want to obtain.

To obtain target, you may apply the following operation on triplets any number of times:
- Choose two indices (0-indexed) i and j (i != j) and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
- For example, if triplets[i] = [2, 5, 3] and triplets[j] = [1, 7, 5], triplets[j] will be updated to [max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5].

Return true if it is possible to obtain the target triplet [x, y, z] as an element of triplets, or false otherwise.

Example 1:
Input: triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and last triplets [[2,5,3],[1,8,4],[1,7,5]]. Update the last triplet to [max(2,1), max(5,7), max(3,5)] = [2,7,5]. triplets = [[2,5,3],[1,8,4],[2,7,5]]
The target triplet [2,7,5] is now an element of triplets.

Example 2:
Input: triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
Output: false
Explanation: It is impossible to have [3,2,5] as an element because there is no 2 in any of the triplets.

Example 3:
Input: triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
Output: true
Explanation: Perform the following operations:
- Choose the first and third triplets [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]. Update the third triplet to [max(2,1), max(5,2), max(3,5)] = [2,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]].
- Choose the third and fourth triplets [[2,5,3],[2,3,4],[2,5,5],[5,2,3]]. Update the fourth triplet to [max(2,5), max(5,2), max(5,3)] = [5,5,5]. triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]].
The target triplet [5,5,5] is now an element of triplets.

Constraints:
- 1 <= triplets.length <= 10^5
- triplets[i].length == target.length == 3
- 1 <= ai, bi, ci, x, y, z <= 1000
"""

class Solution:

    def merge_triplets(self, triplets: list[list[int]], target: list[int]
        ) ->bool:
        max_values = [0, 0, 0]
        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[
                2] <= target[2]:
                max_values[0] = max(max_values[0], triplet[0])
                max_values[1] = max(max_values[1], triplet[1])
                max_values[2] = max(max_values[2], triplet[2])
        return max_values[0] == target[0] and max_values[1] == target[1
            ] and max_values[2] == target[2]


if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    target = [2,7,5]
    result = solution.merge_triplets(triplets, target)
    print(f"Example 1: {result}")  # Expected: True
    
    # Example 2
    triplets = [[3,4,5],[4,5,6]]
    target = [3,2,5]
    result = solution.merge_triplets(triplets, target)
    print(f"Example 2: {result}")  # Expected: False
    
    # Example 3
    triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
    target = [5,5,5]
    result = solution.merge_triplets(triplets, target)
    print(f"Example 3: {result}")  # Expected: True
