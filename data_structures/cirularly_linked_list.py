class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class CircularlyLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        new_node.next = self.head
        if self.head is None:
            new_node.next = new_node
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            self.head = cur.next

    def append(self, data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            val = self.head
            while val.next != self.head:
                val = val.next
            val.next = Node(data)
            val.next.next = self.head

    def print_list(self):
        val = self.head
        new_str = ""
        while True:
            new_str += str(val.data) + "--->"
            val = val.next
            if val == self.head:
                print(new_str)
                break
        pass


new_list = CircularlyLinkedList()
new_list.append(7)
new_list.print_list()
new_list.append(5)

new_list.append(9)
new_list.print_list()
new_list.prepend(8)
new_list.print_list()
