from typing import List

"""
LeetCode Combination Sum

Problem from LeetCode: https://leetcode.com/problems/combination-sum/

Description:
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []
"""

class Solution:
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all unique combinations of numbers that sum to target.
        Uses backtracking approach.
        
        Args:
            candidates: Array of distinct integers
            target: Target sum
            
        Returns:
            List[List[int]]: All unique combinations that sum to target
        """
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
        if target < 0:
            return
            
        if target == 0:
            result.append(path[:])
            return
            
        for i in range(start, len(candidates)):
            path.append(candidates[i])
            # Continue from the same index since we can reuse the same element
            self._backtrack(candidates, target - candidates[i], path, result, i)
            path.pop()  # Backtrack
    
    def combination_sum_iterative(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Iterative approach using a queue-like structure.
        
        Args:
            candidates: Array of distinct integers
            target: Target sum
            
        Returns:
            List[List[int]]: All unique combinations that sum to target
        """
        result = []
        # Sort to optimize and handle smaller candidates first
        candidates.sort()
        
        # Queue of (combination, target_remaining, start_index)
        queue = [([], target, 0)]
        
        while queue:
            path, remain, start = queue.pop(0)
            
            if remain == 0:
                result.append(path)
                continue
                
            for i in range(start, len(candidates)):
                # Skip if this candidate is too large
                if candidates[i] > remain:
                    break
                    
                # Skip duplicates (unnecessary for distinct candidates but useful for extension)
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                # Add this candidate and continue
                new_path = path + [candidates[i]]
                queue.append((new_path, remain - candidates[i], i))  # i to reuse the same element
                
        return result

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    result1 = solution.combination_sum(candidates1, target1)
    print(f"Example 1: candidates={candidates1}, target={target1}")
    print(f"Result: {result1}")  # Expected output: [[2,2,3],[7]]
    
    # Example 2
    candidates2 = [2, 3, 5]
    target2 = 8
    result2 = solution.combination_sum(candidates2, target2)
    print(f"\nExample 2: candidates={candidates2}, target={target2}")
    print(f"Result: {result2}")  # Expected output: [[2,2,2,2],[2,3,3],[3,5]]
    
    # Example 3
    candidates3 = [2]
    target3 = 1
    result3 = solution.combination_sum(candidates3, target3)
    print(f"\nExample 3: candidates={candidates3}, target={target3}")
    print(f"Result: {result3}")  # Expected output: []
    
    # Compare with iterative approach
    print("\nUsing iterative approach:")
    print(f"Example 1: {solution.combination_sum_iterative(candidates1, target1)}")
    print(f"Example 2: {solution.combination_sum_iterative(candidates2, target2)}")
