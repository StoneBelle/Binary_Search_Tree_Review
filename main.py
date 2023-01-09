
# Binary Tree
# data structure where all nodes have min 1, max 2 child nodes

# Binary Search Tree (BST)
# BT but with a special condition
# node being added will always be a new child
# need to find where within the BST that new child can be inserted (i.e. on L or R)
# L child < parent > R child

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # does not add duplicate data
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

        def search(self, val):
            if self.data == val:
                return True

            if val < self.data:
                if self.left:
                    return self.left.search(val)
                else:
                    return False

            if val > self.data:
                if self.right:
                    return self.right.search(val)
                else:
                    return False

        def in_order_traversal(self):
            elements = []
            if self.left:
                elements += self.left.in_order_traversal()

            elements.append(self.data)

            if self.right:
                elements += self.right.in_order_traversal()

            return elements

        def build_tree(elements):
            print("Building tree with these elements:", elements)
            root = BinarySearchTreeNode(elements[0])

            for i in range(1, len(elements)):
                root.add_child(elements[i])

            return root

        if __name__ == '__main__':
            countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
            country_tree = build_tree(countries)

            print("UK is in the list? ", country_tree.search("UK"))
            print("Sweden is in the list? ", country_tree.search("Sweden"))

            numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
            print("In order traversal gives this sorted list:", numbers_tree.in_order_traversal())
