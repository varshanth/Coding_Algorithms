def partition(array, left, right):
    pivot_idx = left
    pivot = array[pivot_idx]
    left_mark = left+1
    right_mark = right
    while True:
        while array[left_mark] < pivot and left_mark < right:
            # Keep moving right until an element is GREATER than pivot
            left_mark +=1
        while array[right_mark] >= pivot and right_mark > left:
            # Keep moving left until an element is LESSER than pivot
            right_mark -= 1
        if left_mark >= right_mark:
            '''
            When left mark overlaps or surpasses right mark, all elements are
            partitioned with respect to the pivot
            '''            
            break
        else:
            '''
            We stopped early, it means there are elements to be ordered with
            respect to the pivot
            '''
            array[left_mark], array[right_mark] = array[right_mark], array[left_mark]
    '''
    After complete ordering with respect to pivot, swap pivot (first element)
    and the last element which is lesser than the pivot element
    '''
    array[right_mark], array[pivot_idx] = array[pivot_idx], array[right_mark]
    return right_mark

def quick_select(array, left, right, k):
    if left == right:
        # 1 element in partitioned block
        return array[left]
    partition_idx = partition(array, left, right)
    '''
    Partition index will return the index of the array to which all the left
    elements are lesser than the value at the partition index.
    Distance from left will give the distance of partition index from left
    '''
    dist_from_left = partition_idx - left +1
    if dist_from_left == k:
        return array[partition_idx]
    elif dist_from_left < k:
        # |-----partitionidx|----k-------|
        return quick_select(array, partition_idx +1, right, k - dist_from_left)
    else:
        # |----k--------|partitionidx----|
        return quick_select(array, left, partition_idx -1, k)

if __name__ == '__main__':
    _array = [4,5,1,9,8,6,3]
    k = int(input('Array = {0}. Choose k\n'.format(_array)))
    _k_ = quick_select(_array, 0, len(_array) -1, k)
    print('{0}(st|nd|th) Smallest Element = {1}'.format(k, _k_))