# Q. Implement binary tree


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_node(self, data):
        """Return a newly created node."""
        return Node(data)

    def is_empty(self):
        """Check if tree is empty or not."""
        return self.root is None

    def get_root(self):
        """Return the root of the tree."""
        return self.root

    # ======================= tree operations start =======================
    def insert(self, data):
        """
        Insert a node where first leaf node found is None/Null while traversing `level-order(BFS)`
        """
        new_node = self.create_node(data)
        if self.is_empty():
            self.root = new_node
            return
        # Do level order traversal until we find an empty place.
        temp = self.get_root()
        queue = []
        queue.append(temp)
        while len(queue) > 0:
            node = queue.pop(0)
            # insert if it doesn't have any left or right child
            if(node.left is None):
                node.left = new_node
                return
            else:
                # if node have left then traverse to left
                queue.append(node.left)

            if(node.right is None):
                node.right = new_node
                return
            else:
                queue.append(node.right)

    def delete(self, key):
        """Deletes a node with given key.
        ```Time complexity: O(n) where n is no number of nodes. 
        Auxiliary Space: O(n) size of queue. ```
        """
        if self.is_empty():
            print("Can't delete. Binary Tree is empty!")
            return None
        root = self.get_root()
        if(root.left is None and root.right is None):
            if(root.data == key):
                return None
            return root
        return self._delete(root, key)

    def _delete(self, node, key):
        key_node = None
        temp = None
        last = None
        q = []
        q.append(node)

        while len(q):
            temp = q.pop(0)
            if(temp.data == key):
                key_node = temp
            if(temp.left):
                last = temp  # storing the parent node
                q.append(temp.left)
            if(temp.right):
                last = temp  # storing the parent node
                q.append(temp.right)

        if(key_node is not None):
            key_node.data = temp.data  # replacing key_node's data to deepest node's data
            if(last.right == temp):
                last.right = None
            else:
                last.left = None
        return node

    def check_node_exists(self, key):
        """Check if a node with the given key exists in the tree.
        ```Time Complexity: O(N), as we are using recursion to traverse N nodes of the tree. Auxiliary Space: O(N), we are not using any explicit extra space but as we are using recursion there will be extra space allocated for recursive stack.```
        """
        if self.is_empty():
            print("Binary Tree is empty!")
            return False
        return self._check_node_exists(self.get_root(), key)

    def _check_node_exists(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        # check in left sub-tree
        left_tree_res = self._check_node_exists(node.left, key)
        if left_tree_res:
            return True

        # check in right sub-tree
        right_tree_res = self._check_node_exists(node.right, key)
        return right_tree_res

    # ======================= tree operations end =======================

    # =============================== Print Binary Tree Start =============================

    def display(self):
        if self.is_empty():
            print("Binary Tree is empty!")
            return
        lines, *_ = self._display_aux(self.get_root())
        for line in lines:
            print(line)

    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if node.right is None and node.left is None:
            line = '%s' % node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = '%s' % node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = '%s' % node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = '%s' % node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    # =============================== Print Binary Tree End =============================
    # ======================= tree traversal Depth First Search (DFS) start =======================

    def print_preorder(self):
        """Prints Pre-order of the given tree."""
        return self.pre_order(self.get_root())

    def pre_order(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def print_inorder(self):
        """Prints In-order of the given tree."""
        return self.inorder(self.get_root())

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def print_postorder(self):
        """Prints Post-order of the given tree."""
        return self.post_order(self.get_root())

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end=" ")

    # ======================= tree traversal Depth First Search (DFS) end =======================

    # ======================= tree traversal Breadth First Search (BFS) start =======================
    def print_level_order(self):
        """ Print the BFS/Level Order of the tree."""
        return self.level_order(self.get_root())

    def level_order(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)
        while len(queue) > 0:
            print(queue[0].data, end=" ")
            node = queue.pop(0)
            if(node.left):
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    # ======================= tree traversal Breadth First Search (BFS) end =======================

    def find_height_of_tree(self):
        """Returns height of the tree."""
        return self._find_height(self.get_root())

    def _find_height(self, node):
        if node is None:
            return 0
        left_height = self._find_height(node.left)
        right_height = self._find_height(node.right)
        return 1 + max(left_height, right_height)

    def check_balance_tree(self):
        """Check whether given tree is balanced or not."""
        return self._check_balance_tree(self.get_root())

    def _check_balance_tree(self, node):
        if node is None:
            return 0
        left_height = self._find_height(node.left)
        right_height = self._find_height(node.right)
        return abs(left_height - right_height) <= 1


if __name__ == "__main__":
    bt = BinaryTree()
    bt.display()
    bt.root = bt.create_node(5)
    bt.root.left = bt.create_node(4)
    bt.root.right = bt.create_node(7)
    bt.root.right.left = bt.create_node(9)
    # bt.display()
    bt.insert(10)
    # bt.display()
    bt.insert(15)
    # bt.display()
    bt.insert(25)
    bt.insert(51)
    bt.delete(5)
    bt.display()
