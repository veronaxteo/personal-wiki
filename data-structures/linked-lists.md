# linked lists
- **linked list** - a data structure that represents a sequence of nodes
	- **singly linked list** - each nodes points to next node in linked list
	- **doubly linked list** - gives each node points to both next node and previous node

- unlike an array, a linked list does not provide constant time access to a particular "index" within list
	- i.e. if you want to find kth element in list, need to iterate through k elements

- can add and remove items from the beginning of list in constant time


### deleting a node from singly linked list
- given a node n, we find the previous node prev and set prev.next = n.next
- if doubly linked, we must also update n.next to set n.next.prev = n.prev

- remember to check for null pointer and to update head or tail pointer as necessary


### runner technique
- "runner" (second pointer) technique - iterate through linked list with two pointers simultaneously, with one ahead of other
	- "fast" node might be ahead by fixed amount or hopping multiple nodes for each one node that the "slow" node iterates through