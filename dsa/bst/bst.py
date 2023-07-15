class Node:

    def __init__(self, key, val = 0) -> None:
        self.key = key
        self.val = key**2
        self.left = None
        self.right = None
        self.subtree_size = 1

class BST:

    def __init__(self) -> None:
        self.root = None


    def traverse_preorder(self) -> None:
        self._preorder(self.root)


    def _preorder (self, curr_node) -> None:
        if curr_node is None:
            return
        
        self._preorder(curr_node.left)
        self._preorder(curr_node.right)


    def _insert_node(self, new_node, curr_node) -> Node:
        if curr_node is None:
            return new_node
        if new_node.key == curr_node.key:
            curr_node.val = new_node.val
        elif new_node.key < curr_node.key:
            curr_node.left = self._insert_node(new_node, curr_node.left)
            curr_node.subtree_size = self.size(curr_node.left) + self.size(curr_node.right) + 1
        elif new_node.key > curr_node.key:
            curr_node.right = self._insert_node(new_node, curr_node.right)
            curr_node.subtree_size = self.size(curr_node.left) + self.size(curr_node.right) + 1
        return curr_node


    def put(self, key) -> None:
        node = Node(key)
        self.root = self._insert_node(node, self.root)


    def _search(self, key, curr_node):
        if curr_node is None:
            return None
        if key == curr_node.key:
            return curr_node
        elif key < curr_node.key:
            return self._search(key, curr_node.left)
        elif key > curr_node.key:
            return self._search(key, curr_node.right)


    def get(self, key) -> int:
        return self._search(key, self.root).val
    

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


    def size(self, node) -> int:
        if node == None:
            return 0
        else:
            return node.subtree_size


    def rank(self, key) -> int:
        rank = 1
        curr_node = self.root

        while curr_node is not None:
            if key < curr_node.key:
                curr_node = curr_node.left
            elif key > curr_node.key:
                rank += self.size(curr_node.left) + 1
                curr_node  = curr_node.right
            elif key == curr_node.key:
                rank += self.size(curr_node.left)
                break

        if curr_node is None:
            return None
        else:
            return rank


    def delete_min(self) -> Node:
        self.root = self._delete_min_in_subtree(self.root)
        

    def _delete_min_in_subtree(self, node) -> Node:
        if node.left is None:
            return node.right                           # This means that if right is not present, it will return null deleting the current node, if right is not None, it will return right as the current node
        else:
            node.left = self._delete_min_in_subtree(node.left)
            node.subtree_size = self.size(node.left) + self.size(node.right) + 1
            return node                                 # This means that if left is present, in that case this node sohould return itself, so that nothing changes for this node


    def _get_min_in_subtree(self, node) -> Node:
        if node.left is None:
            return node
        else: 
            return self._get_min_in_subtree(node)


    def delete(self, key) -> None:
        self.root = self._delete_node_with_key(key, self.root)


    def _delete_node_with_key(self, key, node) -> None: 
        if node is None:
            print(f"Key {key} does not exist in the tree")
            raise ValueError
        elif key == node.key:
            if node.left is None:
                return node.right
            elif node.right is None:                    #This condition will only be true if left is not None because if it was, it would have been caught in the previous condition
                return node.left
            else:
                new_node = self._get_min_in_subtree(node.right)
                new_node.left, new_node.right = node.left, node.right
                new_node.right = self._delete_min_in_subtree(new_node.right)
                new_node.subtree_size = self.size(new_node.left) + self.size(new_node.right) + 1
                return new_node

        elif key < node.key:
            node.left = self._delete_node_with_key(key, node.left)
        elif key > node.key:
            node.right = self._delete_node_with_key(key, node.right)
        node.subtree_size = self.size(node.left) + self.size(node.right) + 1
        return node
            


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


    for i in range(0, 11):
        print(i, " -> ", bst.rank(i))

    # print(bst.get(2))
    # print(bst.min())
    # print(bst.max())
    # print(bst.floor(3.4))
    # print(bst.ceiling(3.4))