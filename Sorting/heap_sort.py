'''
##############################################################################
1) Treat array as tree:
    a b c d e f g h  ->
    0 1 2 3 4 5 6 7
    
          a(0)
        /      \
     b(1)      c(2)
     / \       /  \
  e(3) f(4)  g(5)  h(6)
  
2) The children of node at index i = 2i + 1 and 2i + 2
3) Heapifying a tree means to construct a binary tree in which the children
   of all parent nodes are lesser[min heap] (or greater [max heap]) than the
   parent node
4) If we heapify a tree bottom up, we will get the min (or max) element as the
   1st element (or root node)
5) To heapsort, just swap the 1st element (best) with the last element (one of
   the two worst) after heapification and then pop the last element
   (assign last = last -1) and heapify again
   
##############################################################################   
Although QuickSort works better in practice, the advantage of HeapSort worst
case upper bound of O(nLogn).

MergeSort also has upper bound as O(nLogn) and works better in practice when
compared to HeapSort. But MergeSort requires O(n) extra space

HeapSort is not used much in practice, but can be useful in real time (or time
bound where QuickSort doesn’t fit) embedded systems where less space is
available (MergeSort doesn’t fit)
##############################################################################
'''

## Min Heap: Descending order sort ##
def heapify(array, start, end):
    # Assume Start is the root node of the subtree
    # Left Child Index
    l_idx = 2 * start + 1
    # Right Child Index
    r_idx = 2 * start + 2
    # Always assume the root node passed is the min
    min_idx = start
    if l_idx < end and array[l_idx] < array[min_idx]:
        min_idx = l_idx
    if r_idx < end and array[r_idx] < array[min_idx]:
        min_idx = r_idx
    if min_idx != start:
        array[min_idx], array[start] = array[start], array[min_idx]
        # Heapify children if parent was swapped
        heapify(array, min_idx, end)

def heapsort(array):
    end = len(array)
    start = end - 1
    print('Initial Heapify')
    for i in range(start, -1, -1):
        heapify(array, i, end)
        print('Idx {0}: Array: {1}'.format(i, array))
        
    print('After Initial Heapify: {0}'.format(array))
    print('Swap, Pop, Heapify, Repeat')
    # End idx is 1 [end-1, 0) since there is no point heapifying 1 element
    for i in range(end-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        print('After Swap: Idx {0}: Array: {1}'.format(i, array))
        print('Popped Element: {0}'.format(array[i]))
        # Heapify after assigning one of the 2 worse elements as the new root
        # Hence pushing the best to the root and the worst to the last leaf
        heapify(array, 0, i)
        
array = [2, 7, 1, -2, 56, 5, 3]
heapsort(array)
print(array)