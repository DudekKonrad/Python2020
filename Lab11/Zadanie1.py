import random


def losowe_liczby(N):
  liczby = []
  for i in range(0, N):
      liczby.append(i)
  random.shuffle(liczby)
  return liczby


def prawie_posortowane_liczby(N):
  liczby = []
  for i in range(0, N):
    liczby.append(i)
  for i in range(1, N):
    j = random.randint(i - 1, i)
    liczby[i], liczby[j] = liczby[j], liczby[i]
  return liczby


def prawie_odwrotnie_posortowane_liczby(N):
  liczby = prawie_posortowane_liczby(N)
  liczby.reverse()
  return liczby


def gauss_liczby(N):
  liczby = []
  for i in range(N):
    liczby.append(random.gauss(0, 1))
  return liczby


def powtarzajace_liczby(N):
  liczby = []
  for i in range(N):
    liczby.append(random.randint(0, N // 2))
  random.shuffle(liczby)
  return liczby
