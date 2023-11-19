CONSTANTS = {
    'EMPTY_LINKEDLIST': 'Linked list is empty...',
    'Q_INSERT_AT_BEGINNING': "Do you want to insert node at beginning?",
    'Q_INSERT_AT_ENDING': "Do you want to insert node at ending?",
    'AFFIRMATIVE_USER_INPUT_RANGE': ['y', 'yes'],
    'USER_INPUT_NO': 'You selected no. Exiting...'
}


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def create_node(self, data):
        return Node(data)

    def isempty(self):
        return True if self.head is None else False

    def print_linked_list(self):
        if self.isempty():
            print(CONSTANTS.get('EMPTY_LINKEDLIST'))
            return
        iterator = self.head
        while(iterator is not None):
            print(iterator.data, end=" -> " if iterator.next else "\n")
            iterator = iterator.next

    # ------------------------ Insert a Node in Linked List ------------------------
    def insert_node_at_start(self, data):
        new_node = self.create_node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_node_at_end(self, data):
        if self.isempty():
            return self.insert_node_at_start(data)
        new_node = self.create_node(data)
        iterator = self.head
        while(iterator.next is not None):
            iterator = iterator.next
        iterator.next = new_node
        self.size += 1

    def insert_node_at_position(self, data, position):
        if self.isempty():
            user_input = input(CONSTANTS.get('Q_INSERT_AT_BEGINNING'))
            if(user_input.lower() in CONSTANTS.get("AFFIRMATIVE_USER_INPUT_RANGE")):
                return self.insert_node_at_start(data)
            print(CONSTANTS.get("USER_INPUT_NO"))
            return
        elif self.size < position:
            user_input = input(CONSTANTS.get("Q_INSERT_AT_ENDING"))
            if(user_input.lower() in CONSTANTS.get("AFFIRMATIVE_USER_INPUT_RANGE")):
                return self.insert_node_at_end(data)
            print(CONSTANTS.get("USER_INPUT_NO"))
            return
        iterator = self.head
        current_position = 0
        while(iterator and current_position < position):
            iterator = iterator.next
        new_node = self.create_node(data)
        iterator.next = new_node
        new_node.next = iterator.next.next

    # ------------------------ Delete a Node in Linked List ------------------------


if __name__ == "__main__":
    l = SinglyLinkedList()
    l.print_linked_list()
    l.insert_node_at_start(8)
    l.insert_node_at_start(5)
    l.insert_node_at_start(0)
    l.insert_node_at_end(9)
    l.print_linked_list()
    print(l.size)
