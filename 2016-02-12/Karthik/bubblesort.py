from collections import *
def bubblesort(d) :
    if isinstance(d, list) :
        for I in xrange(len(d)) :
            for j in xrange(len(d)) :
                if d[I] < d[j] :
                    temp = d[I] 
                    d[I] = d[j] 
                    d[j] = temp
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