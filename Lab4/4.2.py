def draw_table():
	x = input("Enter x value: ")
	y = input("Enter y value: ")
	top = ""
	mid = ""
	result = ""
	for i in range(int(y)):
		top += "+---"
		mid += "|   "
	result += top + "+\n"
	for i in range(int(x)):
		result += mid + "|\n"
		result += top + "+\n"
	return result

def draw_ruler():
	x = input("Enter length of ruler: ")
	x = int(x)
	ruler = ""
	ruler += "|"
	ruler_down = "0"
	for i in range(x):
		ruler += "....|"
	for i in range(x):
		i += 1
		to_add = '{:>5}'.format(i)
		ruler_down += to_add
	ruler += "\n" + ruler_down
	return ruler

print("Drawing table function test")
print(draw_table())
print("Drawing ruler function test")
print(draw_ruler())
