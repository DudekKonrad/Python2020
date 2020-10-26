import re
line = "Guido van Rossum is a Dutch programmer\n" \
       "best known as the creator of the Python programming language.\n" \
       "He is currently a member of the Python Steering Council.\n"
result = re.findall(r'\w+', line)
longest_word = max(result, key=len)
print("Longest word is: ", longest_word, "\nLength of longest word is: ", len(longest_word))