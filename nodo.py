#Clase Nodo simple 
class Nodo:
    def __init__ (self,dato):
        self.siguiente = None
        self.info = dato
        
    def verNodo(self):
        return (self.info)

class Lista_Simple:

    def __init__(self):
        self.primero = None

    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False

    def InsertarPrimero(self, dato):
        temporal = Nodo(dato)
        temporal.siguiente = self.primero
        self.primero = temporal

    def listar(self):
        print(" ***** ")
        temporal=self.primero
        while(temporal!=None):
            print(temporal.verNodo(),end=' ')
            temporal= temporal.siguiente
        
    def BorrarPrimero (self):
        if (self.vacia()==False):
            self.primero = self.primero.siguiente

    def BorrarCola(self):
        anterior = self.primero
        actual = self.primero
        while(actual.siguiente!=None):
            anterior = actual
            actual=actual.siguiente
        anterior.siguiente=None
    
    def ModificarPosicion (self,pos,ele):
        anterior = self.primero
        actual = self.primero
        k=0
        if pos > 0:
            while k!=pos  and actual.siguiente!=None:
                anterior= actual
                actual=actual.siguiente
                k+=1
            if k== pos:
                actual.info = ele

lista = Lista_Simple()
lista.InsertarPrimero(1)
lista.InsertarPrimero(2)
lista.InsertarPrimero(3)
lista.InsertarPrimero(4)
#lista.listar()
#lista.BorrarPrimero()
#lista.BorrarCola()
#lista.ModificarPosicion(2,8)
#lista.listar()

if __name__ == '__main__':
    #lista = Lista_Simple()
    salir = True
    while(salir):
        print("*** Menu *** \n"+
            "1. Agregar \n"+
            "2. Listar \n"+
            "3. Modificar \n"+
            "4. Eliminar \n"+
            "5. Salir ")
        num = input("Ingrese la Opcion: ")
        if num == "1":
            elemento = input("ingrese el elemento: ")
            lista.InsertarPrimero(elemento)
        elif num == "2":
            lista.listar()
        elif num == "3":
            p = int(input("Ingrese la posicion del elemento a cambiar: "))
            el = int (input("Ingrese nuevo elemento: "))
            lista.ModificarPosicion(p,el)
        elif num == "4":
            lista.BorrarPrimero()
        elif num == "5":
            salir = False