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


if __name__ == "__main__" :
    arr = [6, 5, 4, 3, 2, 1]

    print(selection_sort(arr, len(arr)))