numbers_list = [1, 12, 345, 52, 5, 7, 8, 3, 99, 71]
result = []
for number in numbers_list:
	str_number = str(number)
	if len(str_number) < 3:
		result.append(str_number.zfill(3))
	else:
		result.append(str_number)
print(result)