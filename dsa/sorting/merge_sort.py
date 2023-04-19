import time
from utils import is_sorted, create_random_int_array, less
from merge import merge

def merge_sort(arr, first, last) :
    if first == last :
        return [arr[first]]
    else :
        mid = first + (last - first) // 2
        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        res = merge(arr, first, mid  + 1, last)
        return res


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    # arr = [4, 3, 2, 1]
    start_time = time.time()
    merge_sort(arr, 0, ARRAY_SIZE - 1)
    end_time = time.time()

    print('time take = ', end_time - start_time)

    print(is_sorted(arr, ARRAY_SIZE))