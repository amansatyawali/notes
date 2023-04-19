import time
from utils import is_sorted, create_random_int_array, less
from merge import merge

def merge_sort(arr, first, last) :
    # print('beginning first, last -> ', first, last)
    if first == last :
        # print('returning ', [arr[first]])
        return [arr[first]]
    else :
        mid = first + (last - first) // 2
        # print('recalling - > ', first, mid, last)
        time.sleep(2)
        merge_sort(arr, first, mid)
        merge_sort(arr, mid + 1, last)
        res = merge(arr, first, mid  + 1, last)
        # print('returning', res)
        return res


if __name__ == "__main__" :
    ARRAY_SIZE = 4
    arr = create_random_int_array(ARRAY_SIZE)
    print(arr)
    merge_sort(arr, 0, ARRAY_SIZE - 1)
    print(arr)

    print(is_sorted(arr, ARRAY_SIZE))