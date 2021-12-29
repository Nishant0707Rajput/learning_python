class BinarySearchTreeNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)

        return elements

    def search(self, val):
        if self.data == val:
            return True

        elif val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        else:

            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_min(self):
        if not self.left:
            return self.data
        else:
            return self.left.find_min()

    def find_max(self):
        if not self.right:
            return self.data
        else:
            return self.right.find_max()


def build_tree(arr):
    root = BinarySearchTreeNode(arr[0])

    for i in range(1, len(arr)):
        root.add_child(arr[i])
    return root


new_arr = [9, 6, 7, 5, 27, 19, 42]
first_tree = build_tree(new_arr)
print(first_tree.pre_order_traversal())
print(first_tree.in_order_traversal())
print(first_tree.post_order_traversal())
# print(first_tree.find_min())
# print(first_tree.find_max())
# print(first_tree.search(10))
# print(first_tree.search(7))

# another_arr = ["India", "America", "UK", "Australia", "New Zealand"]

# another_tree = build_tree(another_arr)
# print(another_tree.search("New Zealand"))
# print(another_tree.in_order_traversal())

