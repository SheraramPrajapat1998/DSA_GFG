# Q. Implement queue using two stacks?

class Queue:
    def __init__(self):
        self.instack = []
        self.outstack = []

    def is_empty(self):
        return len(self.instack) == 0

    def enqueue(self, data):
        return self.instack.append(data)
    
    def dequeue(self):
        if self.is_empty():
            print("Stack is already empty. Can't perform dequeue.")
            return
        while(not self.is_empty() and self.outstack):
            
            
        return self.instack.pop(0)

    def front(self):
        if self.is_empty():
            return
        return self.instack[0]
    


if __name__ == "__main__":
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    q.enqueue(8)
    print(q.front())
    print(q.dequeue())
    print(q.front())
