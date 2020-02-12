"""
Binary Tree Traversal
Venky, 08/10/2017

"""


# Define the node
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


"""
Methods for printing the traversal
Inorder: Left, Root, Right
Preorder: Root, Left, Right
Postorder: Left, Right, Root
"""


def in_order(root):
    if root:
        in_order(root.left)
        if root.data is not None:
            print(root.data)
        in_order(root.right)


def pre_order(root):
    if root:
        print(root.data)
        pre_order(root.left)
        pre_order(root.right)


def post_order(root):
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.data)


if __name__ == "__main__":

    # Create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("InOrder:")
    in_order(root)
    # 4 2 5 1 3
    print("PreOrder:")
    pre_order(root)
    # 1 2 4 5 3
    print("PostOrder:")
    post_order(root)
    # 4 5 2 3 1
