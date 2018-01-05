'''
LeetCode: Remove element in place

Given an array and a value, remove all instances of that value in-place and
return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.

Example:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums
being 2.

Solution: O(n)
Algorithm:
    1) 2 pointers: slow and fast. Both start at the same position. If fast
    encounters the value, it will keep on incrementing until some other element
    has been encountered.
    2) Copy value at fast to value at slow, and increment slow
    3) Increment fast
'''

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len_nums = len(nums)
        slow = 0
        fast = 0
        while fast < len_nums:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
        
        