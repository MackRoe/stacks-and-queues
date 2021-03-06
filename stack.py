#!python
from linkedlist import LinkedList


# Implement LinkedStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class LinkedStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # Check if empty
        if self.list.length() != 0:
            return False
        else:
            return True

    def length(self):
        """Return the number of items in this stack."""
        # Count number of items
        stack_length = self.list.length()
        return stack_length

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1) – Why? [the logic follows a straight line
        without needing to loop]"""
        # Push given item
        self.list.prepend(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        if self.list.length() != 0:
            # index = self.length() - 1
            top_item = self.list.get_at_index(0)
            return top_item
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(n) – Why? [pop() calls peek() that calls length() from
        LinkedList, which iterates using a while loop]"""
        # TODO: Remove and return top item, if any
        # find top_item
        top_item = self.peek()
        # delete top_item
        self.list.delete(top_item)
        # return new_top_item
        new_top_item = self.peek()
        print("new top: ", new_top_item)
        return new_top_item


# Implement ArrayStack below, then change the assignment at the bottom
# to use this Stack implementation to verify it passes all tests
class ArrayStack(object):

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any."""
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        # TODO: Check if empty
        if len(self.list) != 0:
            return False
        else:
            return True

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items
        stack_length = len(self.list)
        return stack_length

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(1)* – Why? [Unless the array needs to be resized,
        the item can be appended without manipulating the array]"""
        # TODO: Insert given item
        self.list.append(item)

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any
        array_length = len(self.list)

        if len(self.list) != 0:
            stack_top = self.list[array_length - 1]
            return stack_top
        else:
            return None

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(1) – Why? [because the top of the stack is the end of
        the array and no iteration is needed to find it]"""
        # TODO: Remove and return top item, if any
        index = len(self.list) - 1
        top = self.peek()
        if top is None:
            raise ValueError('List is Empty')
        else:
            print('top', top)
            self.list.pop(index)
            return top


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
