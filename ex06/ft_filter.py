def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        new_iter = [x for x in iterable if x]
    else:
        new_iter = [x for x in iterable if function(x)]
    return (new_iter)


# iter = ["hello", "2", "i", '']

# nums = [2, -1, 3, 0]

# floats = [float('NaN'), float(4), float(1), float(0)]


# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False


# real = filter(None, nums)
# my = ft_filter(None, nums)

# print("my:", end=' ')
# for i in my:
#     print(i, end=' ')
# print()
# print("real", end=' ')
# for i in real:
#     print(i, end=' ')
# print()
