"""
Iterator Coding Exercise
Given the following definition of a Node , please implement preorder traversal right inside Node. The sequence returned should be the sequence of values, not their containing nodes.
"""


class Node:
    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

        self.parent = None

        if left:
            self.left.parent = self
        if right:
            self.right.parent = self

    def traverse_preorder(self):
        def traverse(current):
            if not current:
                return
            yield current
            if current.left:
                for left in traverse(current.left):
                    yield left
            if current.right:
                for right in traverse(current.right):
                    yield right

        for node in traverse(self):
            yield node.value


if __name__ == "__main__":
    root = Node(1, Node(2), Node(3))
    for i in root.traverse_preorder():
        print(i)
