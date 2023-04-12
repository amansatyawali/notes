class Node :
 
    def __init__(self, val) :

        self.val = val
        self.next = None

class LinkedList :
    
    def __init__(self) :
        
        self.head = None
        self.size = 0

    def add(self, val) :
        
        new_node = Node(val)
        if self.head == None :
            self.head = new_node
        else :
            node = self.head
            while True :
                if node.next == None :
                    break
                node = node.next
            node.next = new_node

        self.size += 1
        return


    def remove(self) :
        
        if self.size == 0 :
            print('Cannot remove, list already empty')
            return

        node = self.head

        if node.next == None :
            self.head = None
        else :
            while node.next.next != None :
                node = node.next
            node.next = None

        self.size -= 1

    def show(self) :

        arr = []

        if self.head == None :
            print('List is empty')
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
    
    ll = LinkedList()

    ll.add(5)
    ll.add(4)
    ll.add(3)
    ll.add(2)
    ll.remove()
    ll.remove()
    ll.add(1)
    ll.remove()
    ll.remove()
    ll.remove()
    ll.remove()
    ll.remove()



    ll.show()