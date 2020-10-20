# Determin the most frequently occurring items in a sequence
# Problem: You have a sequence of items, and you'd like to determine the most frequently occuring items in the sequence.

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'around', 'the', 'eyes', 'look', 'into', 'my', 
    'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for words in morewords:
    word_counts[words] += 1
print(word_counts['eyes'])