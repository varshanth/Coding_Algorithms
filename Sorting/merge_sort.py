def merge(arr_l, arr_r):
    print('Merge: Left = {0} Right = {1}'.format(arr_l, arr_r))
    print('Size New = {0}'.format(len(arr_l)+len(arr_r)))
    merged = []
    l_iter = r_iter = 0
    while l_iter < len(arr_l) and r_iter < len(arr_r):
        if arr_l[l_iter] < arr_r[r_iter]:
            merged.append(arr_l[l_iter])
            l_iter += 1
        else:
            merged.append(arr_r[r_iter] )
            r_iter += 1
    if l_iter < len(arr_l):
        merged.extend(arr_l[l_iter:len(arr_l)])
    if r_iter < len(arr_r):
        merged.extend(arr_r[r_iter:len(arr_r)])
    print('Merge: Out = {0}'.format(merged))
    return merged

def merge_sort(array):
    left = 0
    right = len(array)
    print('MergeSort: Array: {0}'.format(array))
    if len(array) == 1:
        return array
    middle = int((left + right)/2)
    arr_l = merge_sort(array[left:middle])
    arr_r = merge_sort(array[middle:right])
    return merge(arr_l, arr_r)

arr = [4,1,8,3,6,0,7,5,2]
print(merge_sort(arr))