from Zadanie1 import *
import time


def partition(tab, l, h):
	i = (l - 1)
	x = tab[h]

	for j in range(l, h):
		if tab[j] <= x:
			i = i + 1
			tab[i], tab[j] = tab[j], tab[i]

	tab[i + 1], tab[h] = tab[h], tab[i + 1]
	return (i + 1)


def quickSortIteracyjny(tab):
	begin = 0
	end = len(tab) - 1
	stack = [0] * (len(tab))
	top = -1
	top = top + 1
	stack[top] = begin
	top = top + 1
	stack[top] = end

	while top >= 0:

		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1

		p = partition(tab, l, h)

		if p - 1 > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = p - 1

		if p + 1 < h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h


print("Sortowanie testowe:")
tab = [4, 3, 5, 2, 1, 3, 2, 3]
quickSortIteracyjny(tab)
print("Sorted tab is:", tab)

print('Losowe liczby:')
liczby = losowe_liczby(100000)
start0 = time.time()
quickSortIteracyjny(liczby)
end0 = time.time()
print("Czas trwania: ", end0 - start0, '\n')

print('Prawie posortowane liczby:')
liczby = prawie_posortowane_liczby(10000)
start1 = time.time()
quickSortIteracyjny(liczby)
end1 = time.time()
print("Czas trwania: ", end1 - start1, '\n')

print('Prawie odwrotnie posortowane liczby:')
liczby = prawie_odwrotnie_posortowane_liczby(10000)
start2 = time.time()
quickSortIteracyjny(liczby)
end2 = time.time()
print("Czas trwania: ", end2 - start2, '\n')

print('Powtarzające się liczby:')
liczby = powtarzajace_liczby(10000)
start3 = time.time()
quickSortIteracyjny(liczby)
end3 = time.time()
print("Czas trwania: ", end3 - start3, '\n')

print('Liczby o rozkładzie gaussowskim:')
liczby = gauss_liczby(10000)
start4 = time.time()
quickSortIteracyjny(liczby)
end4 = time.time()
print("Czas trwania: ", end4 - start4, '\n')
