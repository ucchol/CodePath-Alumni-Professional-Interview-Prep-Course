# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def insert_node(self, val, node):
        if self.inorder_indices[val] < self.inorder_indices[node.val]:
            if not node.left:
                node.left = TreeNode(val)
            else:
                self.insert_node(val, node.left)
        else:
            if not node.right:
                node.right = TreeNode(val)
            else:
                self.insert_node(val, node.right)

    def buildTree(self, A, B):
        self.inorder_indices = {x: i for i, x in enumerate(A)}
        root = TreeNode(B[-1])
        for num in B[:-1][::-1]:
            self.insert_node(num, root)

        return root
