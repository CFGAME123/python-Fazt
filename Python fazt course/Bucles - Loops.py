#realizar ua tarea tipica que va relacionada con una lista de datos
#bucle for
foods = ["apple","milk","cheese","banana"]
for food in foods:
	if food == "cheese":
		print("Compralo")
		continue #para continuar con la ejecucion del bucle | continue
		break #para romper la ejecucion del bucle | break
	print(food)
#explicacion: en la lista se va a recordar su interior y mostrar en pantala y se almacean dentro de la variable asignada al bucle

#recorrer un rango
for number in range(1,11): #definir una variable que es cada uno de los items del rango
	print(number)

#bucle while
count = 4
while count <= 10:
	print(count)
	count = count+1