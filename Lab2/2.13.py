import re
line = "Guido van Rossum is a Dutch programmer\n" \
       "best known as the creator of the Python programming language.\n" \
       "He is currently a member of the Python Steering Council.\n"
result = re.findall(r'\w+', line)
length = 0
for word in result:
	length += len(word)
print("Length of all words in line is: ", length)