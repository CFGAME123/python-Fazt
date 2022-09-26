#Ivestiga sobre los modulos en la pagina de modulos de pytho
#Esto te ayudara bastante en un futuro :/

#llamar modulos
import datetime
from datetime import timedelta

print(datetime.date.today())
print(datetime.timedelta(minutes = 100))

#llamar a nuestro modulo hecho anteriormente
import ModuloPropio #llamamos a nuestro modulo | 1ra forma
from ModuloPropio import sum, rest #2da forma
ModuloPropio.sum(1,2)
ModuloPropio.rest(3,9)