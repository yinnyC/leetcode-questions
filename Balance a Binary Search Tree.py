""" 1382. Balance a Binary Search Tree """


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        do in-order first then store nodes in a list
        find the middle node then rebuild the tree
        """
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            order.append(node)
            inorder(node.right)

        def buildTree(curr_order):
            if not curr_order:
                return None

            mid = len(curr_order)//2
            root = curr_order[mid]
            root.left = buildTree(curr_order[:mid])
            root.right = buildTree(curr_order[mid+1:])
            return root
        order = []
        inorder(root)
        return buildTree(order)
