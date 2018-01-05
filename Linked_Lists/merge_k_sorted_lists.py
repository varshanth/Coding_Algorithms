'''
LeetCode: Merge k sorted lists and return it as one sorted list
Solution: O(n1+n2+..+nk)

Algorithm:
    **VERY IMPORTANT DATA STRUCTURE: PriorityQueue in use**
    0) Initialize a dummy head and an iterator pointing to the dummy head
    1) Load the priority queues with the heads of each of the lists, with
    element being (node.val, node). The PQ will take care of sorting it in the
    increasing order (mostly using min heap)
    2) Repeat until the PQ is empty:
    a) Dequeue the PQ and insert the node into the new list using the iterator
    b) Update the iterator
    c) Update the node as node.next and if it is not None, move it into the PQ
    
Here, Python throws an exception that the ListNode is not comparable if you try
to push (node.val, node) into the PQ. So, instead push the List head index i.e
the position of the listhead node in the list of listheads instead of the node.
While performing 2c, update the original listhead stored in the list of lists
using the listhead index
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from queue import PriorityQueue
        pq = PriorityQueue()
        dummy_head = ListNode(0)
        list_iter = dummy_head
        for index, list_node in enumerate(lists):
            if list_node is not None:
                pq.put((list_node.val, index))
        while not pq.empty():
            val, out_node_idx = pq.get()
            list_iter.next = ListNode(lists[out_node_idx].val)
            lists[out_node_idx] = lists[out_node_idx].next
            list_iter = list_iter.next
            if lists[out_node_idx] is not None:
                pq.put((lists[out_node_idx].val, out_node_idx))
        return dummy_head.next