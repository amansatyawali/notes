class Node :
 
    def __init__(self, val) :

        self.val = val
        self.next = None

class Queue :
    
    def __init__(self) :
        
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, val) :
        
        new_node = Node(val)
        if self.head == None :
            self.tail = new_node
            self.head = new_node
        else :
            self.head.next = new_node
            self.head = self.head.next
        self.size += 1
        return


    def pop(self) :
        
        if self.head == None :
            print('Cannot remove, Queue already empty')
            return
        
        old_tail = self.tail
        if self.tail == self.head :
            self.tail = None
            self.head = None
        else :
            self.tail = self.tail.next

        self.size -= 1
        return old_tail.val

    def show(self) :

        arr = []

        if self.head == None :
            print('Queue is empty')
            return

        else :
            node = self.tail
            while node != None :
                arr.append(str(node.val))
                node = node.next
        print(' -> '.join(arr))
                    

if __name__ == "__main__" :
    
    queue = Queue()

    queue.push(5)
    queue.push(4)
    queue.push(3)
    queue.push(2)
    queue.pop()
    queue.pop()
    queue.push(1)
    queue.pop()
    queue.pop()
    queue.pop()
    queue.pop()
    queue.push(3)
    queue.push(2)
    # queue.pop()

    queue.show()