'''
LeetCode: Min Cost Climbing Stairs

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
indexed).

Once you pay the cost, you can either climb one or two steps. You need to find
minimum cost to reach the top of the floor, and you can either start from the
step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s,
skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].

Solution: O(n)
Algorithm: Dynamic Programming:
    1) The recursive function should accept the current step, the max step, the
    cost array and a dictionary which keeps track of the minimum cost of moving
    up from the current step.
    2) If the current step is greater than the max step, the destination is
    reached, so the cost is 0. Return 0
    3) See if the min cost from the current step is already calculated by
    checking the dictionary. If it is not, calculate the cost required to take
    one step up and the cost required to take two steps up. Find the minimum
    and add it to the cost of taking the current step and store this value in
    the dictionary as the min cost of taking the path from current step
    4) Return the min cost of taking the path from current step
'''
class Solution:
    costs = {}
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        decisions = {}
        max_step = len(cost)-1
        return min(self.climb(0, max_step, cost, decisions), self.climb(1, max_step, cost, decisions))
    
    def climb(self, curr_step, max_step, cost, decisions):
        if curr_step > max_step:
            return 0
        if curr_step not in decisions:
            one = self.climb(curr_step+1, max_step, cost, decisions)
            two = self.climb(curr_step+2, max_step, cost, decisions)
            decisions[curr_step] = cost[curr_step] + min(one, two)
        return decisions[curr_step]