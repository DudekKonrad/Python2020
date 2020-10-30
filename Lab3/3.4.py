x = 0
while (True):
	x = input("Enter a float number: ")
	if x == "stop":
		break
	else:
		try:
			x = float(x)
			print("Normal: ", x, "To the power of 3: ", pow(x, 3))
		except:
			print("It is not a float")
			continue