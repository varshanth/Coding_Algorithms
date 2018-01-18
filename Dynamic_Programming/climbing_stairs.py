'''
LeetCode: Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you
climb to the top?

Note: Given n will be a positive integer.


Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Solution: O(n)
Algorithm: Dynamic Programming:
    1) The recursive function should accept the current step, the max step, and
    a dictionary which keeps track of the number of ways you can reach the last
    step from the current step.
    2) If the current step is greater than the max step, the step is invalid
    hence return 0 (it is not a valid sequence). If the current step is the max
    step, the step sequence is valid, hence return 1
    3) See if the number of valid steps from the current step is already
    calculated by checking the dictionary. If it is not, calculate the number
    of valid ways of reaching the max step from one step up and from two steps
    up and store the sum of both in the dictionary as the number of valid
    ways of reaching the max step from the current step
    4) Return the number of valid ways of reaching the max step from the
    current step
'''
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {}
        return self.climb(0, n, memory)

    def climb(self, curr_step, max_step, memory):
        if curr_step == max_step:
            return 1
        if curr_step > max_step:
            return 0
        if curr_step not in memory:
            one_step = self.climb(curr_step+1, max_step, memory)
            two_step = self.climb(curr_step+2, max_step, memory)
            memory[curr_step] = one_step + two_step
        return memory[curr_step]