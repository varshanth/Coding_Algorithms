'''
Quick Sort in its general form is an in-place sort (i.e. it doesn’t require any
extra storage) whereas merge sort requires O(N) extra storage, N denoting the
array size which may be quite expensive. Allocating and de-allocating the extra
space used for merge sort increases the running time of the algorithm.

Comparing average complexity we find that both type of sorts have O(NlogN)
average complexity but the constants differ. For arrays, merge sort loses due
to the use of extra O(N) storage space.

Most practical implementations of Quick Sort use randomized version.
The randomized version has expected time complexity of O(nLogn). The worst case
is possible in randomized version also, but worst case doesn’t occur for a
particular pattern (like sorted array) and randomized Quick Sort works well in
practice.

Quick Sort is also a cache friendly sorting algorithm as it has good locality
of reference when used for arrays.

Quick Sort is also tail recursive, therefore tail call optimizations is done.
'''


# Randomized Pivot Quick Sort
import random

def partition(array, left, right):
    print('Partition: Left {0} Right {1}'.format(left, right))
    pivot_idx = random.randint(left, right)
    print('PVT IDX = {0}'.format(pivot_idx))
    array[left], array[pivot_idx] = array[pivot_idx], array[left]
    pivot_idx = left
    pivot = array[pivot_idx]
    left_mark = left + 1
    right_mark = right
    while True:
        while array[left_mark] < pivot and left_mark < right:
            left_mark += 1
        while array[right_mark] >= pivot and right_mark > left:
            right_mark -= 1
        if left_mark >= right_mark:
            break
        else:
            array[left_mark], array[right_mark] = array[right_mark], array[left_mark]
    array[right_mark], array[pivot_idx] = array[pivot_idx], array[right_mark]
    print('After Partition: Array = {0}'.format(array))
    print('Left Mark: {0} Right Mark: {1}'.format(left_mark, right_mark))
    return right_mark

def quick_sort(array, left, right):
    if left >= right:
        return
    partition_idx = partition(array, left, right)
    quick_sort(array, left, partition_idx-1)
    quick_sort(array, partition_idx+1, right)
    
arr = [4,1,5,2,9,0,8,3,7]
quick_sort(arr, 0, len(arr)-1)
print('After Sorting, Array = {0}'.format(arr))