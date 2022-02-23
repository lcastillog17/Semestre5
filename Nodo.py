from tkinter import N
from wsgiref.validate import validator


class Nodo:
    #se pne def antes de todo metodo
    #al constructor se le pone __init__()
    #cuando hay dos guiones bajos al principio y al final es porque es un metodo construido por el mismo lenguaje
    #hay que poner self antes de los parametros, y si no hay parametros se pone igual, el self es como el this es para especificar que una 
    #no se crean aqui las propiedades
    
    def __init__(self, valor, dcho=None, izdo=None):
        self.dato=valor
        self.dcho=dcho
        self.izdo=izdo

    def ValorNodo(self):
        return self.dato

    def getSubArbolIzdo(self):
        return self.izdo

    def getSubArbolDcho(self):
        return self.dcho

    def nuevoValor(self, d):
        self.dato=d

    def setRamaIzdo(self, n):
       self.izdo=n

    def setRamaDcho(self, n):
        self.dcho=n
    
#primer_nodo = Nodo(1, Nodo(2), Nodo(3))


#print(primer_nodo.ValorNodo())

#print(primer_nodo.getSubArbolIzdo().ValorNodo())
#print(primer_nodo.getSubArbolDcho().ValorNodo())

