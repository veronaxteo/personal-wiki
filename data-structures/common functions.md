# Common Data Structure Manipulations

### reverse an array
**python**


**java**
```
void reverse(int[] array) {
	for (int i = 0; i < array.length)/2; i++) {
		int other = array.length - i - 1;
		int temp = array[i];
		aray[i] = array[other];
		array[other] = temp;
	}
}
```


### compute Nth fibonacci number
**python**

**java**
```
int fib(int n) {
	if (n <= 0) return 0;
	else if (n == 1) return 1;
	return fib(n - 1) + fib(n - 2);
}
```
