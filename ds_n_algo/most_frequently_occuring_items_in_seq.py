from collections import Counter

words = ['look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my', 'eyes', 'under']

words_counts = Counter(words)
top_three = words_counts.most_common(3)
print(top_three)
