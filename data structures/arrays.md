# Arrays and Strings

## Arrays
- **array** - a data structure used to store homogeneous elements at contiguous locations
	- one memory block is allocated for the entire array to hold the elements of the array
	- the array elements can be accessed in constant time by using the index of the particular element as the subscript

### Properties of arrays
- arrays stores similar data types; array can hold data of same data type values. this is one of the limitations of arrays compared to other data structures
- each value stored, in an array, is known as an element and all elements are indexed. the first element added, by default, gets 0 index
- elements can be retrieved by their index number (**random access**)
- array elements are stored in contiguous (continuous) memory locations
- one array name can represent multiple values
	- array is the easiest way to store a large quantity of data of same data types
	- for example, to store the salary of 100 employees, it is required to declare 100 variables. But with arrays, with one array name all the 100 employees salaries can be stored
- at the time of creation itself, array size should be declared (array initialization does not require size).

Note: python does not have native support for arrays; has more generic data structure called list. but you can "import array"


### Disadvantages of arrays
- *fixed size*: size of array is static
	- can be overcome using dynamic arrays
- *one block allocation*: to allocate array itself at beginning, sometimes it may not be possible to get memory for complete array (e.g. if array size is big)
- *complex position-based insertion*: to insert an element at a given position, we may need to shift the existing elements
	- if position we want to add an element is at beginning, then shifting operation is more expensive