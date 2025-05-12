from typing import List

"""
LeetCode Jump Game II

Problem from LeetCode: https://leetcode.com/problems/jump-game-ii/

Description:
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i.
In other words, if you are at nums[i], you can jump to any nums[i + j] where:
- 0 <= j <= nums[i] and
- i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
"""

class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        Find the minimum number of jumps to reach the last index.
        Uses a greedy approach with O(n) time complexity.
        
        Args:
            nums: Array of integers representing maximum jump length
            
        Returns:
            int: Minimum number of jumps to reach the last index
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        # Initialize variables
        jumps = 0          # Number of jumps needed
        current_max = 0    # Maximum index that can be reached with current jumps
        farthest = 0       # Farthest index that can be reached
        
        # Iterate through the array
        for i in range(n - 1):
            # Update the farthest possible reach
            farthest = max(farthest, i + nums[i])
            
            # If we've reached the current maximum, we need to make a jump
            if i == current_max:
                jumps += 1
                current_max = farthest
                
                # If we can already reach the end, no need to continue
                if current_max >= n - 1:
                    break
                    
        return jumps
    
    def jump_dp(self, nums: List[int]) -> int:
        """
        Find the minimum number of jumps using dynamic programming.
        O(n²) time complexity but more intuitive.
        
        Args:
            nums: Array of integers representing maximum jump length
            
        Returns:
            int: Minimum number of jumps to reach the last index
        """
        n = len(nums)
        # dp[i] represents the minimum jumps needed to reach index i
        dp = [float('inf')] * n
        dp[0] = 0  # No jumps needed to reach the starting position
        
        for i in range(n):
            # Try all possible jumps from position i
            for j in range(1, nums[i] + 1):
                if i + j < n:
                    # Update dp[i+j] if this jump is better
                    dp[i + j] = min(dp[i + j], dp[i] + 1)
                    
        return dp[n - 1]
    
    def jump_bfs(self, nums: List[int]) -> int:
        """
        Find the minimum number of jumps using a BFS-like approach.
        Conceptually similar to the greedy approach but framed as BFS.
        
        Args:
            nums: Array of integers representing maximum jump length
            
        Returns:
            int: Minimum number of jumps to reach the last index
        """
        n = len(nums)
        if n <= 1:
            return 0
            
        # Initialize variables
        level = 0          # Current jump level (number of jumps)
        current_max = 0    # Maximum index that can be reached with current level
        next_max = 0       # Maximum index that can be reached with next level
        
        i = 0
        while i <= current_max:
            # If we can reach the end in the current level
            if current_max >= n - 1:
                return level
                
            # Explore all positions in the current level
            # and find the farthest position for the next level
            while i <= current_max:
                next_max = max(next_max, i + nums[i])
                i += 1
                
            # Move to the next level
            level += 1
            current_max = next_max
            
        return level

if __name__ == '__main__':
    # Example usage based on LeetCode sample
    solution = Solution()
    
    # Example 1
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.jump(nums1)
    print(f"Example 1: nums={nums1}, result={result1}")  # Expected output: 2
    
    # Example 2
    nums2 = [2, 3, 0, 1, 4]
    result2 = solution.jump(nums2)
    print(f"Example 2: nums={nums2}, result={result2}")  # Expected output: 2
    
    # Compare with other approaches
    print("\nUsing dynamic programming approach:")
    print(f"Example 1: {solution.jump_dp(nums1)}")
    print(f"Example 2: {solution.jump_dp(nums2)}")
    
    print("\nUsing BFS-like approach:")
    print(f"Example 1: {solution.jump_bfs(nums1)}")
    print(f"Example 2: {solution.jump_bfs(nums2)}")
