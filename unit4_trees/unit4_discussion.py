"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None


    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Insertion doesn't rely on a fixed position like inserting at index x in
        # an array list. Instead, the insert method walks through the tree and
        # decides where to place the value by comparing it to existing nodes:
        # if the value is larger than the current node, it moves to the right;
        # if it's smaller, it moves to the left. As long as the tree stays
        # reasonably balanced, this allows values to be found much faster than
        # scanning through every item one by one.

        if self.root is None:
            self.root = Node(value)
            return
        self._insert_recursive(self.root, value)


    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)


    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # search doesnt have to check every single value like a linear search would.
        # since the tree is sorted (smaller values left, larger values right), each
        # comparison lets us skip over an entire half of the remaining tree. so
        # instead of checking every node one by one, we only ever go down one branch
        # at a time, which makes it a lot faster once the tree gets bigger.

        return self._search_recursive(self.root, value)



    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)



    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        list = []
        self._inorder_recursive(self.root, list)
        return list


    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # going left first means we always reach the smallest value before
        # appending anything. once we hit a node with no more left children,
        # we append it, then move to the right side. since every node in a
        # bst follows left < node < right, doing this at every level means
        # the values naturally come out in sorted order.

        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)



def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")
    # Requirements:
    # 1. Create a BST object.
    theTree = BST()

    # 2. Insert at least 7 values.
    for value in[56,33,79,21,46,88,12]:
        theTree.insert(value)
        print(f"Value inserted: {value}")
        
        
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.
    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    print(f"In order: {theTree.inorder()}")


    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")
    #88 is part of the values that do exist so this will return true
    print("Search for value 88")
    print(f"Does value exist: {theTree.search(88)}")
    #46 is part of the values that do exist so this will return true
    print("Search for value 46")
    print(f"Does value exist: {theTree.search(46)}")
    #77 does not exist in the tree this will return false
    print("Search for value 77")
    print(f"Does value exist: {theTree.search(77)}")
    #25 does not exist in the tree this will return false
    print("Search for value 25")
    print(f"Does value exist: {theTree.search(25)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")
    # Example ideas:
    # - Traverse an empty tree

    # since edgeCaseTree.root is still None, _inorder_recursive gets called with
    # None right away and just returns without doing anything, so the values
    # list stays empty and we get [] back instead of an error
    edgeCaseTree = BST()
    print(f"Edge case: {edgeCaseTree.inorder()}")
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.




if __name__ == "__main__":
    main()