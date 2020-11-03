final_result = []
def flatten(sequence):
	result = []
	if isinstance(sequence, (list, tuple)):
		for item in sequence:
			flatten(item)
	else:
		final_result.append(sequence)
	return final_result


# S = [1, [1, 1], [], (2, 5), (3, (4, 4, 4, [1, 10]))]
s = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(s))
