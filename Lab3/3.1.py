x = 2; y = 3; #Wszystko w porządku
if (x > y): #Wszystko w  porządku
    result = x;
else:
    result = y;

for i in "qwerty": if ord(i) < 100: print (i) #Instrukcja if powinna rozpoczynać się od nowej linijki z tabulacją

for i in "axby": print (ord(i) if ord(i) < 100 else i) #Wszystko w porządku