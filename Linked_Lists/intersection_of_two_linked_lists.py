'''
LeetCode: Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked
 lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function
returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

Solution: Time: O(n) Space: O(1)
Algorithm:
    The basic idea of the algorithm is to make the iterators run the same
    length so that we can compare its value.
    1) Run 2 iterators to determine the size of each list
    2) Get the difference in sizes between the 2 lists
    3) Make the pointer of the long lists go ahead by the "difference" amount
    of nodes
    4) Now both the pointers to the respective lists have the same number of
    nodes to traverse
    5) Iterate through nodes of the 2 lists at the same time and if the
    iterators are equal, then return the iterator node
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        A_iter = headA
        B_iter = headB
        A_size = 0
        B_size = 0
        while A_iter:
            A_size += 1
            A_iter = A_iter.next
        while B_iter:
            B_size += 1
            B_iter = B_iter.next
        size_diff = A_size - B_size
        A_iter = headA
        B_iter = headB
        if size_diff < 0:
            for i in range(-size_diff):
                B_iter = B_iter.next
        else:
            for i in range(size_diff):
                A_iter = A_iter.next
        while A_iter and A_iter != B_iter:
            A_iter = A_iter.next
            B_iter = B_iter.next
        return A_iter