# Q. Implement Queue using Linked List

EMPTY_QUEUE = "Queue is empty..."

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def isempty(self):
        return self.head is None

    def create_node(self, data):
        return Node(data)

    def enqueue(self, data):
        if self.isempty():
            print(EMPTY_QUEUE)
            self.head = self.create_node(data)
            self.tail = self.head
            return
        self.tail.next = self.create_node(data)
        self.size += 1

    def dequeue(self):
        if self.isempty():
            print(EMPTY_QUEUE)
            return
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.size -= 1
        return temp.data

    def front(self):
        if self.isempty():
            print(EMPTY_QUEUE)
            return
        return self.head.data


if __name__ == "__main__":
    q = Queue()
    # q.head = Node(5)
    # q.head.next = Node(6)
    # q.head.next.next = Node(7)
    q.enqueue(5)
    q.enqueue(6)
    print("dequeue", q.dequeue())
    print(q.front())
    print("dequeue", q.dequeue())
    print("dequeue", q.dequeue())
    print("dequeue", q.dequeue())
