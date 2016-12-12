""" ''.format_map() in Python 2.x
    See more detail: https://gist.github.com/zed/1384338
"""

import sys

try: 
    ''.format_map({})
except AttributeError: # Python < 3.2
    import string
    def format_map(format_string, mapping, _format=string.Formatter().vformat):
        return _format(format_string, None, mapping)
del string

class _safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

def sub(text):
    return format_map(text, _safesub(sys._getframe(1).f_locals))
