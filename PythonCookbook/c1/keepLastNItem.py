#!/etc/bin/env python
# -*- coding: utf-8 -*-
#
# Keeping the Last N Items

from collections import deque
from string import ascii_uppercase as upCase
import random

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    tmp = list()
    for i in range(100):
        tmp.append(random.choice(upCase))

    print tmp
    for letter, pre_letter in search(tmp, 'A', 3):
        print letter, ':',
        for item in pre_letter:
            print item,
        print 
    
