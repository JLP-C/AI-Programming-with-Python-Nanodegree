"""
Implement a generator function, chunker, that takes in an iterable
and yields a chunk of a specified size at a time.
"""

def chunker(iterable, size):
    i = 0
    while i < len(iterable):
        if i % size == 0:
            yield iterable[i:i+size]
        i += 1

"""Mejor solución:
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
"""

for chunk in chunker(range(25), 4):
    print(list(chunk))
