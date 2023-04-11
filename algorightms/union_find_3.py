"""
This is an improvement over the quick union find :
1. While doing a union, we choose which root will become the parent of the other root, we check the size of
each tree first, and the smaller tree's root's parent is changed to the root of the larger tree, this prevents 
the formiong of very tall trees, and hence reduces the time for quick find.

2. While finding the root of an element, we point that element to its grandparent, this flattens the tree a little bit.
Note that if an element's parent is the root, its parent will still be the root as the root is its own parent as well.

    (We can do other optimizations like replacing all the elements' parents with the root for all elements that we come across
    while finding the root, this will flatten the tree even more, but will increase the space requirement as we will have to
    store all the elements that we came across until we find the root.)
"""

class UF_1:
    def __init__(self, num_objects) :
        """"""

        self.parent = [i for i in range(num_objects)]
        self.size = [1 for i in range(num_objects)]
    
    
    def get_root(self, p) :
        """
            Get the root of an element :
            we will go to that element's parent, then it's parent, then it's parent and so on 
            until we find an element whise parent is itself, which will be the root element that 
            we need"""
        
        el = p

        while el != self.parent[el] :

            """This next line is an improvement, which replaces the parent of an element to its grandparent
                for all the elements it comes across. This flattens the tree a little bit.
                Note that if an element's parent is the root, its parent will still be the root 
                as the root is its own parent as well"""
            self.parent[el] = self.parent[self.parent[el]]

            el = self.parent[el]

        return el
        

    
    def union(self, p, q) :
        """
            Join 2 elements p and q :
            first we compare which of the 2 trees are bigger, then we replace the smaller tree's root's parent
            by the root of the larger tree, and increase the size of the larger tree by the size of the smaller tree.
        """
        
        root_p = self.get_root(p)
        root_q = self.get_root(q)

        size_p = self.size[root_p]
        size_q = self.size[root_q]

        if size_p < size_q :
            self.parent[root_p] = root_q
            self.size[root_q] += self.size[root_p]
        
        else :
            self.parent[root_q] = root_p
            self.size[root_p] += self.size[root_q]

        


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

    print(uf.size)
    print(sum(uf.size)/len(uf.size))
