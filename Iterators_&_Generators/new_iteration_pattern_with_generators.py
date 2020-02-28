def frange(start, stop, increment=1):
    x = start
    while x < stop:
        yield x
        x += increment

for n in frange(4, 8):
    print(n)
