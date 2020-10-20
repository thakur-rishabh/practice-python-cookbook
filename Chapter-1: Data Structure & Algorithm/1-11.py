# Naming a slice
# Problem: Your program has become an unreadable mess of hradcoded slice indices and you want to clean up.
record = '........100    .....200.23 ........'
cost = int(record[8:11]) * float(record[21:26])
print(cost)