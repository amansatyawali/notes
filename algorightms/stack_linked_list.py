class Node :
 
    def __init__(self, val) :

        self.val = val
        self.next = None

class Stack :
    
    def __init__(self) :
        
        self.head = None
        self.size = 0

    def push(self, val) :
        
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
        return


    def pop(self) :
        
        if self.size == 0 :
            print('Cannot remove, stack already empty')
            return

        old_head = self.head
        self.head = self.head.next

        self.size -= 1
        return old_head.val

    def show(self) :

        arr = []

        if self.head == None :
            print('Stack is empty')
            return

        else :
            node = self.head
            while True:
                arr.append(str(node.val))
                if node.next == None :
                    break
                node = node.next
        print(' -> '.join(arr))
                    

if __name__ == "__main__" :
    
    stack = Stack()

    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.pop()
    stack.pop()
    stack.push(1)
    stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()

    stack.show()