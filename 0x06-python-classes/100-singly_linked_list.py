#!/usr/bin/python3

"""
    A program that create a singly linked list
"""


class Node:
    """
      Initialise a node
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and isinstance(value, Node) is not True:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
        Sort a singly linked list in increasing order
    """
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        if self.head is None:
            new_node = Node(value)
            self.head = new_node

        else:
            prevNode = None
            currNode = self.head
            while currNode is not None and currNode.data < value:
                prevNode = currNode
                currNode = currNode.next_node

            if (prevNode is None):
                currNode = self.head
                new_node = Node(value)
                new_node.next_node = self.head
                self.head = new_node

            else:
                new_node = Node(value)
                prevNode.next_node = new_node
                new_node.next_node = currNode

    def __repr__(self):
        temp = self.head
        sorted_node = []
        while temp is not None:
            sorted_node.append(str(temp.data))
            temp = temp.next_node
        return '\n'.join(sorted_node)
