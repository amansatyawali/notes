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
    arr = [0] * ARRAY_SIZE

    for idx in range(ARRAY_SIZE) :
        arr[idx] = random.randint(0, 1000)

    print(arr)
    print(h_sort(arr, ARRAY_SIZE, h = 4))

