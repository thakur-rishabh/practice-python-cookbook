# Cobining Multiple Mappings into a Single Mapping
# Problem: You have multiple dict or mappings that 
# you want to logically combine into a single mapping 
# to perform certain operations, such as looking up values
# or checking for the existence of keys.

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

# We could use merge function but if there is change
# in orignal dict it will not relflect into the merged dict.
# Any changes done would be done on the first dict.