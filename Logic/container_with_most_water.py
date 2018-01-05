'''
LeetCode:
Given n non-negative integers a1, a2, ..., an, where each represents a point at
 coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
 line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
 forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Solution: O(n)
Algorithm:
    There are 2 ways: brute force and optimized.
    Brute force would be to consider the "upper" or "lower" triangle formed by
    taking 2 pointers, considering distance between the pointers and the min
    of the 2 individual items and keeping track of the max area
    
    Optimized: Greedy:
        1) When you have to optimize a value dependent on 2 quantities, start
           by optimizing one of them first. Here, take 2 pointers, one starting
           from 0 and the other starting from the end. Hence you are maximizing
           one of the distances which are required for the calculation of the
           area
        2) Now consider the area formed by the product of the 2 difference b/w
           the 2 indices and the min of the 2 values at the indices. Keep track
           of the best area.
        3) Now try to optimize the other quantity i.e the y value. We do this by
           analyzing the value at the 2 pointers. Whichever one has a smaller
           value, move the corresponding pointer accordingly.
           
See the solution video for a visual explanation
https://leetcode.com/problems/container-with-most-water/solution/
'''

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        best = 0
        while left < right:
            area = abs(right-left) * min(height[left], height[right])
            if area > best:
                best = area
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best