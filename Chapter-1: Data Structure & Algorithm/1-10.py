# Removing Duplicates from a sequence while maintaing order

# Problem: You want to eliminate the dublicate values in a sequence, but preserve the order of the remianing items

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(a)
print(list(dedupe(a)))

# for dic
def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [
        {'x': 1, 'y': 2},
        {'x': 4, 'y': 3},
        {'x': 1, 'y': 2},
        {'x': 3, 'y': 9},
    ]

print(list(dedupe(a, key = lambda d: (d['x'], d['y']))))