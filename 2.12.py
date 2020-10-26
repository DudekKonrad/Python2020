import re
line = "Guido van Rossum is a Dutch programmer\n" \
       "best known as the creator of the Python programming language.\n" \
       "He is currently a member of the Python Steering Council.\n"
result = re.findall(r'\w+', line)
print(result)
first = ""
last = ""
for word in result:
	first += word[0]
	last += word[len(word)-1]
print("First: ", first)
print("Last: ", last)