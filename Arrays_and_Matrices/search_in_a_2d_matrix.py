'''
LeetCode: Search in a 2D Matrix
    
Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous
row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

Solution: O(log(m) + log(n))
Algorithm:
    1) Take advantage that the entire matrix is sorted. We do this by narrowing
    down the row which the target can be in. Form an array with the first
    elements of each row. Take advantage of the binary search algorithm and 
    make it return "mid". The typical implementation of binary search can be
    used to isolate the bounds of the target. Consider first row elem array as
    first_row:
        i) If first_row[mid] == target, obviously the target is in that row
       ii) Consider the penultimate and ultimate steps of binary search where
           low = a high = b and it will only be [a,b] to search in between at
           the penultimate step. (Here a and b represent the first elements of
           their respective rows)
           a) If target < a, mid = indexof(a) in first_row
           b) If a < target < b, then mid = index(b) in first_row
           c) If b < target, then mid = index(b) in first_row
          
           In cases where target < first_row[mid], we want it to search in the
           previous row because since the first element of row "mid" is a,
           target will not be in row "mid", but maybe in previous row, so we
           search in row "mid-1". This will be a problem only when mid = 0, so
           we check that condition and return False.
           In case c), if the b < target, then either the element has to be in
           row "mid" or it is not there in the matrix at all.
           
     iii) Now that we have the row in which the target maybe in, perform normal
          binary search on that row to find out if the element exists in that
          row or not
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) is 0:
            return False
        if len(matrix[0]) is 0:
            return False
        
        def bin_search(arr, target):
            low = 0
            high = len(arr)-1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            return mid
        
        first_elem = [row[0] for row in matrix]
        # Narrow down which row the target can be in
        which_row = bin_search(first_elem, target)
        if target < first_elem[0]:
            return False
        if target < first_elem[which_row]:
            which_row -= 1
        return matrix[which_row][bin_search(matrix[which_row], target)] == target