# A slight variant on the classic Node data type


class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None


# Linked list iterator to make parsing through the hash table uncomplicated
class LinkedListIterator:
    def __init__(self, linked_list):
        self._current = linked_list.head

    def __iter__(self):
        return self

    def __next__(self):
        if self._current is None:
            raise StopIteration
        value = (self._current.key, self._current.data)
        self._current = self._current.next
        return value


# A variant on a basic linked list ADT
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        return LinkedListIterator(self)

    @property
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def search(self, key):
        current_node = self.head

        while current_node is not None and current_node.key is not key:
            current_node = current_node.next

        if current_node is not None:
            return current_node
        else:
            return None

    def insert(self, insert_node):
        if self.head is None:
            self.head = insert_node
            return
        else:
            insert_node.next = self.head
            self.head = insert_node

    def remove(self, node):
        current_node = self.head
        if current_node is node:
            self.head = None

        while current_node is not None and current_node.next is not node:
            current_node = current_node.next

        if current_node is None:
            return
        else:
            if current_node.next.next is not None:
                current_node.next = current_node.next.next
            else:
                current_node.next = None
