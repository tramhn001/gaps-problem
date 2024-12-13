# gaps-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

Your goal is to write a function that finds gaps between given intervals.

The intervals will be an UNSORTED tuple containing tuples. Each inner tuple will represent an integer interval. It will have two elements: the first element is the beginning of the interval, the second element is the end of the interval. The first element is guaranteed to be strictly less than the second element.

Here is an example of an input tuple:

```py
intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)
```

For clarity of the example, this tuple is sorted. However, note that some of the other test cases are NOT SORTED.

In this example, we can see that the earliest interval ends at 10, and the next interval starts at 12. Thus, there is a gap from 10 to 12. Similarly, we can see there are two other gaps. Below is a tuple (in sorted order) showing all of the gaps for this example:

```py
expected_output = (
    (10, 12), 
    (15, 16), 
    (25, 27)
)
```

Note that there is NOT a gap at 20. One interval ends at 20, and another starts at 20. Though one interval may start at the same time another ends, you are guaranteed there will be no overlap between the input intervals.

Write a function that accepts the UNSORTED input intervals and returns a SORTED tuple of tuples containing all the gaps.

## Examples

### Example 1
```py
intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)

find_gaps(intervals_1)
```
Produces
```py
((10, 12), (15, 16), (25, 27))
```

### Example 2
```py
intervals_2 = (
    (27, 30),
    (16, 20),
    (12, 15),
    (20, 25),
    (5, 10),
)

find_gaps(intervals_2)
```
Produces
```py
((10, 12), (15, 16), (25, 27))
```

### Example 3
```py
intervals_3 = (
    (17, 35),
)

find_gaps(intervals_3)
```
Produces
```py
tuple()  # Empty tuple
```

### Example 4
```py
intervals_4 = (
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
)

find_gaps(intervals_4)
```
Produces
```py
tuple()  # Empty tuple
```
