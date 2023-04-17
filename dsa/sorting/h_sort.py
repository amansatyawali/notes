import random
from utils import is_sorted, create_random_int_array, less, swap


def h_sort(arr, n, h) :
    """
    This is h-sort, this takes elements at a gap of h and sorts them
    """
    for i in range(h, n) :
        j = i 
        while j - h >= 0 :
            if less(arr[j], arr[j - h]) :               #Element we compare with is at the position h steps back from the current one
                swap(arr, j, j - h)
            j -= h

    return arr


if __name__ == "__main__" :
        
    ARRAY_SIZE = 20
    arr = create_random_int_array(ARRAY_SIZE)

    print(arr)
    print(h_sort(arr, ARRAY_SIZE, h = 4))

