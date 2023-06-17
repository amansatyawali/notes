class MaxPQ:
    N = None
    pq = None


    def init(self, size):
        """Initializes a priority queue of size N"""

        self.pq = [-1] * (size + 1)
        N = 0


    def is_empty(self):
        if self.N == 0:
            return True
        else:
            return False
        

    def les_or_equal(self, i, j):
        if self.pq[i] <= self.pq[j]:
            return True
        else:
            return False
        
    
    def swap(self, i, j):
        temp = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = temp

    
    def swim(self, idx):
