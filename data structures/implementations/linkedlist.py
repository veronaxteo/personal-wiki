# The average time complexity of some operations involving linked lists are as follows:
# Look-up : O(n)
# Insert : O(n)
# Delete : O(n)
# Append : O(1)
# Prepend : O(1)

from ast import Index
from cgi import test
from multiprocessing.sharedctypes import Value
from optparse import IndentedHelpFormatter
from re import I
from typing import Any

# create node class for each node in linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    
# create linked list class
class LinkedList():
    '''
    head: points to beginning of list
    tail: points to end of list
    length: optional value that can keep track of length of linked list
    '''
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    # other methods
    def __iter__(self):
        """
        function for iterators to access and iterate through data inside linked list
        """
        node = self.head
        while node:
            yield node.data
            node = node.next
    
    # get - get node at index
    def __get__(self, index):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")
        
        for i, node in enumerate(self):
            if i == index:
                return node

    # set - set node at index
    def __set__(self, index, data):
        if not 0 <= index < len(self):
            raise ValueError("list index out of range")

        currNode = self.head
        for _ in range(index):
            currNode = currNode.next
        currNode.data = data

    # printList - print values of nodes
    def printList(self):
        if self.head == None:
            print("empty linked list")
        else:
            print(self)

    # generic append method
    # append - adds node to end of linked list
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length = 1
        
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
    
    # generic prepend method
    # prepend - adds node to front of linked list
    def prepend(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.length += 1

    # insert - insert node at index
    def insert(self, index, data):
        """
        index: position to insert node
        """
        # if not 0 <= index <= self.length:
        #     raise IndexError("list index out of range")
            
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.length += 1
        elif index == 0:
            newNode.next = self.head    # link new node to head
            self.head = newNode
            self.length += 1
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.next
            newNode.next = currNode.next
            currNode.next = newNode
            self.length += 1

    # insertTail - insert node at end of linked list
    def insertTail(self, data):
        self.length -= 1
        self.insert(self.length, data)

    # insertHead - insert node at front of linked list
    def insertHead(self, data):
        self.length -= 1
        self.insert(0, data)

    # delete - delete node at given index and return node's data
    def delete(self, index):
        # if not 0 <= index <= self.length - 1:
        #     raise IndexError("list index out of range")

        if self.head is None:
            print("empty linked list")
            return

        deletedNode = self.head     # default delete is first node
        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            currNode = self.head
            for _ in range(index - 1):
                currNode = currNode.next
            deletedNode = currNode.next
            currNode.next = currNode.next.next
            self.length -= 1

        return deletedNode.data

    # deleteHead - delete first node and return node's data
    def deleteHead(self):
        self.length -= 1
        return self.delete(0)
    
    # deleteTail - delete last node and return node's data
    def deleteTail(self):
        self.length -= 1
        return self.delete(self.length - 1)
    
    # reverse - reverses the linked list
    def reverse(self):
        prev = None
        currNode = self.head

        while currNode:
            nextNode = currNode.next
            currNode.next = prev
            prev = currNode
            currNode = nextNode
        
        self.head = prev


def main():
    from doctest import testmod
    testmod()

    linked_list = LinkedList()
    print("insert head/prepend: ", end='\n')
    linked_list.insertHead(3)
    linked_list.insertHead(5)
    linked_list.prepend(4)
    print(linked_list.length, end='\n')
    linked_list.printList()

    print("insert tail/append: ", end='\n')
    linked_list.insertTail(7)
    linked_list.insertTail(1)
    # linked_list.append(9)
    print(linked_list.length, end='\n')
    linked_list.printList()

    print("insert at index: ", end='\n')
    linked_list.insert(index=4, data=6)
    linked_list.insert(0, 1)
    print("\nprint list: ")
    print(linked_list.length, end='\n')
    linked_list.printList()

    print("delete head", end='\n')
    linked_list.deleteHead()
    print(linked_list.length, end='\n')
    linked_list.printList()

    print("delete tail", end='\n')
    linked_list.deleteTail()
    print(linked_list.length, end='\n')
    linked_list.printList()

    print("delete at index", end='\n')
    linked_list.delete(index=2)
    print(linked_list.length, end='\n')
    linked_list.printList()

    print("\nreverse linked list ", end='\n')
    linked_list.reverse()
    linked_list.printList()


if __name__ == "__main__":
    main()