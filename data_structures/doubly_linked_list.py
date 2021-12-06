class Node:

    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_var = self.head
            while new_var.next:
                new_var = new_var.next
            new_node = Node(data)
            new_var.next = new_node
            new_node.prev = new_var
            new_node.next = None
        pass

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.prev = None
        else:
            new_var = self.head
            new_node = Node(data)
            self.head = new_node
            new_var.prev = new_node
            new_node.next = new_var
            new_node.prev = None
        # else:

        pass

    def print_list(self):
        new_var = self.head
        dll = " "
        while new_var:
            dll += str(new_var.data) + " <---> "
            new_var = new_var.next
        print(dll)
        pass


new_object = DoublyLinkedList()
new_object.prepend(91)
new_object.print_list()
new_object.append(4)
new_object.print_list()
new_object.append(8)
new_object.print_list()
new_object.append(7)

new_object.print_list()
new_object.prepend(107)
new_object.print_list()