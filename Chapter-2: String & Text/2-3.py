# Match Strings Using Shell Wildcards
# Problem: You want to match text using the same wildcard patterns
# as are commonly used when working in Unix  shells

from fnmatch import fnmatch, fnmatchcase

print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))

names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# If upper case or lower case matter then use fnmatchcase i.e by default
# fnmatch uses system filesystem underline rules for case-sensitive