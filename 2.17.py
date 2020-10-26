import re
line = "Guido van Rossum is a Dutch programmer\n" \
       "best known as the creator of the Python programming language.\n" \
       "He is currently a member of the Python Steering Council.\n"
result = re.findall(r'\w+', line)
sorted_list = sorted(result, key=str.lower)
print(sorted_list)