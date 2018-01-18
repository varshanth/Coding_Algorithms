'''
LeetCode: Maximum Product Subarray

Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

Solution: O(n)
Algorithm:
    1) Initialize 3 variables to the 1st element in the array.
    a) An element big which keeps track of the local largest product of the
    current contiguous sub array
    b) An element small which keeps track of the local smallest product of the
    current contiguous sub array
    c) An element maximum which keeps track of the global largest product
    contiguous sub array
    2) Go through the array and calculate
    a) The new big as the max of i) current element ii) current local largest
    product * current element iii) current local smallest product * current
    element. The involvement of the current element in all of the choices
    ensures that the contiguousness is maintained even when a border element
    appears next. e.g) 1 2 3 4 5 0 10, here at 0, the local largest product
    will reset to 0
    b) The new small as the min of i) current element ii) current local largest
    product * current element iii) current local smallest product * current
    element. The involvement of the current element in all of the choices
    ensures that the contiguousness is maintained even when a border element
    appears next. e.g) -1 -2 -3 -4 0 10, here at 0, the local smallest product
    will reset to 0
    3) Assign the new global maximum as the maximum of the current global
    maximum and the local largest product    
'''
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        maximum = big = small = nums[0]
        for i in range(1, len_nums):
            new_big = max(nums[i], nums[i]*big, nums[i]*small)
            new_small = min(nums[i], nums[i]*big, nums[i]*small)
            big = new_big
            small = new_small
            maximum = max(maximum, big)
        return maximum