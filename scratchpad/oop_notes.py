class MyClass(object):
    pass


class SomeError(Exception):
    """Sample exception."""
    pass


c = MyClass()
o = object()

print(dir(c))
print(dir(o))

raise SomeError
