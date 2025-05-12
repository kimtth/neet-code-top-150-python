from typing import List

"""
LeetCode Combination Sum II

Problem from LeetCode: https://leetcode.com/problems/combination-sum-ii/

Description:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.
Note: The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6],[1,2,5],[1,7],[2,6]]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5
Output: [[1,2,2],[5]]
"""

class Solution:
    def combination_sum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations of numbers that sum to target.
        Each number may only be used once in the combination.
        
        Args:
            candidates: Collection of candidate numbers (may contain duplicates)
            target: Target sum
            
        Returns:
            List[List[int]]: All unique combinations that sum to target
        """
        # Sort to handle duplicates
        candidates.sort()
        result = []
        self._backtrack(candidates, target, [], result, 0)
        return result
    
    def _backtrack(self, candidates: List[int], target: int, path: List[int], result: List[List[int]], start: int) -> None:
        """
        Helper function for backtracking.
        
        Args:
            candidates: Available numbers
            target: Remaining target sum
            path: Current combination being built
            result: List to collect valid combinations
            start: Starting index to avoid duplicates
        """
        if target == 0:
            result.append(path[:])
            return
            
        if target < 0:
            return
            
        for i in range(start, len(candidates)):
            # Skip duplicates to avoid duplicate combinations
            if i > start and candidates[i] == candidates[i-1]:
                continue
                
            if candidates[i] > target:
                break  # No need to continue as future candidates will be larger
                
            path.append(candidates[i])
            # Move to next index as each number can only be used once
            self._backtrack(candidates, target - candidates[i], path, result, i + 1)
            path.pop()  # Backtrack
    
    def combination_sum2_frequency(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Alternative approach using frequency counting to handle duplicates.
        
        Args:
            candidates: Collection of candidate numbers
            target: Target sum
            
        Returns:
            List[List[int]]: All unique combinations that sum to target
        """
        # Count frequency of each number
        counter = {}
        for num in candidates:
            counter[num] = counter.get(num, 0) + 1
            
        # Create a list of (number, frequency) pairs
        counter_list = [(num, freq) for num, freq in counter.items()]
        counter_list.sort()  # Sort by number
        
        result = []
        self._backtrack_with_frequency(counter_list, target, [], result, 0)
        return result
    
    def _backtrack_with_frequency(self, counter_list, target, path, result, start):
        """Helper function for backtracking with frequency."""
        if target == 0:
            result.append(path[:])
            return
            
        if target < 0 or start >= len(counter_list):
            return
            
        # Skip current number
        self._backtrack_with_frequency(counter_list, target, path, result, start + 1)
        
        # Use current number
        num, freq = counter_list[start]
        
        # Try using the current number 1 to freq times
        for i in range(1, freq + 1):
            if num * i > target:
                break
                
            path.extend([num] * i)
            self._backtrack_with_frequency(counter_list, target - num * i, path, result, start + 1)
            # Remove the added numbers
            for _ in range(i):
                path.pop()

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    candidates1 = [10, 1, 2, 7, 6, 1, 5]
    target1 = 8
    result1 = solution.combination_sum2(candidates1, target1)
    print(f"Example 1: candidates={candidates1}, target={target1}")
    print(f"Result: {result1}")  # Expected output: [[1,1,6],[1,2,5],[1,7],[2,6]]
    
    # Example 2
    candidates2 = [2, 5, 2, 1, 2]
    target2 = 5
    result2 = solution.combination_sum2(candidates2, target2)
    print(f"\nExample 2: candidates={candidates2}, target={target2}")
    print(f"Result: {result2}")  # Expected output: [[1,2,2],[5]]
    
    # Compare with frequency approach
    print("\nUsing frequency approach:")
    print(f"Example 1: {solution.combination_sum2_frequency(candidates1, target1)}")
    print(f"Example 2: {solution.combination_sum2_frequency(candidates2, target2)}")
