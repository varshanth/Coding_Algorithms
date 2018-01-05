'''
LeetCode: Insert Interval

Given a set of non-overlapping intervals, insert a new interval into the
intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their
start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],
[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].


Solution: O(n)

** Hint: Think QuickSort/Quickselect logic

Algorithm:
    1) Treat the newly inserted interval as the "pivot"
    2) Iterate through each interval. If the interval's starting is greater
    than the pivot's ending, then insert the interval to the right. If the
    interval's ending is lesser than the pivot's starting, insert it to the
    left. Else it means that the interval can be used for expanding or being
    absorbed by the current pivot. We set the pivot's start as the min of
    existing pivot's start and the interval's start. We set the pivot's end as
    the maximum of the interval's end and the current pivot's end

'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        left = []
        right = []
        new_int_start = newInterval.start
        new_int_end = newInterval.end
        for interval in intervals:
            print(interval.start)
            if interval.end < new_int_start:
                left.append(interval)
            elif interval.start > new_int_end:
                right.append(interval)
            else:
                new_int_start = min(interval.start, new_int_start)
                new_int_end = max(interval.end, new_int_end)
        return list(left+[Interval(new_int_start, new_int_end)]+right)