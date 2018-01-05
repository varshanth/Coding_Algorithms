'''
Leetcode: Search in rotated sorted array
Suppose an array sorted in ascending order is rotated at some pivot unknown to
you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index,
 otherwise return -1.

You may assume no duplicate exists in the array.

Solution: O(n)
Algorithm:
    1) Rotated sorted array will contain 2 parts both of which are sorted, but
    the elements of the right part will be lesser than the elements of the left
    part. Hence iterate linearly and find this boundary to get the indices of
    the 2 parts
    2) Apply binary search on each of the parts. If it is found in left part,
    return the found index, else if it is found on the right part, return
    partition index + found index
'''


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        # detect boundary
        i = 1
        while i < len(nums):
            if nums[i] < nums[i-1]:
                break
            i += 1
        left_arr = nums[:i]
        right_arr = nums[i:]
        # Left Search
        found_idx = self.bin_search(left_arr, target)
        if found_idx == -1:
            found_idx = self.bin_search(right_arr, target)
            if found_idx == -1:
                return -1
            else:
                return i+found_idx
        else:
            return found_idx
    
    
    def bin_search(self, arr, elem):
        left = 0
        right = len(arr) -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == elem:
                return mid
            elif arr[mid] < elem:
                left = mid+1
            else:
                right = mid-1
        return -1