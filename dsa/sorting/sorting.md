Requirements for sorting :
    The requirement for sorting is that there is total order present in the elements which means 3 things :
        Antisymmetry - If v <= w and w <= v, then v = w
        Transitivity - If v >= w and w >= x , then v >= x
        Totality - Either v >= w or w >= x or both


Selection sort :
    for each position starting from index 0 to n-2
        we check for the smallest element and swap it with the element at that position

    Note : If we have sorted till idx n-2, the element at idx n-1 will already be sorted
    
    This algorithm always checks the entire array to look for the smallest element in each iteration, 
    but it only makes 1 swap at max in each iteration.

    So the time complexity is quadratic (1/2 N^2) in every scenario since there are ~n accesses to the array in each iteration, and
    there are n-1 iterations, 1 for each unsorted element

    The time complexity remains the same irrespective of the order of the input

Insertion sort :
    for each position starting from index 1 to n-1
        we go backwards step by step, swapping this element with the one at the back, till the element has not reached its 
        correct position.

    Note : We start from 1 because for the first element, there is nothing to compare with in the previous positions

    This algorithm only goes back till where the correct position of the element is, so on an average it will only check for 
    half the array behind it, which is half of what selection sort needs(where we have to check every element in the remaining array
    to find the smallest element)

    But it makes ~N comparisons and ~N swaps , so each traversal takes longer than selection sort (where we were only need ~N comparisons and 1 swap)

    So, in worst case, the time complexity will be Quadratic ~(N^2), but it will be more than the time needed for selection sort, 
        since there is more operations done in each step in insertion sort(comparing and swapping) than in selection sort (only comparing) 

    For random case, number of swaps will be half of the remaining array by average, so average time complecity is (1/4 N^2)

    And in best case, where the input array is already sorted, it will sort the array in only n-1 compares and 0 swaps, so time complexity will be ~N

    Inversion :
        An inversion is just a pair of elements that are out of place in a sorted array. 
        eg - in [1, 2, 3, 6, 5, 4] , there are 3 inversions - (6, 4), (5, 4), (6, 5) 

    So number of swaps during insertion sort is equal to the number of inversions present in the input array.
    So if there are ~N inversions in the input array, the time taken by insertion sort will also be ~N. 
    Insertion sort will complete very quickly in such cases

Shell sort :
    First we see what an h-sort is :
        this compares elements at a gap of h and sorts them groupwise, using the insertion sort logic.
        So the only difference is instead of comparing and swapping the current element with the previous element, 
        we compare the current element with h steps back, we do this for each element from index h to n-1

    So in shell sort, we perform h-sort on the array repeatedly starting with a large value of h, decreasing it in
    each step, at last we perform h-sort with h=1(which is essentially an insertion sort)

    The idea is that with h-sort, some small elements are moved towards the left and larger ones are moved towards right
    With each h-sort, more and more values get closer to their correct postion.
    (It is mathematically proven that if an array is h-sorted, then g-sorted for some integers g and h, it will still remain h sorted)

    So during, the last h-sort, which is essentially an insertion sort, there will be very less swaps required as a lot of 
    elements will be close to their correct position already. This reduces the number if total steps taken to sort the array.

    The time complexity of shell sort is estimated to be around n^(3/2)

    h values :
        The h values that have shown good results are ones discovered by Knuth ie starting with h=1, we do h=h*3+1, until h is 
        larger than n 