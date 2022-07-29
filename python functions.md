# various useful python functions

## list
| **function**                                     | **input**                                                                     | **output**  |
| ------------------------------------------------ | ----------------------------------------------------------------------------- | ----------- |
| *string*.join(*iterable*)                        | any iterable object                                                           | string      |
| sorted(_iterable_, key=_key_, reverse=_reverse_) | iterable required (sequence to sort), key is a function, reverse is a boolean | sorted list |
| *list*.sort(key=_key_, reverse=*reverse*)| | none |


## collections
| **function**                              | **input** | **output**| 
| ----------------------------------------- | --------- | --- |
| collections.Counter([*iterable/mapping*]) | iterable or mapping | dict|

- **Counter** - dict subclass for counting hashable objects
	- collection where elements are stored as dictionary keys and counts are stored as dictionary values
	- example:
	```
	c = Counter() #new, empty counter
	c = Counter('gallahad') #new counter from iterable
	c = Counter({'red':4, 'blue':2}) #new counter from mapping
	c = Counter(cats=4, dogs=8) #new counter from keyword args
	```

- additional methods for Counter objects:
	- elements()
	- most_common($[n]$)
	- subtract($[iterable/mapping]$)
	- total()
	- fromkeys($iterable$)
	- update($[iterable/mapping]$)
