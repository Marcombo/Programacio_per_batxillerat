dict1 = {"nombre": "Lara", "edad": 30}

#añadimos con sintaxis de corchetes
dict1["oficio"] = "Médica"
#sil la clave ya existía, actualiza el valor
dict1["edad"] = 31
print(dict1)

#añadimos con update()
nuevos_elementos = {"altura": 172, "peso": "68"}
dict1.update(nuevos_elementos)
print(dict1)

#uso de setdefault()
#como la clave ya existía, no actualiza el valor
valor =dict1.setdefault("nombre", "Yaiza")
print (valor) 
#como la clave no existía, mete el par {clave:valor}
valor =dict1.setdefault("pelo", "rubio")
print (valor)
print (dict1)