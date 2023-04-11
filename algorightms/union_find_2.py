"""
This is an improved way to tackle union find, here we consider one connected group as 
one tree. Each element contains its parent's value, or they have their own value if they are 
a root element. So initially, all elements are separate disconnected trees, 
and are their own parent and their own root. 

Then to union 2 elements, we make one element's root a child of the other element's root.

To find whether 2 elements are connected, we just check whether they have the same roots or not.
"""

class UF_1:
    def __init__(self, num_objects) :
        """create an array with num_objects elements, 
            the index value is the element name, 
            the value at that position parent of the element,
            Initialize all the values same as the index"""

        self.parent = [i for i in range(num_objects) ]
    
    
    def get_root(self, p) :
        """
            Get the root of an element :
            we will go to that element's parent, then it's parent, then it's parent and so on 
            until we find an element whise parent is itself, which will be the root element that 
            we need"""
        
        el = p

        while el != self.parent[el] :
            el = self.parent[el]

        return el
        

    
    def union(self, p, q) :
        """Connect 2 elements p and q : 
           We take the roots of both the elements p and q, and make one root, child of another root,
           this way, p and q will be connected"""
        
        root_p = self.get_root(p)
        root_q = self.get_root(q)
        self.parent[root_p] = root_q


    def is_connected(self, p, q) :
        """Return True if p and q are connected, otherwise return False :
            We get the roots of both p and q, then we check if the roots are the same, 
            which would confirm if they are parts of the same tree or not"""

        root_p = self.get_root(p)
        root_q = self.get_root(q)

        return root_p == root_q

        

    def show_array(self) :
        """show all elements in the array"""

        for i in self.parent :
            print(i, ' ', end = '')
        
        print('\n')


if __name__ == "__main__" :

    uf = UF_1(10)

    uf.show_array()

    uf.union(4, 3)
    uf.show_array()

    uf.union(3, 8)
    uf.show_array()

    uf.union(6, 5)
    uf.show_array()
    
    uf.union(9, 4)
    uf.show_array()

    uf.union(2, 1)
    uf.show_array()

    print(uf.is_connected(3, 4))
    print(uf.is_connected(6, 4))
    print(uf.is_connected(8, 9))
    print(uf.is_connected(5, 4))

    uf.union(5, 0)
    uf.show_array()

    uf.union(7, 2)
    uf.show_array()

    uf.union(6, 1)
    uf.show_array()

    uf.union(7, 3)
    uf.show_array()