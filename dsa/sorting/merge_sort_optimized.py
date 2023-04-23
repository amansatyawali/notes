import time
from utils import is_sorted, create_random_int_array, less, swap


def merge(arr, aux, first , mid, last ) :
    """
    This is a modified merge for merge sort, so that we can also pass the pointer of the auxiliary array so that
    there is no need for a new array creation in every recursive call.
    Arguments :
        arr : Array that contains the 2 sub arrays
        aux : Pointer for auxiliary array
        first : index of the start of the first sub array
        mid : index of the start of the second sub array (index of the last element of first sub array should be mid-1)
        last : index of the last element of the second sub array
    """
    if less(arr[mid - 1], arr[mid]) :        #Checking if the last element of the first subarray is less than the first element 
        return arr                           # of the second array (that would mean the array is already sorted) 
    for i in range(first, last + 1) :
        aux[i] = arr[i]                      # Instead of copying the entire array values into auxiliary, we only copy the part if the array that neets to be sorted
    i = first
    j = mid
    k = first
    while True:
        if i == mid :           #Check if all the elements of the first sub array have been added to the main array
            arr[k] = aux[j]
            j += 1
        elif j > last:          #Check if all the elements of the second sub array have been added to the main array
            arr[k] = aux[i]
            i += 1
        elif less(aux[i], aux[j]) :
            arr[k] = aux[i]
            i += 1
        else : 
            arr[k] = aux[j]
            j += 1
        k += 1
        if k > last :
            break
    return arr


def selection_sort_subarray(arr, n, start_index, end_index) :
    """
    This is a modified selection sort that we use, to optimize merge sort, this function only sorts within the given indices
    """
    if start_index < 0 or end_index > n - 1 :
        raise ValueError
    
    for i in range(start_index, end_index + 1) :
        smallest_idx = i
        for j in range(i+1, end_index + 1) :
            if less(arr[j], arr[smallest_idx]) :
                smallest_idx = j
        swap(arr, i, smallest_idx)
    return arr


def sort(arr, aux, first, last) :
    if first == last :
        return [arr[first]]
    elif last - first < 32   :           #To check whether the array we want to sort is <= 8, then we just use selection sort
        return selection_sort_subarray(arr, len(arr),start_index = first, end_index = last)
    else :
        mid = first + (last - first) // 2
        sort(arr, aux, first, mid)
        sort(arr, aux,  mid + 1, last)
        res = merge(arr, aux, first, mid  + 1, last)
        return res
    

def merge_sort(arr, first, last) :
    aux = arr.copy()
    return sort(arr, aux, first, last)


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    # arr = [8, 7, 6, 5, 4, 3, 2, 1]
    start_time = time.time()
    merge_sort(arr, 0, ARRAY_SIZE - 1)
    end_time = time.time()
    print('time take = ', end_time - start_time)
    print(is_sorted(arr, ARRAY_SIZE))