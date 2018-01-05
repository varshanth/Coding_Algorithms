'''
LeetCode: Linked List Cycle
Solution: O(n)
Algorithm:
    1) Initialize a slow and fast pointer to the head
    2) Traverse the list simultaneously using the slow and fast pointer.
    3) Update the fast pointer by skipping one node (rate = 2) and update the 
    slow pointer to its next connection (rate = 1)
    4) If there is a cycle, the fast node will loop through once and eventually
    catch up to the slow node by "lapping" it
    5) If there is no cycle, the fast pointer will ultimately become null
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            if slow is fast:
                return True
            slow = slow.next
        return False
        