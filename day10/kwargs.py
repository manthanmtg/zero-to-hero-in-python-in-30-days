def foo(a, b, **kwargs):
    print(kwargs)
    print(type(kwargs))

foo(1, 4, c = 3, d = 47)