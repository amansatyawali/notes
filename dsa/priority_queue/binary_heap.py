class MaxPQ:
    N = None
    pq = None
    max_size = None


    def __init__(self, size):
        """Initializes a priority queue of size N"""

        self.pq = [-1] * (size + 1)
        self.N = 0
        self.max_size = size        


    def show(self):
        for idx in range(1, self.N + 1):
            print(self.pq[idx])

        print(self.pq)


    def is_empty(self):
        return self.N == 0


    def greater(self, i, j):
        return self.pq[i] > self.pq[j]

    
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
            elif l_child is not None and r_child is not None and self.greater(l_child, idx) and self.greater(l_child, r_child):
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



pq = MaxPQ(10)

pq.insert(20)
pq.insert(30)
pq.insert(40)
pq.del_max()
pq.insert(60)
pq.del_max()
pq.insert(50)
pq.insert(25)
pq.insert(70)
pq.del_max()
pq.insert(10)
pq.show()
