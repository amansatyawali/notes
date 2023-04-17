import random
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
        arr[idx] = random.randint(0, 1000)
    return arr 

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