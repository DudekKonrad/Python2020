def fibonacci(n):
	previousNumber = 0
	currentNumber = 1
	for i in range(1, n):
		previouspreviousNumber = previousNumber
		previousNumber = currentNumber
		currentNumber = previouspreviousNumber + previousNumber
	return currentNumber

print(fibonacci(13))
