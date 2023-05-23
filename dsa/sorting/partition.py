from utils import is_sorted, create_random_int_array, less, swap

def is_partitioned(prtitn_el, res):
    prtitn_el_found = False
    for i in res:        
        if i == prtitn_el:
            prtitn_el_found = True

        if (i >= prtitn_el and not prtitn_el_found) or (i < prtitn_el and prtitn_el_found):
            return  False

    return True


def partition(arr, first, last) :
    prtitn_el = arr[first]
    i = first + 1
    j = last

    while True:
        while prtitn_el > arr[i]:
            if i == last:
                break
            i += 1

        while prtitn_el < arr[j]:
            if j == first:
                break
            j -= 1
        if i >= j:
            break
        swap(arr, i, j)
    swap(arr, first, j)
    return arr

if __name__ == "__main__" :
    

    for i in range(1000):
        arr = create_random_int_array(10)
        partition_val = arr[0]
        # print(arr)
        partition(arr, first = 0, last = 9)
        # print(arr)
        if not is_partitioned(partition_val, arr):
            print("False")
        # print(is_partitioned(partition_val, arr))