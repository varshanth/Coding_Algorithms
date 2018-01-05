'''
LeetCode: Reverse Linked List from mth node to nth node
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

Solution: O(n)
Algorithm:
    1) Traverse the list till the mth node while keeping track of the (m-1)th
    node
    e.g) 1 ->  2 -> 3 -> 4 -> 5,   m = 3  n = 5
              m-1   m
    
    2) Normally reverse the linked list with an iterator until the number of
    iterations are (n-m+1). (Why +1? Because we are at the mth node and we have
    to reverse the mth node as well i.e inclusive)

    Here p = previous, c = current (used for reversing a linked list)
    
               ------------|
               |           v
    e.g) 1 ->  2   NULL <- 3 <- 4 <- 5     ,   m = 3  n = 5
              m-1                    p   c
             
    3) Establish the new connections as:
        a) m-1.next.next = current
        
                   ------------|
                   |           v
        e.g) 1 ->  2   NULL    3 <- 4 <- 5       ,   m = 3  n = 5
                  m-1          |         p    c      
                               ---------------^ 
                               
        b) m-1.next = prev
        
                   ----------------------|
                   |                     v
        e.g) 1 ->  2   NULL    3 <- 4 <- 5       ,   m = 3  n = 5
                  m-1          |         p    c      
                               ---------------^ 
                               
'''

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m is n:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = curr_node = head
        m_prev_node = dummy_head
        # Goto the mth node and store the (m-1)th node
        for i in range(1, m):
            m_prev_node = curr_node
            curr_node = curr_node.next
        prev_node = None
        # Reverse the list till nth node
        for i in range(n-m+1):
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        m_prev_node.next.next = curr_node
        m_prev_node.next = prev_node
        return dummy_head.next  