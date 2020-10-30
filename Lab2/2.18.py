number = 10240230420001230010
string_number = str(number)
result = 0
for char in string_number:
	if char == "0":
		result += 1
print("The number of zero's in digit:",number, "is:", result)