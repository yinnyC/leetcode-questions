""" 99. Recover Binary Search Tree """


class Solution:
    _prev_node = None
    _swapA = _swapB = None

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do a in-order traverse first
        and check if the previous node > current node
        -> track the previous node
        after all nodes are visited, swap the nodes
        """
        self._inorder_traverse(root)
        if self._swapA and self._swapB:
            self._swapA.val, self._swapB.val = self._swapB.val, self._swapA.val

    def _inorder_traverse(self, root):
        if root is None or root.val is None:
            return

        self._inorder_traverse(root.left)

        if self._prev_node and self._prev_node.val:
            if self._prev_node.val > root.val:
                if self._swapA is None:
                    self._swapA = self._prev_node
                self._swapB = root
        self._prev_node = root
        self._inorder_traverse(root.right)
