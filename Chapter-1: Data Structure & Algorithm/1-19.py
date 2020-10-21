# Transforming and Reduction Data at the Same Time
# Problem: You need to execute a reduction function
# (eg. sum()), but first need to transform or filter the data

nums = [1, 2, 3, 4, 5]
s = sum(x for x in nums)
print(s)
