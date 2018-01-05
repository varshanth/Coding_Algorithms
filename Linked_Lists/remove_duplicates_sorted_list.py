'''
LeetCode: Removing duplicates from sorted Linked List

Solution: O(n)
Algorithm:
    1) Use slow and fast pointers. Slow pointer will always point to a unique
    node while the fast pointer seeks the next unique node.
    2) When the fast pointer finds the next unique node, do slow.next = fast
    3) Update the slow and fast pointers and perform 2) and 3) until fast is
    None
    4) Take care of the edge cases where size of list can be 0 or 1
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        slow = head
        fast = head.next
        duplicate_mode = False
        while fast is not None:
            duplicate_mode = False
            if fast.val != slow.val:
                slow.next = fast
                slow = fast
            else:
                duplicate_mode = True
            fast = fast.next
        if duplicate_mode:
            slow.next = None
        return head