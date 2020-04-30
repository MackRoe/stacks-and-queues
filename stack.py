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
        Running time: O(???) – Why? [TODO]"""
        # Push given item
        list.list.prepend(item)

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
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any
        # find top_item
        top_item = self.peek()
        # delete top_item
        self.list.delete(top_item)
        # return new_top_item
        new_top_item = self.peek()
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

    def length(self):
        """Return the number of items in this stack."""
        # TODO: Count number of items

    def push(self, item):
        """Insert the given item on the top of this stack.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Insert given item

    def peek(self):
        """Return the item on the top of this stack without removing it,
        or None if this stack is empty."""
        # TODO: Return top item, if any

    def pop(self):
        """Remove and return the item on the top of this stack,
        or raise ValueError if this stack is empty.
        Running time: O(???) – Why? [TODO]"""
        # TODO: Remove and return top item, if any


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
Stack = LinkedStack
# Stack = ArrayStack
