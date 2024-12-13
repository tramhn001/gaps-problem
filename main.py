def find_gaps(intervals):
    # Write your solution here!
    pass

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
