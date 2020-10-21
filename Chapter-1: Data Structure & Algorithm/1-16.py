# Filtering Sequence Elements
# Problem: You have data insider of a sequence, and need to extract values
# or reduce the sequence using some criteria.

my_list = [1, 4, -5, 10, -7, 2, 3, -1]
result = [n for n in my_list if n > 0]

pos = (n for n in my_list if n > 0)
print(pos)
for x in pos:
    print(x)

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return

ivals = list(filter(is_int, values))
print(ivals)