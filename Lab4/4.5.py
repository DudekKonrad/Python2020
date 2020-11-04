def odwracanie(L, left, right):
	temp = 0
	for i in range(int((right - left)/2+1)):
		temp = L[right - i]
		L[right - i] = L[left + i]
		L[left + i] = temp

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Before reverse:", L)
odwracanie(L, 5, 13)
print("After reverse: ", L)
