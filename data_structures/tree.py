class TreeNode:

    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spacer = " " * self.get_level() * 2
        prefix = spacer + "-->" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_product_tree():

    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MAC"))
    laptop.add_child(TreeNode("LENOVO"))
    laptop.add_child(TreeNode("ASUS"))

    mobile_phone = TreeNode("Mobile Phone")
    mobile_phone.add_child(TreeNode("I-PHONE"))
    mobile_phone.add_child(TreeNode("ANDROID"))
    mobile_phone.add_child(TreeNode("ONE-PLUS"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("SAMSUNG"))

    root.add_child(laptop)
    root.add_child(mobile_phone)
    root.add_child(tv)

    return root


product_tree = build_product_tree()
product_tree.print_tree()
pass
