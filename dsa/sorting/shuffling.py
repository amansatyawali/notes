import random

def swap(arr, i, j) :
    """
    This can act as a generic funtion that would swap elements at 2 given indices
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def shuffle(arr, n) :
    """
    Shuffle the array elements :
    We start from the beginning, take a random index from the 0 to i, then swap this current element with the element at
    that random position
    Note : We include i in the candidates for the random position because the element should also get an equal chance
        to stay at the same position as much as the chance to be swapped with any other element
    Note : We get the random position from 0 to i, instead of 0 to n-1 because choosing from 0 to n-1 does not give uniformly
        random results
    """
    for i in range(n) :
        position = random.randint(0, i)
        swap(arr, i, position)
    return arr


if __name__ == "__main__" :
    size = 20
    arr = [i for i in range(size)]

    print(arr)
    shuffle(arr, size)
    print(arr)