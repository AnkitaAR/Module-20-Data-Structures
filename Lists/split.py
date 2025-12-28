# Define a list of integers from 1 to 10
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Index where the list will be split
n = 4

# Slice the list from the beginning to the nth index (not inclusive)
first_slice = my_list[:n]

# Slice the list from the nth index to the end
second_slice = my_list[n:]

# Print the first slice of the list
print("First slice:", first_slice)
# Print the second slice of the list
print("Second slice:", second_slice)