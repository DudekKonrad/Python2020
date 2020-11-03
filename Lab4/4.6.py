def sum_sequence(sequence):
	result = 0
	for item in sequence:
		if isinstance(item, (list, tuple)):
			result += sum_sequence(item)
		else:
			result += item
	return result

S = [1, [1, 1], (2,5), (3,(4, 4, 4,[1, 10]))]
print(sum_sequence(S))
