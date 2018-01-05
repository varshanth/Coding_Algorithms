'''
LeetCode: Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.


Solution: O(n)
Algorithm:
    This problem differs from Remove Duplicates from Sorted List in the way
    that we have to condition the copy of fast to slow.
    
    1) It is not sufficient just to have the slow.next update just based on the
    check that slow.val is not equal to fast.val . We need to add an additional
    constraint on the fast.val which conditions on the fast.next.val as well.
    This is required because the current fast seems unique with respect slow
    but making a connection between the slow and current fast is incorrect
    if the fast is not unique with respect to its next value as well.
    e.g) 1     2      2      3
         s     f     f.next
    
    2) The check that slow.val is not equal to fast.val itself has to be
    transformed since we may skip the next unique value w.r.t slow.val if that
    value is not unique to the next value as discussed in the previous point.
    A new check has to be introduced to check if the current fast.val is not
    equal to the previous fast.val. The previous fast.val reflects the most
    recent value which the current fast.val must avoid
    e.g) 1     2      2       3      4
         s            p       f      f.next
         
         (here we see comparing f.val to s.val is useless in determining the
         uniqueness of f.val with respect to the most recent past)
         
    3) For the final node, we can't check the f.next val, so just check if
    f.val is not equal to f.prev.val
    
    4) After coming out of the loop, it might be the fact that the last node is
    not unique. In this case, the slow pointer's next would be pointing to a
    repeating element. Hence we just assign None to slow.next since if the last
    node was unique, it's value would have been None anyways.

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
        fast_prev_val = None
        dummy_head = ListNode(fast_prev_val)
        dummy_head.next = head
        slow = dummy_head
        fast = head
        while fast is not None:
            if ((fast.next is None and fast.val != fast_prev_val) or 
                (fast.next is not None and (fast.val != fast.next.val and fast.val != fast_prev_val))):
                slow.next = fast
                slow = fast
            fast_prev_val = fast.val
            fast = fast.next
        # If a distinct element was never found after the previous one, assign
        # slow.next to None 
        slow.next = None
        return dummy_head.next