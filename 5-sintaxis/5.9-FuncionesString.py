texto = "  Python es un buen lenguaje  "
t = texto.upper()
print (t) #"  PYTHON ES UN BUEN LENGUAJ  "
t = texto.lower()
print (t) #"  python es un buen lenguaje  "
t = texto.strip()
print (t) #"Python es un buen lenguaje"
t = texto.replace("e","3")
print (t) #"  Python 3s un bu3n l3nguaj3  "
posi = texto.find("yth")
print (posi) #3 (cuenta los dos blancos del inicio)