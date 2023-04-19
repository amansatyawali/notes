import time
from utils import is_sorted, create_random_int_array, less

def merge(arr, first , mid, last ) :
    """
    Merge 2 sorted arrays into 1 big sorted array :
    We will first copy the part of the array that we want to sort containing the 2 smaller arrays, move it to an auxiliary array, 
    then check the first item of both sorted arrays and, and move the smaller one of the 2 back to the main array, repeat these steps 
    one by one till all the elements are back in the main array.
    Arguments :
        arr : Array that contains the 2 sub arrays
        first : index of the start of the first sub array
        mid : index of the start of the second sub array (index of the last element of first sub array should be mid-1)
        last : index of the last element of the second sub array
    """
    print('arr', arr, first, mid, last)
    aux = arr[first : last + 1]
    i = first
    j = mid
    k = first
    while True:
        (print(k, i, j))
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


if __name__ == "__main__" :
    
    # arr = [2, 4, 6, 8] + [1, 3, 5, 7]
    arr = [x for x in range(1, 20, 3)] + [x for x in range(2, 20, 3)]
    print(arr)
    merge(arr, first = 0, mid = 7, last = 12)
    print(arr)
    print(is_sorted(arr, len(arr)))