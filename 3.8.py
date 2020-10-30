sequence1 = [[4], (1, 2), [3, 4], (5, 6, 7), [9], (6, 8), [6, 5], 8]
sequence2 = [[4], (1, 2), [3, 4], (5, 6, 7), [8], (6, 5), (1, 2), [6, 5], [6, 5]]
result_intersection = []
result_sum = []
for item1 in sequence1:
	print("item1:", item1)
	for item2 in sequence2:
		print("item2:", item2)
		if item1 == item2:
			result_intersection.append(item2)
			print("Added:", item2)
			break

for item in sequence1:
	if item not in result_sum:
		result_sum.append(item)
for item in sequence2:
	if item not in result_sum:
		result_sum.append(item)

print("Intersection:", result_intersection)
print("Sum:", result_sum)