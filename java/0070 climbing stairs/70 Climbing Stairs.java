// Most asked problems at FAANG companies: https://docs.google.com/spreadsheets/d/1hzP8j7matoUiJ15N-RhsL5Dmig8_E3aP/edit#gid=1377915986

// Leetcode Link: https://leetcode.com/problems/climbing-stairs/

// Video Solution: https://www.youtube.com/watch?v=Y0lT9Fck7qI

**************** Java Solution ***********************

import java.util.HashMap;
import java.util.Map;

class Solution {
    /**
     * You are climbing a staircase that takes n steps to reach the top.
     * Each time you can either climb 1 or 2 steps.
     * Return the number of distinct ways you can climb to the top.
     *
     * @param n Number of steps to reach the top
     * @return Number of distinct ways to climb to the top
     */
    public int climbStairs(int n) {
        // Base cases
        if (n <= 2) {
            return n;
        }
        
        // Initialize dp array
        int[] dp = new int[n + 1];
        dp[1] = 1;  // One way to climb 1 step
        dp[2] = 2;  // Two ways to climb 2 steps: 1+1 or 2
        
        // Fill dp array
        for (int i = 3; i <= n; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }
        
        return dp[n];
    }
    
    /**
     * Space-optimized solution using only two variables instead of an array.
     *
     * @param n Number of steps to reach the top
     * @return Number of distinct ways to climb to the top
     */
    public int climbStairsOptimized(int n) {
        if (n <= 2) {
            return n;
        }
        
        int oneStepBefore = 2;  // Ways to reach the step before the current step
        int twoStepsBefore = 1;  // Ways to reach two steps before the current step
        int currentWays = 0;
        
        for (int i = 3; i <= n; i++) {
            currentWays = oneStepBefore + twoStepsBefore;
            twoStepsBefore = oneStepBefore;
            oneStepBefore = currentWays;
        }
        
        return currentWays;
    }
    
    /**
     * Recursive solution with memoization to avoid redundant calculations.
     *
     * @param n Number of steps to reach the top
     * @return Number of distinct ways to climb to the top
     */
    public int climbStairsRecursive(int n) {
        Map<Integer, Integer> memo = new HashMap<>();
        return climb(n, memo);
    }
    
    private int climb(int n, Map<Integer, Integer> memo) {
        if (memo.containsKey(n)) {
            return memo.get(n);
        }
        
        if (n <= 2) {
            return n;
        }
        
        memo.put(n, climb(n - 1, memo) + climb(n - 2, memo));
        return memo.get(n);
    }
    
    /**
     * Mathematical solution using the Fibonacci formula.
     *
     * @param n Number of steps to reach the top
     * @return Number of distinct ways to climb to the top
     */
    public int climbStairsFibonacci(int n) {
        double sqrt5 = Math.sqrt(5);
        double fibn = Math.pow((1 + sqrt5) / 2, n + 1) - Math.pow((1 - sqrt5) / 2, n + 1);
        return (int) (fibn / sqrt5);
    }
}
