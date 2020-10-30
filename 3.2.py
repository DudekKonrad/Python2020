
x, y = 1, 2, 3 #za dużo wartości (3 wartośći przypisywane do 2 zmiennych)

X = 1, 2, 3 ; X[1] = 4 #Zawartość krotki określamy tylko podczas jej tworzenia, później nie możemy jej zmienić

X = [1, 2, 3] ; X[3] = 4 #Próba wyjścia poza indeks listy. Ta lista ma tylko indeksy 1, 2, 3

X = "abc" ; X.append("d") #Do obiektu string nie możemy używać funkcji .append()

L = list(map(pow, range(8))) #Funkcji pow() brakuje argumentów