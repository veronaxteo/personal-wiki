# ArrayList, Resizable Arrays
- **arraylist** - an array that resizes itself as needed while still providing O(1) access
	- typical implementation: when array is full, array doubles in size
		- each doubling takes O(n) time, but happens so rarely that amortized insertion time is still O(1)
	- name of data structure and resizing factor (two for java) can vary

*why is the amortized insertion runtime O(1)?*
- inserting N elements takes O(N) work total. each insertion is O(1) on average, though some insertions take O(N) in worst case
