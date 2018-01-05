'''
LeetCode: Search for a range:

Given an array of integers sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
If target is 10,
return [5, 5]

Solution: O(log(n)) i.e log(n) + 2log(n/2) + 2log(n/4) +..
Algorithm:
    1) Phase 1 - Determine if element is present: Use binary search and
    determine the found index
    2) Initialize left bound and right bound to the found index
    3) Phase 2 - Determine left bound - Iteratively use binary search on
    array[0, left_bound-1] and if the target is found, update left bound and
    continue iteration until binary search returns -1
    4) Phase 3 - Determine right bound - Iteratively use binary search on
    array[0, right_bound-1] and if the target is found, update right bound and
    continue iteration until binary search returns -1
    5) Return [left_bound, right_bound]
    
e.g) 
     1   2   3   3   3    3   3   4   5
P1                 found

     1   2   3   3   3    3   3   4   5
Init               found
                   leftb
                   rightb

     1   2   3   3   3    3   3   4   5
P2           |     found
           leftb
                   rightb

     1   2   3   3   3    3   3   4   5
P3           |     found      |
           leftb              |
                            rightb
                            
'''
                   
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def bin_search(arr, target):
            lo = 0
            hi = len(arr)-1
            while(lo <= hi):
                mid = (lo+hi) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return -1
        # Find the element first
        found_idx = bin_search(nums, target)
        if found_idx < 0:
            return [-1, -1]
        left_bound = right_bound = found_idx
        # Analyze left:
        lo = 0
        hi = found_idx -1
        while True:
            found_in_left = bin_search(nums[lo:hi+1], target)
            if found_in_left < 0:
                break
            left_bound = found_in_left
            hi = found_in_left -1
        # Analyze right:
        lo = found_idx + 1
        hi = len(nums)-1
        while True:
            found_in_right = bin_search(nums[lo:hi+1], target)
            if found_in_right < 0:
                break
            right_bound = lo+found_in_right
            lo = right_bound+1
        return [left_bound, right_bound]