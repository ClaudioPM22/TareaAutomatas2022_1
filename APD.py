#Para las trancisiones 
lEstados = []       #contiene los estados de las trancisiones
lSimbolos = []      #contiene los simbolos de las trancisiones
simPila = []      #va marcando los simbolos
lEstadosSgte = []   #contiene los estados a los que se cambia
sgteSimPila = []     

#Datos 
estadoInicial = ""  #contiene al estado inicial
lEstadoFinal = []   #contiene los estados finales
palabra = ""        #contiene la palabra a verificar
pila = []
pila.append("R")
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
""""
p = input("Ingrese la palabra a revisar") 
fin = True
cTran = 0       #contador de trancisiones
print("\n\nIngrese transicion por transicion a continuacion: ")
while(fin):
    estado = input("Ingrese estado: ")
    lEstados.append(estado)
    simbolo = input("Ingrese el simbolo: ")
    lSimbolos.append(simbolo)
    simStack = input("Ingrese simbolo del Stack: ")
    simPila.append(simStack)
    sgteEstado = input("Ingrese el estado al que cambia: ")
    lEstadosSgte.append(sgteEstado)
    sgteStack = input ("Ingrese el siguiente simbolo de stack: ")
    sgteSimPila.append(sgteStack)
    sigue = input("\nSi desea agregar otra transicion digite S: ")
    cTran += 1  #se le suma una al contador despues de pedir cada trancision
    if("S"== sigue or "s"== sigue):    #verifica si el usuario quiere ingresar otra tracision
        fin = True
    else:
        fin = False
"""
lEstados=        ['q0','q0','q0','q1','q1']       #Aqui van las transiciones van por orden[1°transicion, 2°, 3°,...]
lSimbolos=       [ 'a', 'a', 'b', 'b', 'E']
simPila=         [ 'R', 'A', 'A', 'A', 'R']
lEstadosSgte=    ['q0','q0','q1','q1','qf']
sgteSimPila=     ['AR','AA', 'E', 'E', 'R']
"""
(q0, a, R) = (q0, AR)
(q0, a, A) = (q0, AA)
(q0, b, A) = (q1, E)
(q1, b, A) = (q1, E)
(q1, b, R) = (q0, AR)
""" 
simbolosPila = "R" 
p = "aaaabbbb"
c = 0               #contador para recorrer la palabra
i = 0               #contador para recorrer los estados de las trancisiones
stackVacio= False
estadoActual = lEstados[0]
if(estadoActual == estadoInicial):
    while((estadoActual not in lEstadoFinal) and (not stackVacio)):    #Valida si estado en el que estamos esta en los estados finales
        if(estadoActual == lEstados[i]):        #Vemos si el estado en el que estamos coincide con 
            if(p[c] == lSimbolos[i]):           #revisa si la letra de la palabra coincide con el simbolo leido en la trancision
                if(pila[-1] == simPila[i]):       # revisa si la variable esta en el tope de la pila
                    
                    """
                    estadoActual = lEstadosSgte[i]
                    pila.append(sgteSimPila)
                    print("Estado actual")
                    print("Los datos en la pila son: \n", pila)
                    i +=1
                    """



                
        else:
            i+=1        #siguiente trancision
else:
    print("Las trancisiones no comienzan en el estado inicial.")


