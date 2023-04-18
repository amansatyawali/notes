import random
from utils import is_sorted, create_random_int_array, less, swap


def h_sort(arr, n, h) :
    """
    This is h-sort, this takes elements at a gap of h and sorts them, using the insertion sort logic.
    So the only difference is instead of comparing and swapping the current element with the previous element, 
    we compare the current element with h steps back, we do this for each element from index h to n-1
    """
    for i in range(h, n) :
        j = i
        while j - h >= 0 :
            if less(arr[j], arr[j - h]) :               #Element we compare with is at the position h steps back from the current one
                swap(arr, j, j - h)
            else :
                break
            j -= h
    print('h-sort complete for h=', h)
    return arr


if __name__ == "__main__" :
        
    ARRAY_SIZE = 20
    arr = create_random_int_array(ARRAY_SIZE)

    print(arr)
    print(h_sort(arr, ARRAY_SIZE, h = 4))

