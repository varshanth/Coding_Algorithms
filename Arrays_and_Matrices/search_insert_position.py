'''
LeetCode: Search Insert Position

Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 1:

Input: [1,3,5,6], 0
Output: 0

Solution: O(log(n))
Algorithm:
    1) Perform binary search. If arr[mid] == target, return mid
    2) Other cases come down to how binary search works in case of the
    penultimate and ultimate step:
        Arr = [a, b], required to insert c.
        low = 0, high = 1. Remember, mid = (0+1)//2 = 0
        
        i) If c < a, required to return 0
        Penultimate: high = mid-1 = 0. 
        Ultimate: mid = (0+0)//2 = 0, c < arr[mid]=a, high = mid-1 = -1, stop.
        Mid is 0, which is what we want to return
        
        ii) If a < c < b, required to return 1
        Penultimate: a < c, so low = mid+1 = 1
        Ultimate: mid=(1+1)/2 = 1, c < arr[mid]=b, high = mid-1 = 0, stop
        Mid is 1, which is what we want to return
        
        iii) If b < c, required to return 2
        Penultimate: a < c, so low = mid+1 = 1
        Ultimate: mid=(1+1)/2 = 1, c > arr[mid]=b, low = mid+1=2, stop
        Mid is 1, which is 1 less than what we want to return
        
        Hence if target (c) > arr[mid], then return mid+1
'''    


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) -1
        while lo <= hi:
            mid = (lo + hi) //2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        if nums[mid] < target:
            mid +=1
        return mid