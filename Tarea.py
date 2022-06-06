 #Implementación de una pila en pyhton
 
from inspect import stack
from xmlrpc.client import boolean


class Stack: # Creamos la clase Stack
    def __init__(self):
        self.items = []
     
    def is_empty(self): # Metodo para verificar si la pila esta vacia
        return self.items == []
     
    def push(self, item): # Metodo para insertar elementos a la pila
        self.items.insert(0, item)
     
    def pop(self): # Metodo para eliminar el ultimo elemento apilado
        return self.items.pop(0)
     
    def print_stack(self): # Metodo para mostrar los elementos de la pila
        print(self.items)




# ingresamos algunos elementos a la pila
#pila.push('a')
#pila.push('b')
#pila.push('c') 
#pila.print_stack() # Mostramos los elementos de la pila
#pila.pop() # Utilizamos el metodo pop
#pila.print_stack() # Mostramos nuevamente los elementos de la pila

#(q0, a, R) => (q0, AR)
#(q0, a, A) => (q0, AA)

#Para las trancisiones 
lEstados = []       #contiene los estados de las trancisiones
lSimbolos = []      #contiene los simbolos de las trancisiones
pila = Stack()      #va marcando los simbolos
lEstadosSgte = []   #contiene los estados a los que se cambia
#pila1 = Stack()     

#Datos extras
estadoInicial = ""  #contiene al estado inicial
lEstadoFinal = []   #contiene los estados finales
palabra = ""        #contiene la palabra a verificar

def largo_palabra(x):       #funcion para ver el largo de una palabra
    l = 0
    for i in x:
        l+= 1
    return l

estadoInicial = input("Ingrese estado inicial: ") # recibimos el estado inicial
fin = True
while(fin):
    estadoFinal = input("Ingrese un estado final: ")
    lEstadoFinal.append(estadoFinal)
    sigue = input("Si desea agregar otro estado final digite S(sino enter): ")
    if("S"== sigue):
        fin = True
    else:
        fin = False
fin = True
print("\n\nIngrese transicion por transicion a continuacion: ")
while(fin):
    estado = input("Ingrese estado: ")
    lEstados.append(estado)
    simbolo = input("Ingrese el simbolo: ")
    lSimbolos.append(simbolo)
    simStack = input("Ingrese simbolo del Stack: ")
    pila.push(simStack)
    sgteEstado = input("Ingrese el estado al que cambia: ")
    lEstadosSgte.append(sgteEstado)
    sgteStack = input ("Ingrese el siguiente simbolo de stack: ")
    pila1 = Stack()
    sigue = input("Si desea agregar otra transicion digite S: ")
    if("S"== sigue):
        fin = True
    else:
        fin = False
"""
lEstados=        ['q0','q0','q0','q1','q1']       #Aqui van las transiciones van por orden[1°transicion, 2°, 3°,...]
lSimbolo=        [ 'a', 'a', 'b', 'b', 'E']
actualStack=     [ 'R', 'A', 'A', 'A', 'R']
estadoSiguiente= ['q0','q0','q1','q1','qf']
reemplazoStack=  ['AR','AA', 'E', 'E', 'R']
 pila = "AAR" 
 "aaaabbbb"
 ""
estadoActual = lEstados[0]
estadoActual = estadoInicial # q0
if(estadoActual != )

"""




