#Quick Sort
def partition(arr, low, high):
	i = (low - 1)
	pivot = arr[high]

	for j in range(low, high):
		if arr[j] <= pivot:
			i = i + 1
			arr[i], arr[j] = arr[j], arr[i]

	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	return i + 1


def quickSort(arr, low, high):
	if len(arr) == 1:
		return arr
	if low < high:
		pi = partition(arr, low, high)
		quickSort(arr, low, pi - 1)
		quickSort(arr, pi + 1, high)
##

def mediana_sort(L, left, right):
	leng = right - left
	quickSort(L, left, right)
	if leng % 2 == 0:
		return L[int(leng/2)]
	else:
		result = (L[int((leng)/2-0.5)] + L[int((leng)/2+0.5)])/2
		return result


lista = [1, 6, 8, 6, 6, 4, 10, 5, 9, 7, 1]
print("Lista: ", lista)
result = mediana_sort(lista, 0, 2)
print("Mediana: ", result)
