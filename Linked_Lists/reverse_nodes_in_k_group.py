'''
LeetCode: Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return
its modified list.

k is a positive integer and is less than or equal to the length of the linked
list. If the number of nodes is not a multiple of k then left-out nodes in the
end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5


Solution: Time: O(n) Space: O(1)

Algorithm:
    1) The idea is to have 2 pointers. A slow and a fast. Let's call fast as
    k_iterator. The slow will be pointing to the dummy head and the k_iterator
    will be pointing to the head
    2) Repeat until break:
        a) Allow the k_iterator to visit k nodes (do not update k_iterator
        when it is on the kth node)
        b) If the k_iterator is None, break out completely
        c) If the k_iterator is not none, it means that it has successfully
        visited k nodes
        
        At this stage we have (if k = 3)
            dummy  ->  1  ->  2  ->  3  ->  4
              s                      k
        d) Starting with slow.next, reverse k nodes and establish the links
        appropriately. Save the current slow.next as we must update the slow to
        be slow = current slow.next (starting slow point of next k groups).
        e) Update the k_iterator as new slow.next (because it is the fast node)
        
            dummy  ->  3  ->  2  ->  1  ->  4
                                     s      k
    3) Return dummy_head.next
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k is 1:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = dummy_head
        k_iterator = dummy_head.next
        while True:
            k_temp = 0
            while k_iterator is not None:
                k_temp += 1
                if k_temp == k:
                    k_temp = 0
                    break
                k_iterator = k_iterator.next
            if k_iterator is None:
                break
            prev_node = None
            curr_node = slow.next
            for i in range(k):
                next_node = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = next_node
            slow.next.next = curr_node
            next_slow = slow.next
            slow.next = prev_node
            slow = next_slow
            k_iterator = slow.next  #or curr_node
        return dummy_head.next
            