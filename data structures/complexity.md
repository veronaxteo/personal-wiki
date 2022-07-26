# Big-O
## Notes from *Cracking the Coding Interview*

## Bounds
- **big O** - upper bound 
- **big omega** - lower bound
- **big theta** - both O and omega; gives tight bound

- in industry, big O is more like big theta, the tightest bound

## Best, Worst, and Expected Case
- example: quick sort (picks random element as pivot and swaps values in array such that elements < pivot appear before elements > pivot)
	- best: O(N); e.g. if all elements are equal
	- worst: O($N^2$); e.g. sorted in reverse order and pivot is biggest element of array
	- expected: O($NlogN$)

*what is the relationship between best/worst/expected case and big O/theta/omega?*
- No particular relationship
- Cases describe the big O/theta time for particular inputs or scenarios
- Big O/omega/theta describe upper, lower, and tight bounds for runtime


## Space Complexity
- space complexity is a parallel concept to time  complexity
- ex: array of size n is O(n) space, 2d array nxn is O(n^2) space


- it is possible for O(N) code to run faster than O(1) code for specific inputs
	- big O just describes rate of increase
- So, we drop the constants in runtime and non-dominant terms
	- ex: O($N^2 + N^2$) = O($2N^2$) = O($N^2$)
	- ex: O($N^2 + N$) = O($N^2$)
	- ex: O($N + logN$) = O($N$)


![[big-o_complexity.png]]


- add runtimes:
```
for (int a : arrA) {
	print(a);
}
for (int b : arrB) {
	print(b);
}
```

- multiply runtimes:
```
for (int a : arrA) {
	for (int b : arrB) {
		print(a + "," + b)
	}
}
```


## Amortized Time
- best way to express time complexity when an algorithm has the very bad time complexity only once in awhile besides the time complexity that happens most of the time
- the average time taken per operation, if you do many operations

- example: arraylist
	- for arraylist, when array hits capacity, arraylist class creates new array with double capacity and copies all elements over to new array
	- so if full, then insertion takes O(N) time (creates new array of size 2N + copying N elements over)
	- but vast majority of time insertion is O(1) time
	- thus, X insertions takes O(2X) time. amortized time for each insertion is O(1)

### Log N Runtimes
- *when you see problem where # of elements in problem space gets halved 1/2 each time, will likely be O(logN) runtime.*


### Recursive Runtimes
- ex: time = $2^N$, space = O(N)
![[recursive_ex1.png]]

- *generally, if you have recursive function that makes multiple calls, the runtime will often look like O($branches ^{depth}$), where branches = # of times each recursive call branches


## Examples
1. 
```
void printPairs(int[] array) {
	for (int i = 0; i < array.length; i++) {
		for (int j = i+1; j < array.length; j++){
			system.out.println(array[i] + "," + array[j]);
		}
	}
}
```
$N^2$

2. ![[Screen Shot 2022-07-22 at 17.21.59.png]]
O($arrA.length * arrB.length$)

3. reversing an array
![[Screen Shot 2022-07-22 at 17.32.34.png]]
O(N)

4. take in array of strings, sort each string, and then sort full array
	- let s = length of longest string, a = length of array
	- sorting each string is O($s*log s$). we do this for every string so that's O($a*s*logs$)
	- now we sort all the strings: # of comparisons * each string comparison
		- string comparison = O(s)
		- number of comparisons = O($aloga$)
		- so sorting strings takes O($s*aloga$)
	- adding all together: O($a * s(loga + logs$))

5. sum values of all nodes in balanced binary search tree
![[Screen Shot 2022-07-22 at 17.56.10.png]]
O(N) = O($2^{logN}$)
- meaning
	- teach each node in tree once and does constant work each touch
- recursive approach
	- 2 branches at each call, so O($2^{depth}$)
	- N total nodes, so depth is ~logN
	- thus, O($2^{logN}$) = O(N) where N = # of nodes

6. check if number is prime
![[Screen Shot 2022-07-22 at 17.59.49.png]]
O($\sqrt{N}$)
- constant work in for loop
- for loop starts at x=2 and ends when $x*x = n$ so when $x = \sqrt{n}$

7. compute n!
![[Screen Shot 2022-07-22 at 18.02.15.png]]
O(n) because recursion from n -> n-1 -> n-2 -> ... -> 1


8. compute nth fibonacci number
![[Screen Shot 2022-07-22 at 18.08.36.png]]
O($2^N$)
- 2 branches per call, go as deep as N


9. print all fibonacci numbers from 0 to n
![[Screen Shot 2022-07-22 at 18.12.08.png]]
O($2^N$)
- be careful not to do O($2^N$) * n because *n is changing*


10. print all fibonacci numbers from 0 to n. store (cache) previously computed values in integer array. if already computed, return the cache
![[Screen Shot 2022-07-22 at 18.14.44.png]]
O(n)
- at each call to fib(i), we've computed and stored values for fib(i-1) and fib(i-2)
	- take these two values, sum, and store new result = O(1)
- O(1) * N times, so O(n)


11. print powers of 2 from 1 through n inclusive
![[Screen Shot 2022-07-22 at 18.16.51.png]]
O(logn)