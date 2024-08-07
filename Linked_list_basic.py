class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current = self.head

        if self.head:
            pos = 1

            while current and pos <= position:
                if pos == position:
                    return current
                else:
                    current = current.next

                pos = pos + 1

        else:
            return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if self.head:
            pos = 1
            while current and pos <= position:
                if pos == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                else:
                    current = current.next

                pos = pos + 1

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        previous = None
        if self.head.value == value:
            current = self.head.next
            self.head = current
        else:
            while current.value != value:
                current = current.next
                previous = current
            previous.next = current


# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# # Should print 4 now
print(ll.get_position(2).value)
# # Should print 3 now
print(ll.get_position(3).value)
