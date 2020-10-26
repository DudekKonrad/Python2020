word = "word"
result = ""
x = 0
for x in range(len(word)):
	result = result + word[x] + "_"
	x += 1
result = result[:len(result)-1] + "" + result[len(result):]
print(result)