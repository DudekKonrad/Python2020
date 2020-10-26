import re
line = "Guido van Rossum is a Dutch programmer\n" \
       "best known as the creator of the Python programming language.\n" \
       "He is currently a member of the Python Steering Council.\n"
result = re.findall(r'\w+', line)
sorted_alphabetically = sorted(result, key=str.lower)
sorted_by_length = sorted(result, key=len)
print("Sorted alphabetically: ")
print(sorted_alphabetically)
print("Sorted by length:")
print(sorted_by_length)
