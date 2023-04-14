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


def insertion_sort(arr, n) :

    for i in range(1, n) :
        for j in range(i - 1, -1 , -1) :
            if less(arr[i], arr[j]) :
                swap(arr, i, j)

    return arr


if __name__ == "__main__" :
    arr = [6, 4, 2, 5, 2, 1]

    print(insertion_sort(arr, len(arr)))