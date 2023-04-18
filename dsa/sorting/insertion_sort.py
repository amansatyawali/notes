import time
from utils import is_sorted, create_random_int_array, less, swap

def insertion_sort(arr, n) :
    for i in range(1, n) :
        for j in range(i, 0 , -1) :
            if less(arr[j], arr[j-1]) :
                swap(arr, j, j - 1)
            else :
                break
    return arr


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    start_time = time.time()
    insertion_sort(arr, len(arr))
    end_time = time.time()

    print('time take = ', end_time - start_time)
    print(is_sorted(arr, ARRAY_SIZE))