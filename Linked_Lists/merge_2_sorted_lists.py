'''
LeetCode: Merge Two Sorted Lists
Solution: O(m+n)
Algorithm: Same as mergesort "merge" function
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        ite = dummy_head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                ite.next = l1
                l1 = l1.next
            else:
                ite.next = l2
                l2 = l2.next
            ite = ite.next
        if l1 is not None:
            ite.next = l1
        if l2 is not None:
            ite.next = l2      
        dummy_head = dummy_head.next
        return dummy_head