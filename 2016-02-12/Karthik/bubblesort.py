"""
Author: K@rthik Bh@t K.
Date: March 14, 2016 11:23 AM

Last Commit: Added reverse sorting option
Description: 
This code manually sorts the items of a iterable by swapping items.
The iterables can be a list or dict.
"""
from collections import OrderedDict


def bubblesort(iterable, reverse=False):
    if isinstance(iterable, list):
        for I in xrange(len(iterable)):
            for j in xrange(len(iterable)):
                if reverse:
                    if iterable[I] > iterable[j]:
                        # swap items
                        temp = iterable[I]
                        iterable[I] = iterable[j]
                        iterable[j] = temp
                else:
                    if iterable[I] < iterable[j]:
                        # swap items
                        temp = iterable[I]
                        iterable[I] = iterable[j]
                        iterable[j] = temp
        return iterable
    elif isinstance(iterable, dict):
        # Sort the keys and insert keys in that order.
        keys = bubblesort(iterable.keys(), reverse=reverse)

        # OrderedDict remembers the insertion Order which is not done by normal dict.
        sorted_dict = OrderedDict()
        for key in keys:
            sorted_dict[key] = iterable[key]
        return sorted_dict


unsorted_dict = {72:6, 85:2, 32:4, 49: 7, 'a':42, 'anish':'ram'}
# d = ['a', 1, 'v', 4, 2, 'karthik', 76] 
print bubblesort(unsorted_dict, reverse=True) 
