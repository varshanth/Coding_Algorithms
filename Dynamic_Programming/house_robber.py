'''
LeetCode: House Robber

Solution: O(n)
Algorithm: Dynamic Programming:
    1) We can start one robbing either the first house or by robbing the second
    house
    2) If we rob the first house, the possible choices would be nums[2:] and
    if we rob the second house, the possible choices would be nums[3:]
    3) Initialize the memory
    4) Recursive function which accepts the current house, the choices and the
    memory:
        a) If the current house is greater than the max house, there is no
        profit, so return 0
        b) If the current house is not in the memory, then initialize the
        max profit to the value of the current house, else skip to f)
        c) Go through the range of houses to rob next as current_house + 2
        onwards. Calculate the profit gained as value of robbing current house
        + recursive function which accepts the current house as the iterating
        house i.e
        profit = current_house value + fn_call(iterator, choices, memory)
        d) Check if this profit is greater than the current max profit, if so,
        assign the max profit as the current profit
        e) Add the max profit of the current house to the memory
        f) Return the max profit of current house in the memory
    5) Return max profit as the maximum value of robbing the first house vs
    robbing the second house
'''
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums is 0:
            return 0
        memory = {}
        # Explore 1st onwards
        first = self.rob_further(0, nums, memory)
        # Explore 2nd onwards
        second = self.rob_further(1, nums, memory)
        return max(first, second)
    
    def rob_further(self, current_house, choices, memory):
        if current_house >= len(choices):
            return 0
        if current_house not in memory:
            max_profit = choices[current_house]
            for house in range(current_house+2, len(choices)):
                profit = choices[current_house] + self.rob_further(house, choices, memory)
                max_profit = max(max_profit, profit)
            memory[current_house] = max_profit
        return memory[current_house]