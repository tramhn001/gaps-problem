def find_gaps(intervals):
    # Write your solution here!
    # Input: tuple of tuples, not sorted
    # Output: sorted tuple of gaps 
    # If there no gap, return empty tuple
    
    # Pseudo code:
    # Sort the intervals
    # Initialize result variable, add the gap between the second element of the first tuple and the first elem. of the second, and go on
    # Return result

    result = []

    sorted_intervals = sorted(intervals)

    for i in range(len(sorted_intervals) - 1):
        current = sorted_intervals[i]
        next = sorted_intervals[i + 1]
        if current[1] < next[0]:
            result.append((current[1], next[0]))
 
    return tuple(result)

intervals_1 = (
    (5, 10),
    (12, 15),
    (16, 20),
    (20, 25),
    (27, 30),
)

assert find_gaps(intervals_1) == ((10, 12), (15, 16), (25, 27))

intervals_2 = (
    (27, 30),
    (16, 20),
    (12, 15),
    (20, 25),
    (5, 10),
)
assert find_gaps(intervals_2) == ((10, 12), (15, 16), (25, 27))

intervals_3 = (
    (17, 35),
)
assert find_gaps(intervals_3) == tuple()

intervals_4 = (
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 5),
)
assert find_gaps(intervals_4) == tuple()

print("All tests passed!")
print("Discuss time and space complexity if there's time remaining")
