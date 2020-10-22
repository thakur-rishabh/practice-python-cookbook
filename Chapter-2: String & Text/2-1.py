# Splitting Strings on Any of Multiple Delimiters
# Problem: You need to split a string, but the delimiters(and spacing around them)
# aren't consistent throughtout the string.

line = 'asdf fjdk; fjek,asdf,   foo'
import re
filter_string = re.split(r'[;,\s]\s*', line)
print(filter_string)