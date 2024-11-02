def pipe(*args):
    if not all(callable(i) for i in args):
        raise TypeError

    def comp(x):
        for f in args:
            x = f(x)
        return x
    return comp

def pipe_1(*args):
    if not all(callable(i) for i in args):
        raise TypeError

    def comp(x):
        for f in args[::-1]:
            x = f(x)
        return x
    return comp


inc = lambda x: x + 1
twice = lambda x: x * 2
cube = lambda x: x ** 3
h = pipe(inc, twice, cube)
j = h(2)
h_1 = pipe_1(inc, twice, cube)
j_1 = h_1(2)


print(j, j_1)