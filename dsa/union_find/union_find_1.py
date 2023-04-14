"""
This is the first try for union find. 
The time complexity for is_connected is O(1), 
but the time complexity for union is n^2 because we have to access 
each element in the array once during the union operation.
"""

class UF_1:
    def __init__(self, num_objects) :
        """create an array with num_objects elements, 
            the index value is the element name, 
            the value at that position is the element that it is connected to,
            Initialize all the values same as the index"""

        self.arr = [i for i in range(num_objects) ]
    
    def union(self, p, q) :
        """Connect 2 elements p and q : 
            all the elements with the values same as p, their will change to the value at q """

        p_val = self.arr[p]
        q_val = self.arr[q]

        for idx, i in enumerate(self.arr) :
            if i == p_val :
                self.arr[idx] = q_val

    def is_connected(self, p, q) :
        """Return True if p and q are connected, otherwise return False :\
            if the 2 elements have the same values at the indices p and q, return True else, return False"""
        
        return self.arr[p] == self.arr[q]

    def show_array(self) :
        """show all elements in the array"""

        for i in self.arr :
            print(i, ' ', end = '')
        
        print('\n')


if __name__ == "__main__" :

    uf = UF_1(10)

    uf.show_array()
    uf.union(3, 4)
    uf.show_array()
    print(uf.is_connected(3, 4))
    print(uf.is_connected(6, 4))
