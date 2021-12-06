class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        temp_var = self.head
        self.head = Node(data)
        self.head.next = temp_var

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data)

    def print(self):
        if self.head is None:
            print("Linked list is Empty")
            return

        itr = self.head
        llstr = " "

        while itr:
            llstr += str(itr.data) + "---->"
            itr = itr.next
        print(llstr)

    def insert_arr(self, arr):
        self.head = None
        for data in arr:
            self.insert_at_end(data)

    def get_length(self):
        if self.head is None:
            return 0
        count = 0
        val = self.head
        while val:
            val = val.next
            count += 1
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        val = self.head

        while val:
            if count == index-1:
                val.next = val.next.next
                break
            val = val.next
            count += 1

    def insert_at(self, index, var):
        if index < 0 or index > self.get_length()+1:
            raise Exception("Invalid index")
        elif index == 0:
            self.insert_at_beginning(var)
            return
        elif index == self.get_length() + 1:
            self.insert_at_end(var)
            return
        else:
            val = self.head
            count = 0
            while val:
                if count == index-1:
                    new_var = val.next
                    val.next = Node(var)
                    val.next.next = new_var
                    return
                val = val.next
                count += 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.print()
    ll.insert_at_beginning(5)
    ll.print()
    ll.insert_at_beginning(6)
    ll.print()
    ll.insert_at_end(7)
    ll.print()
    ll.insert_at_end(8)
    ll.print()
    ll.insert_at_end(9)

    ll.print()
    print(ll.get_length())
    # ll.remove_at(1)
    ll.insert_at(6, 111)
    ll.print()
    ll.insert_arr(["ASd", "ert", 6, "45", "wer"])
    ll.print()
    ll.remove_at(0)
    ll.print()