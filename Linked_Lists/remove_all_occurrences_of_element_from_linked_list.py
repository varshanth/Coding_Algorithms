'''
LeetCode: Remove Element from LinkedList
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5

Solution: O(n)
Algorithm:
    1) Maintain 2 pointers, fast and slow. Slow will start on dummy_head and
    fast will start on head
    2) Link slow to fast i.e slow.next = fast and update slow as slow.next only
    if fast.val is not equal to target val.
    3) Make sure to take care of the case where the target to be deleted is the
    last node. If the node at the end was not the target, it would have had
    its next pointer as None. Hence we just assign slow.next as None because
    the slow would have the last known node whose value is not the target val.
    
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = dummy_head
        fast = dummy_head.next
        while fast is not None:
            if fast.val != val:
                slow.next = fast
                slow = fast
            fast = fast.next
        slow.next = None
        return dummy_head.next