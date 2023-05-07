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

Merge sort :

    We divide the array into half, then each half into 2 halves, then those 4 sub arrays into their halves and so on, until
    each subarray is just one element. So then, that each element is not sorted, then we start joining the halves back, 
    but we create an auxiliary array similar to the main array and then merge the 2 halves together into a sorted array using that auxiliary array, we do this operation of merging halves back till the top.
    At the end we have one complete sorted array
    
    The time complexity of this sort is O(Nlog(N)), in best average and worst case 
    Since in every merge function, we change the values of the auxiliary array only for the part that we are merging for, so at each level, total value changes in auxiliary array are N
    Also, the merge itself takes N array accesses, for all the merge calls at one level combined.

    And there are log(N) levels for an array of N elements as we will need maximum of log(N) divisions by 2 to half the array 
    repeatedly until we get a single element in each array.
    
    The space complexity is O(N) since, the only extra space we need is the auxiliary array which is the same size of the main array


    Optimizations :
        -> While merging, since we know that the 2 sub arrays are sorted, we can check at the beginning, 
            if last element of first array < the first element of the second array
            If that is true, that would mean that the combind array is already sorted and there is no need to merge.

        -> Since the operation of a recursive call is expensive in itself, it is better to sort using recursion for 
            sorting only large arrays, if the array is small enough, we can just use selection sort to sort that small 
            sub array, so we don't have to make a recursive call for sorting small arrays.
            (After testing, I found that using selection sort for an array of length <= 8 worked best for me)


##Stability :
    If we use a sorting algorithm to sort the data on one column, then we sort it on another column of the same data, 
    It should still be sorted by the first column.

    Insertion sort, merge sort are stable
        Merge sort is stable if merge operation is stable.
        Which can be if we use the condition that if both column 2 keys are equal during merging, we take value from the left.
        Because the left sub array's value of column 1 will be smaller since the main array was already sorted on column1 values
    Selection sort and shell sort are not stable
        Think that in selection sort, while we check the smallest for the element at index i, when we swap the el at ith index, it can
        be moved  to any place in the array which could disturb the order
        For h sort, we check and swap between some gaps, so it is possible that there is another value in between the gap that has same 
        value in the ith column, so the order might be disrupted.
    It is diffictult to type how to check these above algorithms in more detail, maybe some day.
