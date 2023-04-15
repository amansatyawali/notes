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


def h_sort(arr, n, h) :
    """
    This is h-sort, this takes elements at a gap of h and sorts them, using the insertion sort logic.
    So the only difference is instead of comparing and swapping the current element with the previous element, 
    we compare the current element with h steps back, we do this for each element from index h to n-1
    """
    swap_count = 0
    for i in range(h, n) :
        j = i
        while j - h >= 0 :
            if less(arr[j], arr[j - h]) :               #Element we compare with is at the position h steps back from the current one
                swap(arr, j, j - h)
                swap_count += 1
            j -= h
    print('h-sort complete for h=', h)
    print('Swap count = ', swap_count)
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


def is_sorted(arr, n) :
    """
    Checks if an array is sorted or not
    """
    for i in range(1, n) :
        if(arr[i] < arr[i - 1]) :
            return False
    return True


def create_random_int_array(ARRAY_SIZE) :
    """
    Using the random function, we generate an array with random integers.
    """
    arr = [0] * ARRAY_SIZE

    for idx in range(ARRAY_SIZE) :
        arr[idx] = random.randint(0, 1000000)
    return arr 


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    start_time = time.time()
    shell_sort(arr, ARRAY_SIZE)
    end_time = time.time()

    print('time take = ', end_time - start_time)
    # print(is_sorted(arr, ARRAY_SIZE))