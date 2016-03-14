from collections import OrderedDict


def bubblesort(iterable) :
    if isinstance(iterable, list) :
        for I in xrange(len(iterable)) :
            for j in xrange(len(iterable)) :
                if iterable[I] < iterable[j] :
                    temp = iterable[I] 
                    iterable[I] = iterable[j] 
                    iterable[j] = temp
        return d
    elif isinstance(d, dict) :
        keys = bubblesort(d.keys())
        udict = OrderedDict() 
        for key in keys:
            udict[key] = d[key] 
        return udict

d = {72:6, 85:2, 32:4, 49: 7, 'a':42, 'anish':'ram'}
#d = ['a', 1, 'v', 4, 2, 'karthik', 76] 
print bubblesort(d) 
