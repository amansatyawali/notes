import time
from utils import is_sorted, create_random_int_array, less, swap


def selection_sort(arr, n) :

    for i in range(n - 1) :
        smallest_idx = i
        for j in range(i+1, n) :
            if less(arr[j], arr[smallest_idx]) :
                smallest_idx = j
        swap(arr, i, smallest_idx)
    return arr


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    start_time = time.time()
    selection_sort(arr, len(arr))
    end_time = time.time()

    print('time take = ', end_time - start_time)

    print(is_sorted(arr, ARRAY_SIZE))
