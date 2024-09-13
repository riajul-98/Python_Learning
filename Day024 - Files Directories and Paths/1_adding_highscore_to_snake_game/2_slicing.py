piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

print(piano_keys[2:5])
# The last index is not included. Can think of it like this "To but not including index 5".

print(piano_keys[2:])
# You can slice the list to include all the numbers from the starting point specified by adding the starting index but
# omitting the end index.

print(piano_keys[:5])
# You can also do the same in the opposite direction. Here we will omit the starting index and specify where we want
# the slice to end. This will not include the index specified.

print(piano_keys[2:5:2])
# We can also add an increment value which will come after the end value.

print(piano_keys[::-1])
# You can also use -1 for the increment value to reverse the list.

piano_tuple = ('do', 're', 'mi', 'fa', 'so', 'la', 'ti')
# The same slicing techniques can be used on tuples.

print(piano_tuple[2:5])