class Node:

    def __init__(self, key, val = 0) -> None:
        self.key = key
        self.val = key**2
        self.left = None
        self.right = None

class BST:

    def __init__(self) -> None:
        self.root = None


    def traverse_preorder(self) -> None:
        self._preorder(self.root)


    def _preorder (self, curr_node) -> None:
        if curr_node is None:
            return
        
        self._preorder(curr_node.left)
        print(curr_node.key)
        self._preorder(curr_node.right)


    def _insert_node(self, new_node, curr_node) -> Node:
        if curr_node is None:
            return new_node
        print(curr_node.key, new_node.key)
        if new_node.key == curr_node.key:
            curr_node.val = new_node.val
        elif new_node.key < curr_node.key:
            curr_node.left = self._insert_node(new_node, curr_node.left)
        elif new_node.key > curr_node.key:
            curr_node.right = self._insert_node(new_node, curr_node.right)
        return curr_node



    def put(self, key) -> None:
        node = Node(key)
        self.root = self._insert_node(node, self.root)


    def _search(self, key, curr_node):
        if curr_node is None:
            return None
        if key == curr_node.key:
            return curr_node.val
        elif key < curr_node.key:
            return self._search(key, curr_node.left)
        elif key > curr_node.key:
            return self._search(key, curr_node.right)


    def get(self, key) -> int:
        return self._search(key, self.root)
    

    def min(self) -> int:
        if self.root is None:
            return None
        
        curr_node = self.root
        min = curr_node
        while curr_node is not None:
            min = curr_node
            curr_node = curr_node.left

        return min.val
    

    def max(self) -> int:
        if self.root is None:
            return None
        
        curr_node = self.root
        max = curr_node
        while curr_node is not None:
            max = curr_node
            curr_node = curr_node.right

        return max.val
    

    def floor(self, key) -> int:

        floor = None
        curr_node = self.root

        while curr_node is not None:
            if key == curr_node.key:
                floor = curr_node
                break
            elif key < curr_node.key:
                curr_node = curr_node.left
            elif key > curr_node.key:
                floor = curr_node
                curr_node = curr_node.right

        if floor != None:
            return floor.key
        else:
            return None
    

    def ceiling(self, key) -> int:

        ceiling = None
        curr_node = self.root

        while curr_node is not None:
            if key == curr_node.key:
                ceiling = curr_node
                break
            elif key < curr_node.key:
                ceiling = curr_node
                curr_node = curr_node.left
            elif key > curr_node.key:
                curr_node = curr_node.right

        if ceiling != None:
            return ceiling.key
        else:
            return None

            



    
if __name__ == "__main__":
    bst = BST()
    bst.put(3)
    bst.put(2)
    bst.put(1)
    bst.put(6)
    bst.put(8)
    bst.put(10)
    bst.put(5)
    bst.put(9)
    bst.put(7)
    bst.put(4)
    bst.traverse_preorder()

    print(bst.get(2))
    print(bst.min())
    print(bst.max())
    print(bst.floor(3.4))
    print(bst.ceiling(3.4))


