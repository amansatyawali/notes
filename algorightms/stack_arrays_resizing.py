"""
This is an implementation of stacks using arrays that supports resizing
We just declare a new array with double the size of the previous array when the array gets full, and copy 
the elements of the current array to the new larger array.
Similarly, when the stack size reaches **QUARTER** of the current array length, we declare a new array with half
the size of the current array and copy all the elements of the stack to the new smaller array.
"""

class Stack :
    
    def __init__(self) :
        self.head = -1
        self.arr = [-1]
        self.size = 1

    def __show_array__(self) :
        print(self.arr)

    def __upsize__(self) :
        old_size = self.size
        new_size = old_size * 2
        new_arr  = [-1] * new_size
        for i in range(self.head + 1) :
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.size = new_size
    

    def __downsize__(self) :
        old_size = self.size
        new_size = old_size // 2
        new_arr  = [-1] * new_size

        for i in range(self.head + 1) :
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.size = new_size


    def __upsize__(self) :
        old_size = self.size
        new_size = old_size * 2
        new_arr  = [-1] * new_size
        for i in range(len(self.arr)) :
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.size = new_size


    def push(self, val) :
        if self.head == self.size - 1 :         #Checking if we have reached the end of the array
            self.__upsize__()
        self.head += 1
        self.arr[self.head] = val
        return


    def pop(self) :
        if self.head == -1 :
            print('Cannot remove, stack already empty')
            return
        old_head = self.head
        self.arr[self.head] = -1 #This is just used for understanding while displaying the whole array, garbage collection is automatic in python
        self.head -= 1


        if self.head < self.size / 4 :
            self.__downsize__()
        return self.arr[old_head]


    def show(self) :
        arr = []
        for i in range(self.head + 1) :
            arr.append(str(self.arr[i]))
        print(' -> '.join(arr))
                    

if __name__ == "__main__" :
    
    stack = Stack()

    stack.push(5)
    stack.push(4)
    stack.push(3)
    stack.push(2)
    stack.push(1)
    stack.pop()
    stack.pop()
    stack.push(1)
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    stack.__show_array__()

    stack.show()