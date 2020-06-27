

"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        # Stores a node, that corresponds to our first node in the list
        self.head = None
        # stores a node that is the end of the list
        self.tail = None

    # return all values in the list a -> b -> c -> d -> None
    def __str__(self):
        output = ''
        current_node = self.head  # create a tracker node variable
        while current_node is not None:  # loop until its NONE

            output += f'{current_node.value} -> '

            # update the tracker node to the next node
            current_node = current_node.next_node

        return output

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head

        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node
        return False


class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def enqueue(self, value):
        # add the new value, to the tail of our list
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        # remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_head()
        return value


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # add an element to the front of our array
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        # check if empty
        if self.size == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.remove_head()
        return node


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                return self.left.insert(value)

        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                return self.right.insert(value)

    # Artem's solution
    #         # take the current value of our node (self.value)
    #         # compare to the new value we want to insert
    # ​
    #         if value < self.value:
    #             # IF self.left is already taken by a node
    #                 # make that (left) node, call insert
    #             # set the left to the new node with the new value
    #             if self.left is None:
    #                 self.left = BSTNode(value)
    #             else:
    #                 self.left.insert(value)
    # ​
    #         if value >= self.value:
    #             # IF self.right is already taken by a node
    #                 # make that (right) node call insert
    #             # set the right child to the new node with new value
    #             if self.right is None:
    #                 self.right = BSTNode(value)
    #             else:
    #                 self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            found = self.left.contains(target)
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
        return found

    # Return the maximum value found in the tree

        # Artem's solution
    #     if self.value == target:
    #             return True
    #         # compare the target to current value
    #         # if current value is more than target
    #         found = False
    #         if self.value >= target:
    #             # check the left subtree (self.left.contains(target))
    #             # if you cannot go left, return False
    #             if self.left is None:
    #                 return False
    #             found = self.left.contains(target)
    # ​
    #         # if current value is less than target
    #         if self.value < target:
    #             # check if right subtree contains target
    #             # if you cannot go right, return False
    #             if self.right is None:
    #                 return False
    #             found = self.right.contains(target)
    #         return found

    def get_max(self):
        # initializes largest value as the root value
        largest_value = self.value
        # checks is right has nothing in it if so self.value is larget num
        # so self.value is return
        if self.right is None:
            return self.value

        # else if the right value is not None...
        elif self.right is not None:
            # check if the current largest value is larger or equal to the right value
            if largest_value >= self.right.value:
                # if it is larger than reassign the current largest value to the right value
                largest_value = self.right.value
                # return the new current largest value
                return largest_value
            # Assign the check next variable to a recurssive function so that the
            # algo will run again and keep going until the furthest right node is None
            # which at that point will return it's value as specified at line 58
            check_next = self.right.get_max()
        # return the check_next variable that will only run so long as the right variable is not None
        return check_next

        # Artem's solution
        # the largest value will always be to the right of the current node
        # if we can go right, lets find the largest number there by calling get_max on the right subtree
        # if we cannot go right, return the current value
        # if self.right is None:
        #     return self.value
        # max_val = self.right.get_max()
        # return max_val

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.right is not None:
            self.right.for_each(fn)
        if self.left is not None:
            self.left.for_each(fn)

        # Artem's solution
        # call function on the current value fn(self.value)
        # if you can go left, call for_each on the left tree
        #         if self.left:
        #             self.left.for_each(fn)
        # ​
        #         fn(self.value)
        #         # if you can go right, call for_each on the right tree
        #         if self.right:
        #             self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self, node):
        self.value = node.value

        if self.left is not None:
            self.left.in_order_print(self.left)

        print(self.value)

        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    def bft_print(self, node):

        # create a queue for nodes
        # add the first node to the queue
        # while queue is not empty
        # remove the first node from the queue
        # print the removed node
        # add all children into the queue
        # Print the value of every node, starting with the given node,
        # in an iterative depth first traversal

        queue = []
        queue.append(node)
        # current_node = node
        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def dft_print(self, node):

        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
        # get the current node from the top of the stack
        # print that node
        # add all children to the stack

        stack = []
        stack.append(node)
        # current_node = node
        while len(stack) > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.append(current_node.left)
            if current_node.right:
                stack.append(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required
    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        # self.in_order_print(node)
        pass

    # Print Post-order recursive DFT

    def post_order_dft(self, node):
        pass


test = BSTNode(1)
test.insert(8)
test.insert(5)
test.insert(7)
test.insert(6)
test.insert(3)
test.insert(4)
test.insert(2)

test.bft_print(test)
