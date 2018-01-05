'''
LeetCode: Swap Nodes in Pairs
Solution: O(n)
Algorithm:
    1) Use 2 pointers, a fast and a slow. Let the fast go ahead to the 2nd node
    At this point, the we can make all the necessary connections because:
        a) slow sees slow.next which is the node fast is to be exchanged with
        b) fast sees fast.next which is the node that the new slow has to make
           connections with
    2) After making the connections, we want both the slow and fast to start
    from the same point again, which is ideally the new fast.next
    3) Perform 1 and 2 until fast node becomes None

***IMPORTANT LESSON: ORDER OF MAKING THE CONNECTIONS MATTER***
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = fast = dummy_head
        num_forw = 0
        while fast is not None:
            if num_forw == 2:
                num_forw = 0
                slow.next.next = fast.next
                fast.next = slow.next
                slow.next = fast
                slow = fast = fast.next
            num_forw += 1
            fast = fast.next
        return dummy_head.next
            
            
            
        