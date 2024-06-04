#Importa tudo do modulo
import matematica

#importa elementos específicos
from matematica import PI, somar
#from matematica import *
#from matematica import PI as PI_MAT, somar as somar_mat

from estatistica.descritiva import media, maximo, minimo
from estatistica.inferencial import VALOR

PI=99999

print(matematica.PI)

print(matematica.somar(10, 3))