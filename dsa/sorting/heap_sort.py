import time
from utils import is_sorted, create_random_int_array


class MaxPQ:
    N = None
    pq = None
    max_size = None
    sorted_array = None


    def show(self):
        print(self.pq)


    def is_empty(self):
        return self.N == 0


    def greater(self, i, j):
        return self.pq[i] > self.pq[j]
    

    def greater_or_equal(self, i, j):
        return self.pq[i] >= self.pq[j]

    
    def swap(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    
    def parent(self, idx):
        if idx == 1:
            return None
        else:
            return int(idx/2)
        
    
    def children(self, idx):
        l_child = idx*2
        r_child = idx*2 + 1
        
        if l_child > self.N:
            l_child = None
        if r_child > self.N:
            r_child = None

        return l_child, r_child

    
    def swim(self, idx):
        while idx != 1:
            if self.greater(idx, self.parent(idx)):
                self.swap(idx, self.parent(idx))
                idx = self.parent(idx)
            else:
                break


    def sink(self, idx):
        while idx <= self.N:
            l_child, r_child = self.children(idx)
            if r_child is None and l_child is not None and self.greater(l_child, idx):         #we only need to check if (r_child is null and l_child is not none) because if l_child is null, thien r_child will also be null since it is a complete binary tree
                self.swap(idx, l_child)
                idx = l_child
            elif l_child is not None and r_child is not None and self.greater(l_child, idx) and self.greater_or_equal(l_child, r_child):                #used greater_or_equal because in case both children are equal, but bigger than the curr node, then we have to pick one
                self.swap(idx, l_child)
                idx = l_child
            elif l_child is not None and r_child is not None and self.greater(r_child, idx) and self.greater(r_child, l_child):
                self.swap(idx, r_child)
                idx = r_child
            else:
                break


    def insert(self, key):
        if self.N == self.max_size:
            raise IndexError("Cannot insert, max_size already reached")
        else:
            self.N += 1
            self.pq[self.N] = key
            self.swim(self.N)

    
    def del_max(self):
        if self.N == 0:
            raise IndexError("Cannot delete, heap already empty")
        max = self.pq[1]
        self.swap(1, self.N)
        self.N -= 1
        self.sink(1)
        return max

    
    def heap_sort(self):
        for i in range(self.max_size):
            self.sorted_array[i] = self.del_max()
        

    def _convert_to_max_heap(self, arr):
        self.pq =  [0] + arr
        self.N =  len(arr)
        self.max_size = len(arr)
        self.sorted_array = [-1]*len(arr)                               #this sorted array will be used when we eventually sort the array using heap sort

        for idx in range(self.parent(self.N), 0, -1):                   #We start with N/2 because the first little heap with any non null children will be the parent of the last node
            l_child, r_child = self.children(idx)
            if l_child is not None or r_child is not None:
                self.sink(idx)


    def __init__(self, arr):
        """Initializes a priority queue of size N"""
        self._convert_to_max_heap(arr)


if __name__ == "__main__" :
    ARRAY_SIZE = 10000
    arr = create_random_int_array(ARRAY_SIZE)
    start_time = time.time()
    pq = MaxPQ(arr)
    pq.heap_sort()
    arr = pq.sorted_array[::-1]
    end_time = time.time()

    print('time take = ', end_time - start_time)

    print(is_sorted(arr, ARRAY_SIZE))