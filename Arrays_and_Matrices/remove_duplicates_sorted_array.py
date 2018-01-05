'''
LeetCode: Remove duplicate elements in-place from sorted array and return 
effective length

Given a sorted array, remove the duplicates in-place such that each element
appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.

Solution: O(n)
Algorithm:
    1) Use 2 pointers, a slow and a fast. Slow points to the first element,
    fast points to the second element
    2) Repeat until slow or fast reach the length of the array
    a) If the value at slow pointer is not equal to fast pointer, increase
    length counter, slow pointer and copy the value at slow pointer to that
    in fast pointer
    b) Increment fast pointer

e.g)
    1   2   2   3  4
    s   f                ---> increment s, copy a[f] to a[s] and increment f
    
    1   2   2   3  4
        s   f            ---> increment s, copy a[f] to a[s] and increment f
        
    1   2   2   3  4
        s       f        ---> increment f
        
    1   2   3   3  4
            s   f        ---> increment s, copy a[f] to a[s] and increment f
            
    1   2   3   3  4
            s      f     ---> increment f
            
    1   2   3   4  4
                s  f     ---> increment s, copy a[f] to a[s] and increment f
                
'''
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_arr = len(nums)
        if  len_arr == 0:
            return 0
        slow = 0
        fast = 1
        while slow < len_arr and fast < len_arr:
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow+1

