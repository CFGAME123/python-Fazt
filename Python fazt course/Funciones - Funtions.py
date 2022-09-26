def saludo(saludoDox): #def() nos sirve para crear funciones | se le puede agregar parametros dentro de los  "()"
	print("hola " + saludoDox)
saludo('Jorge') #llamar a una funcion

#calculadora | prueba
def add(n1,n2): #se puede agregar cuatos parametros se deseen
	return n1 + n2
print(add(10,30))

#fuciones lambda
add = lambda N1,N2: N1+N2
print(add(10,30))
#explicacion: crear funcion, se llama al lambda y se le dan sus parametros y luego se le asignan sus valores