import time
import random

def less(a, b) :
    """
    This can act as a generic funtion to check which of the 2 elements is smaller
    """
    return a < b 

def swap(arr, i, j) :
    """
    This can act as a generic funtion that would swap elements at 2 given indices
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(arr, n) :

    for i in range(n - 1) :
        smallest_idx = i
        for j in range(i+1, n) :
            if less(arr[j], arr[smallest_idx]) :
                smallest_idx = j
        swap(arr, i, smallest_idx)
    return arr


def create_random_int_array(ARRAY_SIZE) :
    """
    Using the random function, we generate an array with random integers.
    """
    arr = [0] * ARRAY_SIZE

    for idx in range(ARRAY_SIZE) :
        arr[idx] = random.randint(0, 1000000)
    return arr 


def is_sorted(arr, n) :
    """
    Checks if an array is sorted or not
    """
    for i in range(1, n) :
        if(arr[i] < arr[i - 1]) :
            return False
    return True


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    start_time = time.time()
    selection_sort(arr, len(arr))
    end_time = time.time()

    print('time take = ', end_time - start_time)

    print(is_sorted(arr, ARRAY_SIZE))
