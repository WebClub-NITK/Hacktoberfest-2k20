class Node:
    """The unit that consists AVL tree.

    Attributes:
        value (int): Value of the node.
        left (Node): Left child. None if no child on left.
        right (Node): Right child. None if no child on right.
        bf (int): Balance factor which is determined by (height of `left`) - (height of `right`).
        height (int): Height of the node. 1 if it's a leaf node.
    """
    def __init__(self, value: int):
        """Constructor of Node class.
        It will have None on its `left` and `right`,
        and 0 and 1 for `bf` and `height` by default.

        Args:
            value (int): Value of the node.
        """
        self.value = value
        self.left = None
        self.right = None
        self.bf = 0
        self.height = 1

    def update(self, recurse: bool):
        """Updates node's height and balance factor (bf)

        Args:
            recurse (bool): Flag to update recursively.
        """
        if self.left is None and self.right is None:
            self.bf = 0
            self.height = 1
        elif self.left is None:
            if recurse:
                self.right.update(True)
            self.bf = -self.right.height
            self.height = self.right.height + 1
        elif self.right is None:
            if recurse:
                self.left.update(True)
            self.bf = self.left.height
            self.height = self.left.height + 1
        else:
            if recurse:
                self.left.update(True)
                self.right.update(True)
            self.bf = self.left.height - self.right.height
            self.height = max(self.left.height, self.right.height) + 1

    def __repr__(self):
        return "%d" % self.value

class AVLTree:
    """A tree structure that always has balanced binary search tree.

    Attributes:
        root (Node): The root node of the tree. It can be null when it's empty.
    """
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> bool:
        """Inserts a value to the tree.

        Args:
            value (int): A int-typed value to insert.

        Returns:
            True if successful, False otherwise.

        Raises:
            ValueError: If the given `value` is already in the tree.
        """
        self.root = self.__insert(self.root, value)
        return self.root is not None

    def __insert(self, node, value: int) -> Node:
        if node is None:
            node = Node(value)
        elif value < node.value:
            node.left = self.__insert(node.left, value)
        elif value > node.value:
            node.right = self.__insert(node.right, value)
        else:
            raise ValueError("Tree already has the value %d." % value)
        
        node = self.__rebalance(node)
        return node

    def find(self, value: int) -> bool:
        """Determine whether given value is in the tree.

        Args:
            value (int): A int-typed value to find.

        Returns:
            True if `value` is in the tree, False otherwise.
        """
        return self.__find(self.root, value) is not None
    
    def __find(self, node: Node, value: int) -> Node:
        if node is None:
            return None
        elif value == node.value:
            return node
        elif value < node.value:
            return self.__find(node.left, value)
        else:
            return self.__find(node.right, value)

    def delete(self, value: int) -> bool:
        """Delete given value from the tree.

        Args:
            value (int): A int-typed value to delete.

        Returns:
            True if `value` was in the tree, False otherwise.
        """
        self.root, deleted = self.__delete(self.root, value)
        return deleted is not None

    def __delete(self, node: Node, value: int) -> Node:
        if node is None:
            return None, None
        elif value < node.value:
            node.left, deleted = self.__delete(node.left, value)
        elif value > node.value:
            node.right, deleted = self.__delete(node.right, value)
        else:
            deleted = Node(node.value)
            if node.left is None and node.right is None:
                node = None
            elif node.left is None:
                node = node.right
            elif node.right is None:
                node = node.left
            else:
                node, smallest = self.__delete(node, self.__smallest_node(node.right))
                smallest.left = node.left
                smallest.right = node.right
                node = smallest

        if node is not None:
            node = self.__rebalance(node)
        return node, deleted

    def __smallest_node(self, node: Node) -> int:
        if node.left is None:
            return node.value
        else:
            return self.__smallest_node(node.left)

    def __rebalance(self, node: Node) -> Node:
        return node
        node.update(False)
        while node.bf < -1 or node.bf > 1:
            if node.bf > 1:
                if node.left.bf < 0:
                    node.left = self.__lrotate(node.left)
                    node.update(True)
                node = self.__rrotate(node)
                node.update(True)
            elif node.bf < -1:
                if node.right.bf > 0:
                    node.right = self.__rrotate(node.right)
                    node.update(True)
                node = self.__lrotate(node)
                node.update(True)

        return node

    def __rrotate(self, node: Node) -> Node:
        A = node
        B = node.left
        T = B.right
        
        node = B
        B.right = A 
        A.left = T 
        return node
    
    def __lrotate(self, node: Node) -> Node:
        A = node
        B = node.right
        T = B.left
        
        node = B
        B.left = A
        A.right = T
        return node
    
    def __repr__(self):
        ret = ""
        queue = [self.root]
        queue_next = []
        while True:
            num = len(queue)
            while queue:
                node = queue.pop(0)
                if node is None:
                    ret += "-"
                else:
                    queue_next.append(node.left)
                    queue_next.append(node.right)
                    ret += repr(node)
                ret += " "
            
            if not queue_next:
                break
            
            queue = queue_next
            queue_next = []
            ret += "\n"

        return ret
