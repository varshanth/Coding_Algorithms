'''
LeetCode: Maximum Subarray

Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Solution: O(n)
Algorithm:
    1) Initialize 2 variables, one which keeps track of the current subarray
    sum and the other as the max subarray sum to -1*max value
    2) Go through the array and assign the current subarray sum as the max of
    the (current sub array sum + nums[i]) and the nums[i]. The first term
    keeps track of the contiguous property while the second term handles when
    the current term by itself is greater than current sub array sum with the
    term e.g) curr sub array sum = -1 and term = 5.
    3) Assign the maximum subarray sum to be max of the current max subarray
    sum and the current subarray sum    
'''
from sys import maxsize
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if len_nums is 0:
            return 0
        largest_continuous = continuous = -maxsize
        for i in range(len_nums):
            continuous = max(continuous+nums[i], nums[i])
            largest_continuous = max(largest_continuous, continuous)
        return largest_continuous
