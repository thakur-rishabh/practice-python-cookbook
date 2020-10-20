# Sorting a list of Dict by a common key
# Problem: You have a list of dict and you would like to sort the entries according to one more of the dictionary values.

from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'Rishabh', 'lname': 'Thakur', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_lname = sorted(rows, key=itemgetter('lname'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

print(rows_by_fname)
print(rows_by_lname)
print(rows_by_lfname)

# better than min and max function due to fast processing