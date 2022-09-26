#Que es lo que podemos hacer con los strings?
Mystring = "hola mundo"
#print(dir(Mystring))

print(Mystring.upper()) #String mayuscula
print(Mystring.lower()) #String minuscula
print(Mystring.swapcase()) #Letas mayusculas y minusculas
print(Mystring.capitalize()) #1ra letra en mayuscula
print(Mystring.replace("hola","adios :(")) #Reemplazar una parte del string

#se puede definir metodos dentro de otros metodos

print(Mystring.count('l')) #Ver cuantas veces se repite una letra
print(Mystring.startswith("hola")) #Ver si el string inicia con un texto o no
print(Mystring.endswith("Mundo")) #Ver si el string termina con un determinado texto
print(Mystring.split('o')) #Separar el string
print(Mystring.find('o')) #Buscar una letra o parte del string
print(len(Mystring)) #Ver la cantidad de caracteres que posee tu string
print(Mystring.index('o')) #Ver la ubicacion de un caracter dentro de nuestro string
print(Mytring.isnumeric()) #Ver si nuestro string es numero
print(Mystring.isalpha())#Ver si nuestro string es alpha numerico
print(Mystring[4]) #Ver el valor de un indice dentro de nuestro string
print(":D ".format(Mystring))
