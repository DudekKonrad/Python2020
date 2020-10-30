dictionary = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}
result = 0
roman = input("Enter number in roman system: ")
for i in range(len(roman)):
	if i > 0 and dictionary[roman[i]] > dictionary[roman[i - 1]]:
		result += dictionary[roman[i]] - 2 * dictionary[roman[i - 1]]
	else:
		result += dictionary[roman[i]]
print("Your input before:", roman)
print("Result:", result)
