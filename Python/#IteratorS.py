#IteratorS
# Iterator = An object that returns elements one at a time from a sequence (or data stream) and remembers its position between calls.
# A Python object is an iterator if it has:
# __iter__() → Returns the iterator object itself
# __next__() → Returns the next item in the sequence
# (raises StopIteration when there's no more items)
nums = [1, 2, 3, 4, 5]


# for n in nums:
#     print(n)

it = iter(nums)
print(next(it))
print(next(it))
print(next(it))

