line = "GvR is a Dutch programmer\n" \
       "best known as the creator of the Python programming language.\n" \
       "He is currently a member of the Python Steering Council.\n"
print(line)
print("Before replace:")
print(line)
result = line.replace("GvR", "Guido van Rossum")
print("After replace:")
print(result)