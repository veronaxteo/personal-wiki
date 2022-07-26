## Hash Tables
- **hash table** - data structure that maps keys to values for highly efficient lookup
	- key-value pairs
	- keys must be unique, but values can be repeated

- a **hash function** H(x) is a function that maps a key 'x' to a whole number in a fixed range
- we can also define hash functions for arbitrary objects like strings, lists, tuples, etc.

### Properties of hash functions
- if H(x) = H(y), then objects x and y *might be equal*, but if H(x) != H(y), then x and y are certainly not equal

### Collisions
- for hash collisions, the two most popular resolution techniques are **separate chaining** and **open addressing**

- **separate changing** - deals with hash collisions by maintaining a data structure (usually a linked list) to hold all the different values which hashed to a particular value
- **open addressing** - deals with hash collisions by finding another place within hash table for object to go by offsetting it from position to which it hashed to

### Complexity
| **operation** | **average** | **worst** |
| ------------- | ----------- | --------- |
| *insertion*   | O(1)* |     O(n)      |
| *removal* |      O(1)*       |     O(n)      |
| *search*|       O(1)*      |      O(n)     |
- * constant time for hash tables only true if you have a good uniform hash function

### Implementations
- one simple implementation: use array of linked lists and a cash code function. to insert a key and value:
	1. compute key's hash code (usually int or long)
		- different keys can have same hash code
	2. map hash code to index in the array
		- different hash codes can map to same index
	3. at this index, there is a linked list of keys and values. store key and value in index
		- use linked list because of collisions (different keys with same hash code or different hash codes that map to same index)

	- complexity: if # of collisions is high, then worst case runtime is O(N), where N = # of keys. usually, lookup time is O(1)

- we can implement hash table with balanced binary search tree
	- complexity: O(logN)
	- advantage: potentially uses less space

