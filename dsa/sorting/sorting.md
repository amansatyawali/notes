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