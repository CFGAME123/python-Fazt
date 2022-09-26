#lista
Prueba = [1,10.1,True,[2]]
colores = ["amarillo", "azul", "rojo"]

#constructor
lista = list((1,2,3,"hola",True,10.1)) #llamar una tupla para crear una lista
print(lista)

#rangos
R = list(range(1,6)) #de donde a donde va a ir nuestra lista, es decir sus valores tienen un incio y tiene un final
print(R)

#mostrar informacion que se puede hacer con una lista | metodos
print(dir(colores)) #investiga sobre eso es muy importante

#saber si un elemento existe dentro de una lista
print('amarillo' in colores)

#cambio de valores
print(colores)
colores[1] = 'Verde'
print(colores)
