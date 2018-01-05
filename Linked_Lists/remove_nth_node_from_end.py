'''
LeetCode: Remove nth node from the end of linked list
Solution: O(n)
Algorithm:
    1) Allocate a dummy node (dummy_head) and make it to point to the head
    2) Initialize a fast and slow pointer to the dummy_head
    3) Make the fast pointer to travel to the nth node
    4) Increment the fast and the slow pointer until fast.next is None
    5) At this point, the slow.next is the node to be deleted, so assign
    slow.next = slow.next.next
    6) Assign head to be dummy_head.next
    7) Return head
    
Important details:
******************
    1) Requirement of dummy_head is for the case where there is only 1 node
    in the list and that is to be deleted
    2) The main logic is to locate the position of the n-1th node from the end
    and this can be done by making sure that we are always n nodes ahead of the
    last.

e.g) 1 2 3 4 5, n=3
    d  1  2  3  4  5
    sf
**  Move fast to n=3
    s  f
    s     f
    s        f
**  Start moving s with f
       s        f
          s        f
    del   s->
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = fast = dummy_head
        for i in range(n):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        head = dummy_head.next
        return head