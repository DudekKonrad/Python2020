x = input("Enter length of ruler: ")
x = int(x)
ruler = ""
print("Lenght: ", x)
ruler += "|"
ruler_down = "0"
for i in range(x):
	ruler += "....|"
for i in range(x):
	i += 1
	to_add = '{:>5}'.format(i)
	ruler_down += to_add
print("Ruler: ")
print(ruler)
print(ruler_down)