#!/etc/bin/env python
# -*- conding: uft-8 -*-
#
# Sorting a List of Dictionaries (list, tuple, ...) by a Common Key (specific region)
# can be applied to functions such as min() and max()

import random

# equivalent to operator.itemgetter
def itemgetter(*items):
    if len(items) == 1:
        item = items[0]
        def g(obj):
            return obj[item]
    else:
        def g(obj):
            return tuple(obj[item] for item in items)
    return g

if __name__ == '__main__':
    l = list()
    for i in range(10):
        tmp = list()
        for j in range(5):
            tmp.append(random.randint(0, 10))
        l.append(tmp)

    print l
    print sorted(l, key=itemgetter(2))
    print '-'*20

    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
    ]
    print rows
    print sorted(rows, key=itemgetter('fname'))
    print '-'*20

    inventory = [('apple', 3), ('banana', 2), ('pear', 5), ('orange', 1)]
    getcount = itemgetter(1)
    print map(getcount, inventory)
    print sorted(inventory, key=getcount)
