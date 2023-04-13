class Queue :
    
    def __init__(self, capacity) :
        
        self.head = -1
        self.tail = -1
        self.arr = [-1] * capacity
        self.max_arr_size = capacity

    def enqueue(self, val) :
        if (self.head + 1) % self.max_arr_size == self.tail :
            print('Cannot push, queue is full')
        if self.head == -1 :        #Checking if the queue is empty
            self.head = 0
            self.tail = 0
        else :
            self.head = (self.head + 1) % self.max_arr_size    # Next position for head will be the first position of the array if the array has reached its max capacity
        self.arr[self.head] = val
        return


    def dequeue(self) :
        
        if self.head == -1 :        # Tail will also be -1 in this case
            print('Cannot remove, queue already empty')
            return
        else : 
            old_tail_val = self.arr[self.tail]
            self.arr[self.tail] = -1 #This is just used for understanding while displaying the whole array, garbage collection is automatic in python
            if self.tail == self.head :
                self.tail = -1
                self.head = -1
            else :
                self.tail = (self.tail + 1) % self.max_arr_size
            return old_tail_val

    def show(self) :

        arr = []
        if self.tail == -1 :
            print('Queue is empty')
            return
        idx = self.tail
        while True :
            arr.append(str(self.arr[idx]))
            if idx == self.head :
                break
            else :
                idx = (idx + 1) % self.max_arr_size

        print(' -> '.join(arr))
                    

if __name__ == "__main__" :
    
    queue = Queue(10)

    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(1)
    # print(queue.dequeue())
    # print(queue.dequeue())
    queue.enqueue(1)
    # print(queue.dequeue())
    # print(queue.dequeue())
    queue.enqueue(5)
    queue.enqueue(4)
    queue.enqueue(3)
    queue.enqueue(2)
    print(queue.dequeue())
    print(queue.dequeue())
    queue.enqueue(6)
    queue.enqueue(7)

    print(queue.arr)
    queue.show()