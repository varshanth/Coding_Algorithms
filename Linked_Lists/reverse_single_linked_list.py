'''
LeetCode: Reverse a singly linked list
Solution: O(n)
Algorithm:
    1) Init previous node to None and current node to head
    2) Perform the following till current node is None:
       a) Save the next node
       b) Assign the current node.next to the previous node
       c) Update the previous node as the current node
       d) Update the current node as the saved next node
    3) Return the previous node as the head
    
e.g)
    
    1 ->  2 ->  3 ->  4 ->
p   c

    1 <-  2 ->  3 ->  4 ->
    p     c
    
    1 <-  2 <-  3 ->  4 ->
          p     c

    1 <-  2 <-  3 <-  4 ->
                p     c

    1 <-  2 <-  3 <-  4 <-
                      p     c
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        prev_node = next_node = None
        curr_node = head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        return prev_node
        