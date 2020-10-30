x = input("Enter x value: ")
y = input("Enter y value: ")
top = ""
mid = ""
for i in range(int(y)):
	top += "+---"
	mid += "|   "
print(top + "+")
for i in range(int(x)):
	print(mid + "|")
	print(top + "+")