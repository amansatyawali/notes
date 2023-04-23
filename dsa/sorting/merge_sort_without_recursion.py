import time
from utils import is_sorted, create_random_int_array, less
from merge import merge

def merge_sort(arr, n) :
    if(n < 2) :
        return arr
    sub_array_size = 2
    while sub_array_size < n * 2 :
        i = 0
        while i < n :                                   #Making the subarrays one bye one
            first = i
            last = i + sub_array_size - 1
            mid = first + (last - first) // 2
            if mid >= n - 1:                               #If last few elements are left (which we know are sorted in previous iterations), we will not merge that part this time
                break                                   #probably, next time it will be merged, but it will be definitely be merged by the end.
            if last >= n :
                last = n - 1
            merge(arr, first, mid + 1, last)
            i += sub_array_size 
        sub_array_size *= 2
    return arr


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    # arr = [6, 5, 4, 3, 2, 1]
    # ARRAY_SIZE = 6
    start_time = time.time()
    merge_sort(arr, ARRAY_SIZE)
    end_time = time.time()

    print('time take = ', end_time - start_time)

    print(is_sorted(arr, ARRAY_SIZE))