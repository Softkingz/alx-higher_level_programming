#!/usr/bin/python3

def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string."""
    return ''.join(x for x in my_string if x not in {'c', 'C'})
