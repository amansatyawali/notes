import time
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


def shell_sort(arr, n) :
    """
    This is Shell sort, it repeatedly runs h-sort on the array, starting from a large value of h, decreasing it
    every time until we sort with h=1, which essentially is insertion sort. 
    To select the h values we are using Knuth formula that starting from h=1, we do h = h * 3 + 1, until h is 
    larger or equal to n
    """
    h_vals = []
    h = 1
    while h < n :
        h_vals.append(h)
        h = h * 3 + 1
    print(h_vals)
    for h in h_vals[::-1] :
        h_sort(arr, n, h)
    return arr


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    start_time = time.time()
    shell_sort(arr, ARRAY_SIZE)
    end_time = time.time()

    print('time take = ', end_time - start_time)
    print(is_sorted(arr, ARRAY_SIZE))