'''
Leetcode: 2 Sum

Given an array of integers, return indices of the two numbers such that they
add up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Solution: O(nlogn)
Algorithm:
    1) Sort items (nlogn)
    2) Fix first number as the first element of the sorted array and keep track
       of the original index say "a"
    3) Using binary search (logn) see if the complement exists in the rest
       of the array.
       If yes, derive its original index "b" and return [a,b]
       else, fix first number as the next number in the sorted array and repeat
       (n)
Complexity: Step 1: O(nlogn) Step 2: O(nlogn). Hence complexity is O(nlogn)

Important Notes:
    1) Do NOT use np.searchsorted, it merges repeated elements and hence yields
       wrong indices
    2) Leetcode requires explicit integer conversion for the elements it takes
'''

import numpy as np

class Solution:       
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_cpy = np.array(nums)
        sorted_args = np.argsort(nums_cpy)
        sorted_nums = nums_cpy[sorted_args]
        first_idx = 0
        target_idx = -1
        found_idx = -1
        for i in range(1, len(nums)):
            to_find = target - sorted_nums[first_idx]
            found_idx = self.bin_search(sorted_nums[i:], to_find)
            if found_idx == -1:
                first_idx += 1
            else:
                target_idx = i + found_idx
                break
        if found_idx == -1:
            return list([])
        else:
            first_idx = sorted_args[first_idx]
            second_idx = sorted_args[target_idx]
            return list([int(first_idx), int(second_idx)])
    
    def bin_search(self, arr, item):
        start = 0
        end = len(arr)-1
        while (start <= end):
            mid = (start + end)//2
            if arr[mid] == item:
                return mid
            elif arr[mid] < item:
                start = mid+1
            else:
                end = mid-1
        return -1