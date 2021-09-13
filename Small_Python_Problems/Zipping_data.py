x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))

for point in points:
    print(point)


# OUTPUT

# F: 23, 677, 4
# J: 53, 233, 16
# A: 2, 405, -6
# Q: -12, 433, -42
# Y: 95, 905, 3
# B: 103, 376, -6
# W: 14, 432, 23
# X: -5, 445, -1

# -------------------------------------------------------------------------------------------------------


# Quiz Solution: Zip Lists to a Dictionary

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

# Output:
# The order of elements in this output may vary since dictionaries are unordered.

# {'Lily': 66, 'Barney': 72, 'Marshall': 76, 'Ted': 72, 'Robin': 68}



# -------------------------------------------------------------------------------------------------------

# Unzipping Tuples

cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)

# Output:
# ('Barney', 'Robin', 'Ted', 'Lily', 'Marshall')
# (72, 68, 72, 66, 76)

# -------------------------------------------------------------------------------------------------------


# Transpose with Zip
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

# Output:
# ((0, 3, 6, 9), (1, 4, 7, 10), (2, 5, 8, 11))

# -------------------------------------------------------------------------------------------------------


