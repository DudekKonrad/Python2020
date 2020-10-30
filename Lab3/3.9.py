sequence = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
result = []
print("Sequence before sum: ", sequence)
for i in range(len(sequence)):
	result.append(sum(sequence[i]))
print("Result: ", result)