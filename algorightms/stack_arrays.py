class Stack :
    
    def __init__(self, capacity) :
        
        self.head = -1
        self.arr = [-1] * capacity

    def push(self, val) :
        
        self.head += 1
        self.arr[self.head] = val
        return


    def pop(self) :
        
        if self.head == -1 :
            print('Cannot remove, stack already empty')
            return

        old_head = self.head
        self.head = -1 #This is just used for understanding while displaying the whole array, garbage collection is automatic in python
        self.head -= 1
        return self.arr[old_head]

    def show(self) :

        arr = []

        for i in range(self.head + 1) :
            arr.append(str(self.arr[i]))

        print(' -> '.join(arr))
                    

if __name__ == "__main__" :
    
    stack = Stack(10)

    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.pop()
    stack.pop()
    stack.push(1)
    # stack.pop()
    # stack.pop()
    # stack.pop()
    # stack.pop()

    stack.show()