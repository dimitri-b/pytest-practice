# redundant_math.py

"""
Totally redundant functions to multiply a pair of values.

Examples:

>>> import redundant_math as rm

>>> rm.multiply(2, 6)
12
>>> rm.multiply('a', 3)
'aaa'
>>> rm.divide(12, 4)
3.0
"""


def multiply(a, b):
    """Returns the product of a and b, for example:
    >>> rm.multiply(4, 3)
    12
    >>> rm.multiply('foo', 2)
    'foofoo'
    """
    return a * b


def divide(a, b):
    """Returs the result of the division, e.g.
    >>> rm.divide(12, 2)
    6.0
    """
    return a / b
